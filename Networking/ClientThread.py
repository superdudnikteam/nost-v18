import time, traceback
from threading import *

from Logic.Initial.Device import Device
from Logic.Initial.Player import Players
from Logic.Helpers.get.getName import whatIsIt
from Protocol.LaserMessageFactory import packets

class ClientThread(Thread):
	def __init__(self, client, address, clients, clientinfo, contime, contries): #looks like zezhka
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)
		self.clients = clients
		self.clientinfo = clientinfo
		self.contime = contime
		self.contries = contries
		self.player.ip = self.address[0]

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				break
			data += s
		return data

	def run(self):
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					id = int.from_bytes(header[:2], 'big')
					name = whatIsIt.getPacketName(id)
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)

					if id in packets:
						print(f'[{self.address[0]}] >> {name} sended! Id: {id}, Length: {length}')
						message = packets[id](self.client, self.player, data)
						message.decode()
						message.process()
					else:
						print(f'[{self.address[0]}] >> Unknown packet! Id: {id}, Name: {name}')
				if time.time() - last_packet > 7:
					print(f"[Server] {self.address[0]} disconnected!")
					self.client.close()
					self.clients.remove(self.address[0])
					self.clients.remove(self.address[1])
					self.clientinfo.remove(self.contime)
					self.clientinfo.remove(self.contries)
					break
		except Exception as e:
			print(traceback.format_exc())
			self.client.close()
			self.clients.remove(self.address[0])
			self.clients.remove(self.address[1])
			self.clientinfo.remove(self.contime)
			self.clientinfo.remove(self.contries)