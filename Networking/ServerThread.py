import socket
import time
from Networking.NetworkFilter import NetworkFilter

class Server:
	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.port = port
		self.ip = ip
		self.clients = []
		self.clientinfo = []

	def start(self):
		self.server.bind((self.ip, self.port))
		print(f"[Server] Listening on {self.ip}:{self.port}. Let's play Nost Brawl!")
		while True:
			self.server.listen()
			client, address = self.server.accept()
			contime = str(int(time.time()))
			contries = 0
			filter = NetworkFilter()
			filter.lvl1protect(self.clients, self.clientinfo, client, address, contime, contries)