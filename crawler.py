import socket
import netaddr


def scan_IP(Start_IP: str, End_IP: str, Attack_function=None):
	ip_range = netaddr.IPRange(Start_IP, End_IP)
	for ip in ip_range:
		for port in range(65535):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeour(1)
			result = sock.connect_ez((str(ip),port))
			res = (result==0)
			if res == True:
				print(f"[+] Open: {ip}:{port}")
			else:
				print(f"[-] Close: {ip}:{port}")
			sock.close()


scan_IP("192.168.1.105","192.168.1.106")
