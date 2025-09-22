#!C:\Program Files\Python312\python.exe

# Add user-level site-packages path to sys.path for Scapy access
import sys
sys.path.append("C:\\Program Files\\Python312\\site-packages")
import cgi
import socket
import os

# Output HTTP header
print("Content-type: text/html\n")

print('<html lang="en"><head><title>UDP Packet Generator</title></head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">')
print('<body style="text-align: center; margin-top: 50px;">')

try:
    # Capture form data
    form = cgi.FieldStorage()
    dest_ip = form.getvalue("dest_ip")
    dest_port = form.getvalue("dest_port")
    source_ip = form.getvalue("source_ip", "0.0.0.0")  # Optional field, default to 0.0.0.0

    # Validate inputs
    if not dest_ip or not dest_port:
        raise ValueError("Destination IP and Port are required.")

    # Convert destination port to int
    try:
        dest_port = int(dest_port)
        if dest_port < 1 or dest_port > 65535:
            raise ValueError("Port number must be between 1 and 65535.")
    except ValueError:
        raise ValueError("Invalid port number.")

    # Create a UDP packet
    message = b"This is a test UDP packet"
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((source_ip, 0))  # Bind to source IP

    # Send the packet
    udp_socket.sendto(message, (dest_ip, dest_port))
    udp_socket.close()

    # Display success message
    print('<h2 class="text-success">UDP Packet Generator</h2>')
    print(f'<p class="text-success">Successfully sent UDP Packet to {dest_ip}:{dest_port}. '
          f'Please check in the packet capture tool.</p>')

except Exception as e:
    # Display error message
    print('<h2 class="text-danger">UDP Packet Generator</h2>')
    print(f'<p class="text-danger">Error: {e}</p>')

# End HTML content
print('</body></html>')
