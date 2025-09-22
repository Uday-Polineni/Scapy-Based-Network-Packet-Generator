#!C:\Program Files\Python312\python.exe

import sys
sys.path.append("C:\\Program Files\\Python312\\site-packages")
# Import necessary modules
import cgi
import os
os.environ["ProgramFiles"] = 'C:\\Program Files'

import scapy.all as scapy

# Output HTTP header
print("Content-type: text/html\n")
print('<html lang="en"><head><title>ARP Packet Generator</title></head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">')
print('<body style="text-align: center; margin-top: 50px;">')

# Capture form data
try:
    theRequest = cgi.FieldStorage()
    destinationIP = theRequest.getfirst("destinationIP", "undefined")
    destinationMAC = theRequest.getfirst("destinationMAC", "undefined")
    sourceIP = theRequest.getfirst("sourceIP", "undefined")

    if destinationIP == "undefined" or sourceIP == "undefined":
        raise ValueError("All fields (Destination IP, Destination MAC, Source IP) are required.")

    # Create an ARP request packet
    arp_packet = scapy.ARP(
        op=1,  # 1 for ARP request, 2 for ARP reply
        pdst=destinationIP,  # Destination IP address
        psrc=sourceIP  # Source IP address
    )

    # Send the ARP request packet
    scapy.send(arp_packet, verbose=False)  # Disable verbose to prevent unwanted output

    # Output success message
    print('<div class="container">')
    print('<h2 class="text-success">ARP Packet Generator</h2>')
    print(f'<p class="text-success">Successfully generated ARP Packet to {destinationIP} with MAC {destinationMAC}. '
          f'Please check in the packet capture tool.</p>')
    print('</div>')

except Exception as e:
    # Output error message
    print('<div class="container">')
    print('<h2 class="text-danger">ARP Packet Generator</h2>')
    print(f'<p class="text-danger">Error: {str(e)}</p>')
    print('</div>')

# Close HTML
print('</body></html>')