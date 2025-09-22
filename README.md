Scapy-Based Network Packet Generator

A web-based tool built with Python (Scapy), HTML/CSS/JS, and XAMPP (Apache + PHP + MySQL) to generate, customize, and test network packets.
The tool provides a GUI for users to create packets for multiple protocols and visualize traffic in Wireshark.

🚀 Features
Multi-protocol support:
Generate packets for:
IP
ARP
DNS
UDP
ICMP
HTTP

Customizable packets: Specify source/destination IPs, headers, payloads, and queries.
GUI-based workflow: Easy-to-use HTML/Bootstrap front-end with Python backend scripts.
Feedback System: Users can submit feedback through a form; responses are stored in a database via PHP + MySQL.
Wireshark integration: Generated packets can be captured and analyzed in Wireshark for validation.

🛠 Tech Stack
Backend: Python3 (Scapy), PHP (feedback handling)
Frontend: HTML5, CSS3, Bootstrap, JavaScript
Server: Apache (XAMPP)
Database: MySQL (for storing feedback)
Tools: Wireshark for packet analysis

⚙️ Installation & Setup
1. Setup XAMPP
Install XAMPP

2, Place the project in:
C:\xampp\htdocs\NPG\

3. Start Apache and MySQL in the XAMPP Control Panel.

4. Configure Database

Open phpMyAdmin (http://localhost/phpmyadmin/).

Create a database (e.g., npg_db).

Create a table feedback:

CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(255),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Update submit_feedback.php with your DB credentials.

5. Enable Python Execution in Apache
Configure Apache to run .py CGI scripts.
Ensure Python path is set correctly.

▶️ Running the Project
Start Apache & MySQL in XAMPP.

Open in browser:
http://localhost/NPG/homepage.html
Generate packets → capture with Wireshark.
Submit feedback → stored in MySQL DB.

🔮 Future Work

Multi-protocol packet crafting in a single flow.
Better error handling & logging.
Containerization with Docker for easier deployment.
Role-based access for advanced users.
