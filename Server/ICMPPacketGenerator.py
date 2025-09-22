#!C:\Program Files\Python312\python.exe

import cgi
import subprocess

import sys
sys.path.append("C:\\Program Files\\Python312\\site-packages")

# Output HTTP header
print("Content-type: text/html\n")
print('<html lang="en"><head><title>ICMP Packet Generator</title></head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">')
print('<body>')
print('<div class="container mt-4">')

try:
    # Capture form data
    form = cgi.FieldStorage()
    destinationIP = form.getvalue("destinationIP")

    # Validate input
    if not destinationIP:
        raise ValueError("Destination IP is required.")

    # Execute the ping command and capture the output
    command = ["ping", "-n", "1", destinationIP]
    result = subprocess.run(command, capture_output=True, text=True)

    # Check the return code to determine success or failure
    if result.returncode == 0:
        print('<h2 class="text-center text-success">ICMP Packet Generator</h2>')
        print(f'<p class="text-center text-success">Successfully sent ICMP Packet to {destinationIP}.</p>')
        print('<p class="text-center">Check the results in your packet capture tool.</p>')
    else:
        print('<h2 class="text-center text-danger">ICMP Packet Generator</h2>')
        print(f'<p class="text-center text-danger">Failed to send ICMP Packet to {destinationIP}.</p>')
        print(f'<pre class="text-danger">{result.stderr}</pre>')

except Exception as e:
    # Display the error message
    print('<h2 class="text-center text-danger">Error</h2>')
    print(f'<p class="text-center text-danger">{str(e)}</p>')

# Close the HTML structure
print('</div></body></html>')