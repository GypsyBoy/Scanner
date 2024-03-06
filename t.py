import socket

hostd = "bing.com"


def a():
	global hostd
	host = socket.gethostbyname(hostd)
	port = 1
	for i in range(500):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s = sock.bind((host,port))
		print(f"open:{port}")
		#else:
		#	print(f"close:{port}")
		port += 1

a()
