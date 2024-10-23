# import nmap
# import subprocess

# def scanOpenPorts(domain):
#     # The domain you want to scan
#     # domain = "scanme.nmap.org"

#     # Define the Nmap command you want to run, using TCP connect scan (-sT)
#     nmap_command = ["sudo", "nmap",  "-sT", "-p", "21,22,23,25,53,80,110,135,143,443,445,3306,3389", domain]
#     open_ports = []
    
#     # Run the command using subprocess
#     try:
#         result = subprocess.run(nmap_command, capture_output=True, text=True, check=True)
#             # Initialize an empty list to store the open ports
        

#         # Process the output line by line
#         for line in result.stdout.splitlines():
#             # Nmap outputs open ports in a format like:
#             # "PORT     STATE  SERVICE"
#             # "22/tcp   open   ssh"
#             if "open" in line:  # Check if the line contains the word "open"
#                 # Extract the port number, which is the first part of the line before "/"
#                 port = line.split("/")[0]
#                 open_ports.append(port)  # Add the open port to the list

#     except subprocess.CalledProcessError as e:
#         print(f"Nmap command failed with error: {e}")
#         print(f"Error output: {e.stderr}")
#     finally:
#         return open_ports

# print(scanOpenPorts("scanme.nmap.org"))

import socket

def scan_open_ports(domain):
    ports = [21, 22, 23, 25, 53, 80, 110, 135, 143, 443, 445, 3306, 3389]
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout of 1 second
        result = sock.connect_ex((domain, port))  # Try to connect to the port
        if result == 0:  # If connection is successful
            open_ports.append(port)
        sock.close()
    return open_ports

# Example usage
# domain = "google.com"
# ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 143, 443, 445, 3306, 3389]

# open_ports = scan_open_ports(domain, ports_to_scan)
# print(f"Open ports on {domain}: {open_ports}")