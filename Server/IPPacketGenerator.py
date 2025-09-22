#!C:\Program Files\Python312\python.exe

# Add user-level site-packages path to sys.path for Scapy access
import sys
sys.path.append("C:\\Program Files\\Python312\\site-packages")

# Import required modules
import cgi
import os
os.environ["ProgramFiles"] = 'C:\\Program Files'

import scapy.all as scapy
from scapy.all import IP, TCP, send, Raw

# Output HTTP header
print('Content-type: text/html\n')

# Start HTML content
print('<html lang="en"><head><title>IP Packet Generator</title></head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">')
print('<body style="text-align: center; margin-top: 50px;">')

# Retrieve CGI form inputs
theRequest = cgi.FieldStorage()
destinationIP = theRequest.getfirst("destinationIP", "undefined")
sourceIP = theRequest.getfirst("sourceIP", "undefined")
ttl = int(theRequest.getfirst("ttl", "64"))

try:
    if destinationIP == "undefined" or sourceIP == "undefined":
        raise ValueError("Both Source IP and Destination IP are required.")

    # Create an IP packet with Scapy
    payload = b"This is a test IP packet"
    raw_payload = Raw(load=payload)
    ip_packet = IP(src=sourceIP, dst=destinationIP, ttl = ttl)

    # Create a TCP packet and add it as a payload to the IP packet
    tcp_packet = TCP(sport=12345, dport=80)
    ip_packet /= tcp_packet/ raw_payload

    # Send the packet
    send(ip_packet, verbose=0)

    # Display success message
    print('<h2 class="text-success">IP Packet Generator</h2>')
    print(f'<p class="text-success">Successfully generated IP Packet with the specified details. '
          f'Please check in the packet capture tool.</p>')

except Exception as e:
    # Handle any errors
    print('<h2 class="text-danger">IP Packet Generator</h2>')
    print(f'<p class="text-danger">Failed to generate IP Packet. Error: {str(e)}</p>')

# End HTML content
print('</body></html>')
