from Protocol.Messages.Server.Authentication.LoginOkMessage import LoginOkMessage 
from Protocol.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage

from DataStream.ByteStream import Reader
from Titan.Helpers import Helpers

class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.high_id = self.readInt()
        self.player.low_id = self.readInt()
        self.player.token = self.readString()

        self.major = self.readInt()
        self.minor = self.readInt()
        self.build = self.readInt()

    def process(self):
        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()