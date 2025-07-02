Nmap Scanner with Python & Colorized Output
📌 Description
This script uses Nmap to scan a target for open ports and services. It highlights results using Colorama for better readability.

🚀 Features
✅ Scans specified ports on a target host
✅ Detects open/closed ports and their protocols
✅ Uses Colorama to color-code output:

🟢 Green → Open ports
🔴 Red → Closed ports
🟡 Yellow → Filtered ports
🔧 Requirements
📌 Install dependencies before running:

sh
Copy
Edit
pip install nmap colorama
⚡ Usage
Run the script:

sh
Copy
Edit
python nmap_scan.py
It scans scanme.nmap.org on ports 22, 80, and 443.

🛠 Customization
To scan different ports or targets, modify this line:

python
Copy
Edit
scanner.scan("TARGET_IP", "PORTS")
Example:

python
Copy
Edit
scanner.scan("192.168.1.1", "21,22,80,443")
📜 Example Output
vbnet
Copy
Edit
Scanning...
Host: scanme.nmap.org (45.33.32.156)
State: up

Protocol: tcp
Port 22 is open  ✅
Port 80 is closed ❌
Port 443 is open  ✅
