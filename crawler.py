import socket
import netaddr


def scan_IP(Start_IP: str, End_IP: str, Attack_function=None):
	ip_range = netaddr.IPRange(Start_IP, End_IP)
	for ip in ip_range:
		port_num = 1
		for i in range(65555):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			try:
				sock.connect((ip,port_num))
				print(f"[+] Open: {ip}:{port_num}")
			except:
				print(f"[-] Closed: {ip}:{port_num}")
			port_num += 1

scan_IP("10.10.10.10", "10.10.10.12")
