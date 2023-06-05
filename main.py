import subprocess
import socket
""" Perform an ICMP ping scan to find active IP addresses within the given gateway IP range.
    Args:  gateway_ip (str): The gateway IP address in the format "x.x.x".
    Returns: list: A list of active IP addresses found within the gateway IP range. """
def icmp_ping_scanner(gateway_ip):
    ip_list = []
    for i in range(1, 255):
        ip_address = f"{gateway_ip}.{i}"
        command = ["ping", "-n", "1", "-w", "1000", ip_address]
        try:
            subprocess.check_output(command)
            ip_list.append(ip_address)
            print(f"Host {ip_address} is up!")
        except subprocess.CalledProcessError:
            print(f"Host {ip_address} is down!")

    return ip_list

# Define the gateway IP address
gateway_ip = "192.168.250"

# Perform ICMP ping scan to find active IP addresses
ip_list = icmp_ping_scanner(gateway_ip)

print("Scan starts:")

# Iterate through the IP addresses and perform port scanning
for ip_address in ip_list:
    target_ip = socket.gethostbyname(ip_address)
    print(f"Scanning {ip_address}...")

    # Iterate through the port range (50-150) and check if the ports are open
    for port in range(50, 150):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print("Port", port, "is open")
        else:
            print("Port", port, "is closed")

        sock.close()
