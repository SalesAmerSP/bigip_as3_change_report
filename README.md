# AS3 Change Report

This script generates a report of changes made to an AS3 configuration on a BIG-IP.

## Usage

1. Clone the repository
2. Install the required Python packages with `pip install -r requirements.txt`
3. Run the script with `python as3_change_report.py`

## Options

* `-h, --help` - Show this help message and exit
* `-user USER, --username USER` - BIG-IP username
* `-pass PASSWORD, --password PASSWORD` - BIG-IP password
* `-host HOSTNAME, --hostname HOSTNAME` - BIG-IP hostname or IP address

## Output

The script will output a report in Markdown format to the console. The report will include the following information:

* The AS3 declaration(s) that were changed
* The specific lines that were changed
* The old and new values of the changed lines

## Example Output

```json
{
    "results": [
        {
            "code": 200,
            "message": "success",
            "dryRun": true,
            "lineCount": 27,
            "changes": [
                {
                    "kind": "D",
                    "path": [
                        "/security/site16_boston/Pool",
                        "properties",
                        "members",
                        "/Common/10.1.20.110:80",
                        "metadata"
                    ],
                    "lhs": {
                        "value": "declaration",
                        "persist": "true"
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm pool",
                    "lhsCommand": "ltm pool",
                    "rhsCommand": "ltm pool"
                },
                {
                    "kind": "D",
                    "path": [
                        "/security/site16_boston/Pool",
                        "properties",
                        "members",
                        "/Common/10.1.20.111:80",
                        "metadata"
                    ],
                    "lhs": {
                        "value": "declaration",
                        "persist": "true"
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm pool",
                    "lhsCommand": "ltm pool",
                    "rhsCommand": "ltm pool"
                },
                {
                    "kind": "N",
                    "path": [
                        "/security/fqdn/airports.example.com a",
                        "properties",
                        "description"
                    ],
                    "rhs": "\"dnsMain\"",
                    "tags": [
                        "tmsh"
                    ],
                    "command": "gtm wideip a",
                    "lhsCommand": "gtm wideip a",
                    "rhsCommand": "gtm wideip a"
                },
                {
                    "kind": "D",
                    "path": [
                        "/Common/10.1.20.110",
                        "properties",
                        "monitor",
                        "/Common/http"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "N",
                    "path": [
                        "/Common/10.1.20.110",
                        "properties",
                        "monitor",
                        "default"
                    ],
                    "rhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "D",
                    "path": [
                        "/Common/10.1.20.111",
                        "properties",
                        "monitor",
                        "/Common/http"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "N",
                    "path": [
                        "/Common/10.1.20.111",
                        "properties",
                        "monitor",
                        "default"
                    ],
                    "rhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                }
            ],
            "host": "localhost",
            "tenant": "security",
            "runTime": 1661,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "success",
            "dryRun": true,
            "lineCount": 19,
            "changes": [
                {
                    "kind": "D",
                    "path": [
                        "/taxes/site17access/Pool",
                        "properties",
                        "members",
                        "/Common/10.1.20.120:80",
                        "metadata"
                    ],
                    "lhs": {
                        "value": "declaration",
                        "persist": "true"
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm pool",
                    "lhsCommand": "ltm pool",
                    "rhsCommand": "ltm pool"
                },
                {
                    "kind": "D",
                    "path": [
                        "/taxes/site17access/TLS_Server",
                        "properties",
                        "cert-extension-includes",
                        "basic-constraints"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm profile client-ssl",
                    "lhsCommand": "ltm profile client-ssl",
                    "rhsCommand": "ltm profile client-ssl"
                },
                {
                    "kind": "D",
                    "path": [
                        "/taxes/site17access/TLS_Server",
                        "properties",
                        "cert-extension-includes",
                        "subject-alternative-name"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm profile client-ssl",
                    "lhsCommand": "ltm profile client-ssl",
                    "rhsCommand": "ltm profile client-ssl"
                },
                {
                    "kind": "D",
                    "path": [
                        "/taxes/site17access/TLS_Server",
                        "properties",
                        "options",
                        "no-dtlsv1.2"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm profile client-ssl",
                    "lhsCommand": "ltm profile client-ssl",
                    "rhsCommand": "ltm profile client-ssl"
                }
            ],
            "host": "localhost",
            "tenant": "taxes",
            "runTime": 1528,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "success",
            "dryRun": true,
            "lineCount": 30,
            "changes": [
                {
                    "kind": "D",
                    "path": [
                        "/legacy/app1/Pool",
                        "properties",
                        "members",
                        "/Common/10.1.20.115:80",
                        "metadata"
                    ],
                    "lhs": {
                        "value": "declaration",
                        "persist": "true"
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm pool",
                    "lhsCommand": "ltm pool",
                    "rhsCommand": "ltm pool"
                },
                {
                    "kind": "D",
                    "path": [
                        "/legacy/app1/Pool",
                        "properties",
                        "members",
                        "/Common/10.1.20.116:80",
                        "metadata"
                    ],
                    "lhs": {
                        "value": "declaration",
                        "persist": "true"
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm pool",
                    "lhsCommand": "ltm pool",
                    "rhsCommand": "ltm pool"
                },
                {
                    "kind": "D",
                    "path": [
                        "/legacy/app1/Pool",
                        "properties",
                        "members",
                        "/Common/10.1.20.117:80",
                        "metadata"
                    ],
                    "lhs": {
                        "value": "declaration",
                        "persist": "true"
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm pool",
                    "lhsCommand": "ltm pool",
                    "rhsCommand": "ltm pool"
                },
                {
                    "kind": "D",
                    "path": [
                        "/legacy/app1/vip134"
                    ],
                    "lhs": {
                        "command": "ltm virtual",
                        "properties": {
                            "enabled": true,
                            "address-status": "yes",
                            "auto-lasthop": "default",
                            "connection-limit": 0,
                            "rate-limit": "disabled",
                            "description": "\"app1\"",
                            "destination": "/legacy/10.1.10.134:80",
                            "ip-protocol": "tcp",
                            "last-hop-pool": "none",
                            "mask": "255.255.255.255",
                            "mirror": "disabled",
                            "persist": {
                                "/Common/cookie": {
                                    "default": "yes"
                                }
                            },
                            "pool": "/legacy/app1/Pool",
                            "policies": {},
                            "profiles": {
                                "/Common/f5-tcp-progressive": {
                                    "context": "all"
                                },
                                "/Common/http": {
                                    "context": "all"
                                }
                            },
                            "service-down-immediate-action": "none",
                            "source": "0.0.0.0/0",
                            "source-address-translation": {
                                "type": "automap"
                            },
                            "rules": {},
                            "security-log-profiles": {},
                            "source-port": "preserve",
                            "translate-address": "enabled",
                            "translate-port": "enabled",
                            "nat64": "disabled",
                            "vlans": {},
                            "vlans-disabled": " ",
                            "metadata": {},
                            "clone-pools": {},
                            "throughput-capacity": "infinite"
                        },
                        "ignore": []
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm virtual",
                    "lhsCommand": "ltm virtual",
                    "rhsCommand": ""
                },
                {
                    "kind": "E",
                    "path": [
                        "/legacy/10.1.10.134",
                        "properties",
                        "traffic-group"
                    ],
                    "lhs": "/Common/traffic-group-1",
                    "rhs": "default",
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm virtual-address",
                    "lhsCommand": "ltm virtual-address",
                    "rhsCommand": "ltm virtual-address"
                },
                {
                    "kind": "D",
                    "path": [
                        "/Common/10.1.20.115",
                        "properties",
                        "monitor",
                        "/Common/http"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "N",
                    "path": [
                        "/Common/10.1.20.115",
                        "properties",
                        "monitor",
                        "default"
                    ],
                    "rhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "D",
                    "path": [
                        "/Common/10.1.20.116",
                        "properties",
                        "monitor",
                        "/Common/http"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "N",
                    "path": [
                        "/Common/10.1.20.116",
                        "properties",
                        "monitor",
                        "default"
                    ],
                    "rhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "D",
                    "path": [
                        "/Common/10.1.20.117",
                        "properties",
                        "monitor",
                        "/Common/http"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "N",
                    "path": [
                        "/Common/10.1.20.117",
                        "properties",
                        "monitor",
                        "default"
                    ],
                    "rhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm node",
                    "lhsCommand": "ltm node",
                    "rhsCommand": "ltm node"
                },
                {
                    "kind": "N",
                    "path": [
                        "/legacy/app1/serviceMain"
                    ],
                    "rhs": {
                        "command": "ltm virtual",
                        "properties": {
                            "enabled": "",
                            "address-status": "yes",
                            "auto-lasthop": "default",
                            "connection-limit": 0,
                            "rate-limit": "disabled",
                            "description": "\"app1\"",
                            "destination": "/legacy/10.1.10.134:80",
                            "ip-protocol": "tcp",
                            "last-hop-pool": "none",
                            "mask": "255.255.255.255",
                            "mirror": "disabled",
                            "persist": {
                                "/Common/cookie": {
                                    "default": "yes"
                                }
                            },
                            "pool": "/legacy/app1/Pool",
                            "policies": {},
                            "profiles": {
                                "/Common/http": {
                                    "context": "all"
                                },
                                "/legacy/app1/statsProfileHttp": {
                                    "context": "all"
                                },
                                "/legacy/app1/statsProfileTcp": {
                                    "context": "all"
                                },
                                "/Common/f5-tcp-progressive": {
                                    "context": "all"
                                }
                            },
                            "service-down-immediate-action": "none",
                            "source": "0.0.0.0/0",
                            "source-address-translation": {
                                "type": "automap"
                            },
                            "rules": {},
                            "security-log-profiles": {},
                            "source-port": "preserve",
                            "translate-address": "enabled",
                            "translate-port": "enabled",
                            "nat64": "disabled",
                            "vlans": {},
                            "vlans-disabled": " ",
                            "metadata": {},
                            "clone-pools": {},
                            "throughput-capacity": "infinite"
                        },
                        "ignore": []
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm virtual",
                    "lhsCommand": "",
                    "rhsCommand": "ltm virtual"
                }
            ],
            "host": "localhost",
            "tenant": "legacy",
            "runTime": 1316,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "Task2",
            "runTime": 1433,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "RetailShopApps",
            "runTime": 1331,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "success",
            "dryRun": true,
            "lineCount": 18,
            "changes": [
                {
                    "kind": "D",
                    "path": [
                        "/Returns/BurgerRefunds/serviceMain",
                        "properties",
                        "profiles",
                        "/Common/serverssl-secure"
                    ],
                    "lhs": {
                        "context": "serverside"
                    },
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm virtual",
                    "lhsCommand": "ltm virtual",
                    "rhsCommand": "ltm virtual"
                },
                {
                    "kind": "D",
                    "path": [
                        "/Returns/BurgerRefunds/serviceMain",
                        "properties",
                        "vlans",
                        "/Common/external"
                    ],
                    "lhs": {},
                    "tags": [
                        "tmsh"
                    ],
                    "command": "ltm virtual",
                    "lhsCommand": "ltm virtual",
                    "rhsCommand": "ltm virtual"
                }
            ],
            "host": "localhost",
            "tenant": "Returns",
            "runTime": 1522,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "GrandSlamRetirement",
            "runTime": 1492,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "Robotcontrollers",
            "runTime": 1471,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "TRexPen",
            "runTime": 1486,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "AskMeAgain",
            "runTime": 1526,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "Nestle",
            "runTime": 849,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "Recipes",
            "runTime": 1348,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "TomBradyApp",
            "runTime": 1358,
            "declarationId": "isc-lab"
        },
        {
            "code": 200,
            "message": "no change",
            "host": "localhost",
            "tenant": "TractorSales",
            "runTime": 807,
            "declarationId": "isc-lab"
        }
    ],
    "declaration": {
        "security": {
            "fqdn": {
                "class": "Application",
                "template": "generic",
                "dnsMain": {
                    "pools": [
                        {
                            "use": "/security/fqdn/GSLB_Pool1"
                        },
                        {
                            "use": "/security/fqdn/GSLB_Pool2"
                        }
                    ],
                    "enabled": true,
                    "domainName": "airports.example.com",
                    "class": "GSLB_Domain",
                    "resourceRecordType": "A"
                },
                "GSLB_Pool1": {
                    "members": [
                        {
                            "server": {
                                "bigip": "/Common/BOS-vBIGIP01.termmarc.com"
                            },
                            "virtualServer": "/security/site16_boston/serviceMain"
                        },
                        {
                            "server": {
                                "bigip": "/Common/BOS-vBIGIP02.termmarc.com"
                            },
                            "virtualServer": "/security/site16_boston/serviceMain"
                        }
                    ],
                    "monitors": [
                        {
                            "bigip": "/Common/tcp"
                        }
                    ],
                    "lbModeFallback": "return-to-dns",
                    "lbModeAlternate": "round-robin",
                    "lbModePreferred": "round-robin",
                    "class": "GSLB_Pool",
                    "resourceRecordType": "A"
                },
                "GSLB_Pool2": {
                    "members": [
                        {
                            "server": {
                                "bigip": "/Common/SEA-vBIGIP01.termmarc.com"
                            },
                            "virtualServer": "/security/site18_seattle/serviceMain"
                        }
                    ],
                    "monitors": [
                        {
                            "bigip": "/Common/tcp"
                        }
                    ],
                    "lbModeFallback": "return-to-dns",
                    "lbModeAlternate": "round-robin",
                    "lbModePreferred": "round-robin",
                    "class": "GSLB_Pool",
                    "resourceRecordType": "A"
                },
                "remark": "update"
            },
            "class": "Tenant",
            "site16_boston": {
                "Pool": {
                    "class": "Pool",
                    "members": [
                        {
                            "monitors": [
                                "http"
                            ],
                            "adminState": "enable",
                            "shareNodes": true,
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.110"
                            ]
                        },
                        {
                            "monitors": [
                                "http"
                            ],
                            "adminState": "enable",
                            "shareNodes": true,
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.111"
                            ]
                        }
                    ],
                    "monitors": [
                        "http"
                    ]
                },
                "class": "Application",
                "template": "http",
                "serviceMain": {
                    "pool": "/security/site16_boston/Pool",
                    "class": "Service_HTTP",
                    "enable": true,
                    "profileHTTP": {
                        "use": "/security/site16_boston/HTTP_Profile"
                    },
                    "virtualPort": 80,
                    "profileAnalytics": {
                        "use": "/security/site16_boston/Analytics_Profile"
                    },
                    "virtualAddresses": [
                        "10.1.10.116"
                    ]
                },
                "HTTP_Profile": {
                    "class": "HTTP_Profile",
                    "fallbackRedirect": "https://www.example.com/403",
                    "fallbackStatusCodes": [
                        403
                    ]
                },
                "Analytics_Profile": {
                    "class": "Analytics_Profile",
                    "collectIp": true,
                    "collectGeo": true,
                    "collectUrl": true,
                    "captureFilter": {
                        "requestCapturedParts": "all",
                        "responseCapturedParts": "all"
                    },
                    "collectMethod": true,
                    "collectUserAgent": true,
                    "collectOsAndBrowser": true,
                    "collectPageLoadTime": true,
                    "collectResponseCode": true,
                    "collectClientSideStatistics": true,
                    "capturedTrafficInternalLogging": true
                }
            }
        },
        "taxes": {
            "class": "Tenant",
            "site17access": {
                "class": "Application",
                "template": "https",
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualPort": 443,
                    "profileAnalytics": {
                        "use": "/taxes/site17access/Analytics_Profile"
                    },
                    "policyIAM": {
                        "bigip": "/Common/simpleHttpsAccess"
                    },
                    "serverTLS": "/taxes/site17access/TLS_Server",
                    "virtualAddresses": [
                        "10.1.10.117"
                    ],
                    "pool": "/taxes/site17access/Pool",
                    "enable": true
                },
                "Analytics_Profile": {
                    "class": "Analytics_Profile",
                    "collectUserAgent": true,
                    "collectClientSideStatistics": true,
                    "collectGeo": true,
                    "collectUrl": true,
                    "collectPageLoadTime": true,
                    "collectOsAndBrowser": true,
                    "collectMethod": true,
                    "collectResponseCode": true
                },
                "TLS_Server": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/taxes/site17access/CertificateTax"
                        }
                    ]
                },
                "CertificateTax": {
                    "certificate": "-----BEGIN CERTIFICATE-----\nMIID7TCCAtWgAwIBAgIJAJH4sMVzl1dMMA0GCSqGSIb3DQEBCwUAMIGMMQswCQYDVQQGEwJVUzETMBEGA1UECAwKV2FzaGluZ3RvbjEQMA4GA1UEBwwHU2VhdHRsZTELMAkGA1UECgwCRjUxDTALBgNVBAsMBFRlc3QxEzARBgNVBAMMCnRscy1zZXJ2ZXIxJTAjBgkqhkiG9w0BCQEWFnNvbWVib2R5QHNvbWV3aGVyZS5jb20wHhcNMTgwMjI4MTkwNzMyWhcNMjgwMjI2MTkwNzMyWjCBjDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24xEDAOBgNVBAcMB1NlYXR0bGUxCzAJBgNVBAoMAkY1MQ0wCwYDVQQLDARUZXN0MRMwEQYDVQQDDAp0bHMtc2VydmVyMSUwIwYJKoZIhvcNAQkBFhZzb21lYm9keUBzb21ld2hlcmUuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwEMNPATg7Vz3jqInIVf2jnOi/9/HYIr8xZYgU0YHHFEiquQ6nYfX4mwezZ6zo9GJom7gHiQ3FNy3fN+RatatZmBmuyvJ+z/uZ6pbKmsuJLPLT89olO9JxMtb4a83oHDz3f6rcc2j8KwTr4lUDc452jLF4ZQ55O17s2tYMg4XW2G5DqUGzp1UKiClaDvpN23ZVOlnqDVpIlnVvJ1mz12AzFPny8xD1lhILv78yMltimdaWhyCLcFom0DbloRvYmowjGLHqLTAZ40jI3YUdw39LEqTXgfDF3DnOgZCIdRpouD9cVZBoQroXpVVfWG7sfzKLqWaAEHhjbhdK5l/p3mT7wIDAQABo1AwTjAdBgNVHQ4EFgQUBlCKIZ0+9DQ4ylW86qsyXoW8KjkwHwYDVR0jBBgwFoAUBlCKIZ0+9DQ4ylW86qsyXoW8KjkwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAuiE5MocznYDc+JHvEgSaiK9fyRBl/bitKTkiOtxWjEFpF5nH6QddV0pqQziXLb6iSbTBwlDJr9Bwzng8moOYbsD7hP2/mCKJj8o/lsRaPAk+abekWXRqYFNucct/ipBG3s+N2PH+MEpy3ioPH1OBuam6UomjE+mqoP09FrQha1hHEbabt4nN11l8fM5GW+0zRU0SwLFvnR58zUSlTMwczSPA0eUrhEU4AGPD/KN8d1fYnCcWqPF5ePcU11k7SNFl5PZQsgXv9cOc2Vq+qc/NmDBO0rQyKEAPDxbM8CK212G1M+ENTqmuePnr+mNope3AhEsqfH8IOPEoT7fIwmpqLw==\n-----END CERTIFICATE-----",
                    "privateKey": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAQw08BODtXPeOoichV/aOc6L/38dgivzFliBTRgccUSKq5Dqdh9fibB7NnrOj0YmibuAeJDcU3Ld835Fq1q1mYGa7K8n7P+5nqlsqay4ks8tPz2iU70nEy1vhrzegcPPd/qtxzaPwrBOviVQNzjnaMsXhlDnk7Xuza1gyDhdbYbkOpQbOnVQqIKVoO+k3bdlU6WeoNWkiWdW8nWbPXYDMU+fLzEPWWEgu/vzIyW2KZ1paHIItwWibQNuWhG9iajCMYseotMBnjSMjdhR3Df0sSpNeB8MXcOc6BkIh1Gmi4P1xVkGhCuhelVV9Ybux/MoupZoAQeGNuF0rmX+neZPvAgMBAAECggEAHm3eV9v7z4WRxtjiMZRO+Q/TQgUkdKK6y/jtR9DDClfLEVoK7ujTocnz/B48l1ZwHq3Gue6IazxdrB1kUhEFI7lpOQF+t83QCUc8o5OQG437RTfx+PSAa+21rpwBRVrrNfz7HIlsA4jwmq01CPRVUrQLfp7rpNBzbhu0u0Ngrf0ccOwXZkEUVvZ55WaPY1YADI9PBExQ2k04LvHJjoz/tJH3nsQLA/+90UXqy8ctUSMJ8Ko3crxJhnIO91BtCugkgS+U+pTEnvdAebE4pd7J5e6qqEyCu9F3DC5R6hH+K8bAj76VGwjxOr9a90o/js92HoCVAlQMHnW06Uk2RdIRmQKBgQD0uQPlA2PLBysWA+IQvd8oBfZuXWQjUZPBU9MK5k7bfuRbNeCA2kbTt1MVf15lv7vcwrwAbYo+Ur+L9CVL3lA8d/lQkz51r1ISChTPUiAMyU+CDDnXjQ1Gik/nC399AeluxS62Tur8hGPAb4rkVEyU60hPFVZTjmv13n81EjUoNwKBgQDJHyiPIgbwI+OoZYMUcGQrsr+yp1MdJrjpuFloc7+sdUpsvelyc146h3+TSAlhDce2BMH68kMUWUYHxHIooQjtDMu9S9b8VAF52F3E9osyjMzsywTri3hgBPy69j/Kr623gbZpbm6lYmdxRp/FKZyWtAbPts45GH1GPdv+9fUmCQKBgQCX7CfDy1fvWXLhBuYXuJfJs/HpT+bzmhgdA5nXgWRhFSRUj1zhASDJHFzi0qBakC3i/a1Soq4YxKwPCTECKXAsKdrHr7Etw/oyIroKfpRQ+8R1GnvqGbGtIf46k8PAaihtUNIP8Wwl+VYnx9c0qjSkmm/YUIm384mIKGlWHAiN/wKBgDV5bF5KLNASqsguXWDE1U1tFF0a8hVRI185HcSQ6gifku9Au14r4ITtW/U79QpyEISL1Uu0uDMj3WPZToUQ8/+bJFyrWnjymQXdimkBKFeDakUXYbKC/bmB+fR33tQ0S5r8CRUVQKQGevx6S6avfqvvJ9R4hXJW2ZAgiGrM2KaJAoGAPXuy4KHRmeeBZj8AT/shQ0VrDWIMNYDrhx0T6q9hVMahBS0SJaKDlQn6cSF7TX5N9PFAbwzcrvRKKfNjQVSZpQdR4l42f+N/5q0c1wihf43k9FgeYQ8jHGJ05uJnh3nj/O57FKgjlZ4FZVQdR8ieHN+rT4sHWj36a/FLHa6p1oo=\n-----END PRIVATE KEY-----",
                    "class": "Certificate"
                },
                "Pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "adminState": "enable",
                            "serverAddresses": [
                                "10.1.20.120"
                            ],
                            "shareNodes": true
                        }
                    ]
                }
            }
        },
        "legacy": {
            "class": "Tenant",
            "app1": {
                "class": "Application",
                "template": "http",
                "serviceMain": {
                    "virtualPort": 80,
                    "virtualAddresses": [
                        "10.1.10.134"
                    ],
                    "profileAnalytics": {
                        "use": "statsProfileHttp"
                    },
                    "profileAnalyticsTcp": {
                        "use": "statsProfileTcp"
                    },
                    "pool": "Pool",
                    "class": "Service_HTTP"
                },
                "statsProfileHttp": {
                    "class": "Analytics_Profile",
                    "collectUserAgent": true,
                    "collectClientSideStatistics": true,
                    "collectGeo": true,
                    "collectUrl": true,
                    "collectPageLoadTime": true,
                    "collectOsAndBrowser": true,
                    "collectMethod": true,
                    "collectResponseCode": true,
                    "capturedTrafficInternalLogging": true,
                    "captureFilter": {
                        "requestCapturedParts": "all",
                        "responseCapturedParts": "all"
                    }
                },
                "statsProfileTcp": {
                    "class": "Analytics_TCP_Profile",
                    "collectCity": true,
                    "collectRegion": true,
                    "collectCountry": true,
                    "collectPostCode": true,
                    "collectContinent": true,
                    "collectedByClientSide": true,
                    "collectedByServerSide": true,
                    "collectNexthop": true,
                    "collectRemoteHostIp": true,
                    "collectRemoteHostSubnet": true
                },
                "Pool": {
                    "members": [
                        {
                            "serverAddresses": [
                                "10.1.20.115",
                                "10.1.20.116",
                                "10.1.20.117"
                            ],
                            "servicePort": 80,
                            "monitors": [
                                "http"
                            ],
                            "adminState": "enable",
                            "shareNodes": true
                        }
                    ],
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ]
                }
            }
        },
        "Task2": {
            "class": "Tenant",
            "MyWebApp2https": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.1.10.113"
                    ],
                    "pool": "/Task2/MyWebApp2https/web_pool",
                    "profileAnalytics": {
                        "use": "/Task2/MyWebApp2https/statsProfile"
                    },
                    "serverTLS": "/Task2/MyWebApp2https/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/Task2/MyWebApp2https/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "RetailShopApps": {
            "class": "Tenant",
            "Gizmos": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.13.24.12"
                    ],
                    "pool": "/RetailShopApps/Gizmos/web_pool",
                    "profileAnalytics": {
                        "use": "/RetailShopApps/Gizmos/statsProfile"
                    },
                    "serverTLS": "/RetailShopApps/Gizmos/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/RetailShopApps/Gizmos/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "Returns": {
            "class": "Tenant",
            "BurgerRefunds": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.13.24.123"
                    ],
                    "pool": "/Returns/BurgerRefunds/web_pool",
                    "profileAnalytics": {
                        "use": "/Returns/BurgerRefunds/statsProfile"
                    },
                    "serverTLS": "/Returns/BurgerRefunds/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/Returns/BurgerRefunds/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "GrandSlamRetirement": {
            "class": "Tenant",
            "CheapMealsApp": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.13.23.23"
                    ],
                    "pool": "/GrandSlamRetirement/CheapMealsApp/web_pool",
                    "profileAnalytics": {
                        "use": "/GrandSlamRetirement/CheapMealsApp/statsProfile"
                    },
                    "serverTLS": "/GrandSlamRetirement/CheapMealsApp/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/GrandSlamRetirement/CheapMealsApp/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "Robotcontrollers": {
            "class": "Tenant",
            "WargamesAppController": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.241.23.23"
                    ],
                    "pool": "/Robotcontrollers/WargamesAppController/web_pool",
                    "profileAnalytics": {
                        "use": "/Robotcontrollers/WargamesAppController/statsProfile"
                    },
                    "serverTLS": "/Robotcontrollers/WargamesAppController/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/Robotcontrollers/WargamesAppController/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "TRexPen": {
            "class": "Tenant",
            "GateControls": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.11.32.23"
                    ],
                    "pool": "/TRexPen/GateControls/web_pool",
                    "profileAnalytics": {
                        "use": "/TRexPen/GateControls/statsProfile"
                    },
                    "serverTLS": "/TRexPen/GateControls/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/TRexPen/GateControls/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "AskMeAgain": {
            "class": "Tenant",
            "IllKnockYouDown": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.113.32.23"
                    ],
                    "pool": "/AskMeAgain/IllKnockYouDown/web_pool",
                    "profileAnalytics": {
                        "use": "/AskMeAgain/IllKnockYouDown/statsProfile"
                    },
                    "serverTLS": "/AskMeAgain/IllKnockYouDown/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/AskMeAgain/IllKnockYouDown/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "Nestle": {
            "class": "Tenant",
            "CrunchBarsApp": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.113.32.123"
                    ],
                    "pool": "/Nestle/CrunchBarsApp/web_pool",
                    "profileAnalytics": {
                        "use": "/Nestle/CrunchBarsApp/statsProfile"
                    },
                    "serverTLS": "/Nestle/CrunchBarsApp/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/Nestle/CrunchBarsApp/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "Recipes": {
            "class": "Tenant",
            "RetailShopApp": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.213.25.123"
                    ],
                    "pool": "/Recipes/RetailShopApp/web_pool",
                    "profileAnalytics": {
                        "use": "/Recipes/RetailShopApp/statsProfile"
                    },
                    "serverTLS": "/Recipes/RetailShopApp/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/Recipes/RetailShopApp/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "TomBradyApp": {
            "class": "Tenant",
            "DivorceRecords": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.213.215.123"
                    ],
                    "pool": "/TomBradyApp/DivorceRecords/web_pool",
                    "profileAnalytics": {
                        "use": "/TomBradyApp/DivorceRecords/statsProfile"
                    },
                    "serverTLS": "/TomBradyApp/DivorceRecords/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/TomBradyApp/DivorceRecords/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "TractorSales": {
            "class": "Tenant",
            "SalesApp": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.13.15.123"
                    ],
                    "pool": "/TractorSales/SalesApp/web_pool",
                    "profileAnalytics": {
                        "use": "/TractorSales/SalesApp/statsProfile"
                    },
                    "serverTLS": "/TractorSales/SalesApp/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/TractorSales/SalesApp/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            },
            "ServiceApp": {
                "class": "Application",
                "template": "https",
                "statsProfile": {
                    "class": "Analytics_Profile",
                    "collectClientSideStatistics": true,
                    "collectOsAndBrowser": false,
                    "collectMethod": false
                },
                "serviceMain": {
                    "class": "Service_HTTPS",
                    "virtualAddresses": [
                        "10.99.11.123"
                    ],
                    "pool": "/TractorSales/ServiceApp/web_pool",
                    "profileAnalytics": {
                        "use": "/TractorSales/ServiceApp/statsProfile"
                    },
                    "serverTLS": "/TractorSales/ServiceApp/webtls"
                },
                "web_pool": {
                    "class": "Pool",
                    "monitors": [
                        "http"
                    ],
                    "members": [
                        {
                            "servicePort": 80,
                            "serverAddresses": [
                                "10.1.20.112",
                                "10.1.20.113"
                            ],
                            "shareNodes": true
                        }
                    ]
                },
                "webtls": {
                    "class": "TLS_Server",
                    "certificates": [
                        {
                            "certificate": "/TractorSales/ServiceApp/webcert"
                        }
                    ]
                },
                "webcert": {
                    "class": "Certificate",
                    "certificate": {
                        "bigip": "/Common/default.crt"
                    },
                    "privateKey": {
                        "bigip": "/Common/default.key"
                    }
                }
            }
        },
        "class": "ADC",
        "schemaVersion": "3.42.0",
        "id": "isc-lab",
        "label": "Task2",
        "remark": "Task 2 - HTTPS Application Service",
        "updateMode": "selective",
        "controls": {
            "class": "Controls",
            "userAgent": "BIG-IQ/8.4 Configured by API",
            "archiveTimestamp": "2025-06-10T01:26:31.579Z",
            "dryRun": true,
            "logLevel": "debug"
        },
        "$schema": "https://raw.githubusercontent.com/F5Networks/f5-appsvcs-extension/refs/heads/main/schema/3.42.0/as3-schema.json"
    },
    "dryRun": true
}
```