from DataStream.ByteStream import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeLong(0, 1)
        self.writeLong(0, 1)
        
        self.writeString("token")
        self.writeString()
        self.writeString()

        self.writeInt(18)
        self.writeInt(104)
        self.writeInt(0)

        self.writeString("dev")

        self.writeInt(0) 
        self.writeInt(0)  
        self.writeInt(0) 

        self.writeString()  
        self.writeString() 
        self.writeString()  
        
        self.writeInt(0)

        self.writeString() 

        self.writeString("RU")
        self.writeString()

        self.writeInt(1)

        self.writeString()  
        self.writeString() 
        self.writeString() 

        self.writeVInt(0)

        self.writeString()

        self.writeVInt(1)