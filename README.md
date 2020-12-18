# JSONmap

Convert XML formatted Nmap scan output to JSON.

## Installation

Pipenv:

```
$ git clone https://github.com/f0xtek/jsonmap.git
$ cd jsonmap
$ pipenv install
$ pipenv shell
```

Virtualenv:

```
$ git clone https://github.com/f0xtek/jsonmap.git
$ cd jsonmap
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

```
usage: jsonmap.py [-h] [--json-output-file JSON_FILE] xmlfile
positional arguments:
  xmlfile               The path to the XML formatted Nmap file

optional arguments:
  -h, --help            show this help message and exit
  --json-output-file JSON_FILE
                        The path to the saved JSON file. Default: scan.json
```

```
$ sudo nmap -sS -p 80 -oX scan.xml scanme.nmap.org
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-18 21:50 GMT
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.15s latency).

PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.39 seconds

$ cat scan.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE nmaprun>
<?xml-stylesheet href="file:///usr/local/bin/../share/nmap/nmap.xsl" type="text/xsl"?>
<!-- Nmap 7.91 scan initiated Fri Dec 18 21:50:05 2020 as: nmap -sS -p 80 -oX scan.xml scanme.nmap.org -->
<nmaprun scanner="nmap" args="nmap -sS -p 80 -oX scan.xml scanme.nmap.org" start="1608328205" startstr="Fri Dec 18 21:50:05 2020" version="7.91" xmloutputversion="1.05">
<scaninfo type="syn" protocol="tcp" numservices="1" services="80"/>
<verbose level="0"/>
<debugging level="0"/>
<hosthint><status state="up" reason="unknown-response" reason_ttl="0"/>
<address addr="45.33.32.156" addrtype="ipv4"/>
<hostnames>
<hostname name="scanme.nmap.org" type="user"/>
</hostnames>
</hosthint>
<host starttime="1608328206" endtime="1608328206"><status state="up" reason="echo-reply" reason_ttl="53"/>
<address addr="45.33.32.156" addrtype="ipv4"/>
<hostnames>
<hostname name="scanme.nmap.org" type="user"/>
<hostname name="scanme.nmap.org" type="PTR"/>
</hostnames>
<ports><port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="52"/><service name="http" method="table" conf="3"/></port>
</ports>
<times srtt="153444" rttvar="115128" to="613956"/>
</host>
<runstats><finished time="1608328206" timestr="Fri Dec 18 21:50:06 2020" summary="Nmap done at Fri Dec 18 21:50:06 2020; 1 IP address (1 host up) scanned in 0.39 seconds" elapsed="0.39" exit="success"/><hosts up="1" down="0" total="1"/>
</runstats>
</nmaprun>

$ python3 jsonmap.py scan.xml
Complete! JSON output saved to scan.json

$ cat scan.json
{
    "nmaprun": {
        "@args": "nmap -sS -p 80 -oX scan.xml scanme.nmap.org",
        "@scanner": "nmap",
        "@start": "1608328205",
        "@startstr": "Fri Dec 18 21:50:05 2020",
        "@version": "7.91",
        "@xmloutputversion": "1.05",
        "debugging": {
            "@level": "0"
        },
        "host": {
            "@endtime": "1608328206",
            "@starttime": "1608328206",
            "address": {
                "@addr": "45.33.32.156",
                "@addrtype": "ipv4"
            },
            "hostnames": {
                "hostname": [
                    {
                        "@name": "scanme.nmap.org",
                        "@type": "user"
                    },
                    {
                        "@name": "scanme.nmap.org",
                        "@type": "PTR"
                    }
                ]
            },
            "ports": {
                "port": {
                    "@portid": "80",
                    "@protocol": "tcp",
                    "service": {
                        "@conf": "3",
                        "@method": "table",
                        "@name": "http"
                    },
                    "state": {
                        "@reason": "syn-ack",
                        "@reason_ttl": "52",
                        "@state": "open"
                    }
                }
            },
            "status": {
                "@reason": "echo-reply",
                "@reason_ttl": "53",
                "@state": "up"
            },
            "times": {
                "@rttvar": "115128",
                "@srtt": "153444",
                "@to": "613956"
            }
        },
        "hosthint": {
            "address": {
                "@addr": "45.33.32.156",
                "@addrtype": "ipv4"
            },
            "hostnames": {
                "hostname": {
                    "@name": "scanme.nmap.org",
                    "@type": "user"
                }
            },
            "status": {
                "@reason": "unknown-response",
                "@reason_ttl": "0",
                "@state": "up"
            }
        },
        "runstats": {
            "finished": {
                "@elapsed": "0.39",
                "@exit": "success",
                "@summary": "Nmap done at Fri Dec 18 21:50:06 2020; 1 IP address (1 host up) scanned in 0.39 seconds",
                "@time": "1608328206",
                "@timestr": "Fri Dec 18 21:50:06 2020"
            },
            "hosts": {
                "@down": "0",
                "@total": "1",
                "@up": "1"
            }
        },
        "scaninfo": {
            "@numservices": "1",
            "@protocol": "tcp",
            "@services": "80",
            "@type": "syn"
        },
        "verbose": {
            "@level": "0"
        }
    }
}
```

