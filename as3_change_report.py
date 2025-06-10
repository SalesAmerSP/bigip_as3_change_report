#!/usr/bin/env python3

'''
Author: G-Rob (grob@f5.com)
Title: AS3 Change Report

'''

import sys
import argparse
import getpass
import logging
import requests
import urllib3
import tempfile
import json


# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def _parse_args():
    try:
        logger.debug("Parsing CLI arguments")
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-user', '--username', help='BIG-IP username', required=True
        )
        parser.add_argument(
            '-pass', '--password', help='BIG-IP password', required=True
        )
        parser.add_argument(
            '-host', '--hostname', help='BIG-IP Host IP address or FQDN', required=True
        )
    except Exception as e:
        logger.error(e)
        sys.exit(1)
    logger.debug("parsing CLI arguments complete")
    args = parser.parse_args()
    hostname = args.hostname or input("BIG-IP hostname: ")
    username = args.username or input("BIG-IP username: ")
    password = args.password or getpass.getpass("BIG-IP password: ")
    # Log everything except password for security best practices
    logger.debug(f"parsed variables: hostname={hostname}, username={username}")
    return (hostname, username, password)

def bigip_get(username, password, url, headers):
    try:
        logger.debug(f"Attempting HTTP GET to BIG-IP at {url}")
        apiRequest = requests.Session()
        apiRequest.verify = False
        apiRequest.auth = (username, password)
        apiRequest.headers = headers    
        apiResponse = apiRequest.get(url)
        apiResponse.raise_for_status()
        logger.info(f"Successful API call to BIG-IP at {url}")
        logger.debug(f"iControl REST Response: {apiResponse.text}")
        return apiResponse
    except Exception as e:
        logger.error(f"Unable to connect to BIG-IP at {url}: {e}")
        raise ConnectionError(f"Unable to connect to BIG-IP at {url}")

def bigip_post(username, password, url, headers, payload):
    try:
        logger.debug(f"Attempting HTTP POST to BIG-IP at {url}")
        apiRequest = requests.Session()
        apiRequest.verify = False
        apiRequest.auth = (username, password)
        apiRequest.headers = headers        
        apiResponse = apiRequest.post(url, json=payload)
        apiResponse.raise_for_status()
        logger.info(f"Successful API call to BIG-IP at {url}")
        logger.debug(f"iControl REST Response: {apiResponse.text}")
        return apiResponse
    except Exception as e:
        logger.error(f"Unable to connect to BIG-IP at {url}: {e}")
        raise ConnectionError(f"Unable to connect to BIG-IP at {url}")


# Run the program if called from the command line
if __name__ == "__main__":
    # Configure Logging
    logger = logging.getLogger(__name__)
    logger.setLevel('DEBUG')
    ch = logging.StreamHandler()
    ch.setLevel('INFO')
    fh = logging.FileHandler('as3_change_report.log')
    fh.setLevel('DEBUG')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    
    # Parse CLI arguments
    hostname, username, password = _parse_args()

    # Log AS3 Version
    url = f"https://{hostname}/mgmt/shared/appsvcs/info"
    headers = {}
    response = bigip_get(username, password, url, headers)
    as3_info = response.json()
    logger.debug(f'AS3 Info: {as3_info}')
    
    # Get AS3 from BIG-IP
    url = f"https://{hostname}/mgmt/shared/appsvcs/declare"
    headers = {
        "Content-Type": "application/json"
    }
    response = bigip_get(username, password, url, headers)
    logging.debug(f'AS3 Response: {response.text}')
    as3_declarations = response.json()

    # Add the AS3 schema link to the declaration
    as3_schema_version = as3_declarations['schemaVersion'] or 'latest'
    as3_base_schema_url = f"https://raw.githubusercontent.com/F5Networks/f5-appsvcs-extension/refs/heads/main/schema/{as3_schema_version}/as3-schema.json"
    as3_declarations['$schema'] = as3_base_schema_url

    # Add the dry-run operator to the declaration
    as3_declarations['controls']['dryRun'] = True

    # Set the logging level for AS3 to debug
    as3_declarations['controls']['logLevel'] = 'debug'

    # Create a temporary file and export AS3 declarations to it
    temp_file = open("as3_declarations.json", "w")
    temp_file.write(json.dumps(as3_declarations, indent=4))
    temp_file.close()
    logging.debug(f'Temp File: {temp_file} written to {temp_file.name}')

    # Send the temporary file as a payload into the BIG-IP AS3 endpoint
    url = f"https://{hostname}/mgmt/shared/appsvcs/declare"
    headers = {
        "Content-Type": "application/json"
    }
    response = bigip_post(username, password, url, headers, as3_declarations)
    logging.debug(f'AS3 Response: {response.text}')
    
    # Output the change report to a file
    json_output_file = open("as3_change_report.json", "w")
    json_output_file.write(json.dumps(response.json(), indent=4))
    json_output_file.close()
    
    # Complete Script
    logger.info("Script Complete")
    sys.exit(0)

# End