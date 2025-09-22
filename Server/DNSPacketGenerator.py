#!C:\Program Files\Python312\python.exe

# Add user-level site-packages path to sys.path for Scapy access
import sys
sys.path.append("C:\\Program Files\\Python312\\site-packages")

# import cgi module:
import cgi
import os
os.environ["ProgramFiles"] = 'C:\\Program Files'

from scapy.all import *
from scapy.all import IP

# output http header:
print('Content-type: text/html\n')

print('<html lang="en"><head><title>DNS Packet Generator</title></head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">')
print('<body style="text-align: center; margin-top: 50px;">')

theRequest = cgi.FieldStorage()
# get the required fields
destinationIP = theRequest.getfirst("destinationIP", "undefined")
dnsQuery = theRequest.getfirst("dnsQuery", "undefined")

try:
    if destinationIP == "undefined" or dnsQuery == "undefined":
        raise ValueError("Invalid inputs. Destination IP and DNS Query are required.")

    # Create a DNS query packet
    dns_query = IP(dst=destinationIP) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=dnsQuery)) # type: ignore

    # Send the packet and receive the response
    response = sr1(dns_query, timeout=2, verbose=0)

    if response:
        print('<h2 class="text-success">DNS Packet Generator</h2>')
        print(f'<p class="text-success">Successfully generated DNS Packet with the specified details. '
              f'Please check in the packet capture tool.</p>')
    else:
        print('<h2 class="text-danger">DNS Packet Generator</h2>')
        print(f'<p class="text-danger">Failed to generate DNS Packet. No response from the destination.</p>')

except Exception as e:
    print('<h2 class="text-danger">DNS Packet Generator</h2>')
    print(f'<p class="text-danger">Error: {str(e)}</p>')

print('</body></html>')
