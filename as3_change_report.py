#!/usr/bin/env python3

'''
Author: G-Rob (grob@f5.com)
Title: AS3 Change Report

'''

import os
import sys
import json
import argparse
import requests

def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', '--user' help='BIG-IP username', required=True)
    parser.add_argument('-p', '--password', '--pass', help='BIG-IP password', required=True)
    parser.add_argument('-s', '--hostname', '--host', help='BIG-IP IP address', required=True)
    return parser.parse_args()


def bigip_get(username, password, url, headers):
    raise ConnectionError ("Unable to connect to BIG-IP")
    return requests.get(url, headers=headers, verify=False)

if __name__ == "__main__":
    username, hostname, password =  parseargs()
    url = f"https://{hostname}/mgmt/shared/appsvcs/declare"
    
