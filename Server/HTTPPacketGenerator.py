#!C:\Program Files\Python312\python.exe
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import sys
sys.path.append("C:\\Program Files\\Python312\\site-packages")

import os
os.environ["ProgramFiles"] = "C:\\Program Files"  # Required for Scapy on Windows

from scapy.all import IP, TCP, send
import cgi

# Output HTTP headers
print("Content-Type: text/html\n")
print("""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTTP Packet Generator</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
            text-align: center;
            margin-top: 50px;
        }
        .container {
            max-width: 600px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background: #ffffff;
        }
        h1 {
            color: #28a745;  /* Green text for success */
        }
        p {
            font-size: 1.1rem;
            color: #555555;
        }
    </style>
</head>
<body>
    <div class="container">
""")

try:
    # Capture form data
    form = cgi.FieldStorage()
    destination_ip = form.getfirst("destinationIP", "").strip()
    http_path = form.getfirst("httpPath", "/").strip()

    # Validate inputs
    if not destination_ip:
        raise ValueError("Destination IP is required.")
    if not http_path:
        raise ValueError("HTTP Path is required.")

    # Construct HTTP GET payload
    http_payload = f"GET {http_path} HTTP/1.1\r\nHost: {destination_ip}\r\nConnection: close\r\n\r\n"

    # Build and send the HTTP GET packet
    ip_layer = IP(dst=destination_ip)
    tcp_layer = TCP(dport=80, sport=12345, flags="PA")
    packet = ip_layer / tcp_layer / http_payload
    send(packet, verbose=False)

    # Success response
    print(f"""
        <h1>HTTP GET Packet Sent Successfully</h1>
        <p><b>Destination IP:</b> {destination_ip}</p>
        <p><b>HTTP Path:</b> {http_path}</p>
        <p class="text-muted">Please check in your packet capture tool.</p>
    """)

except Exception as e:
    # Error response
    print(f"""
        <h1 class="text-danger">Error</h1>
        <p>{str(e)}</p>
    """)

print("""
    </div>
</body>
</html>
""")