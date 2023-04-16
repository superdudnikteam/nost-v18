from Logic.Initial.Shop import Shop
from Logic.Initial.Events import Events

from DataStream.ByteStream import Writer

class LogicClientHome(Writer):
    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)  # Timestamp

        self.writeVInt(self.player.trophies)  # Player Trophies
        self.writeVInt(self.player.highest_trophies)  # Player Max Reached Trophies
        self.writeVInt(self.player.highest_trophies)

        self.writeVInt(self.player.trophy_road)  # Trophy Road Reward

        self.writeVInt(99999)  # Player exp set to high number because of the name and bot battle level restriction

        self.writeDataReference(28, self.player.profile_icon)  # Player Icon ID
        self.writeDataReference(43, self.player.name_color)  # Player Name Color ID

        self.writeVInt(0)  # array

        # Selected Skins array
        self.writeVInt(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeVInt(29)
            self.writeVInt(self.player.brawlers_skins[brawler_id])  # skinID

        # Unlocked Skins array
        self.writeVInt(len(self.player.skins_id))
        for skin_id in self.player.skins_id: # skins_id
            self.writeDataReference(29, skin_id)

        self.writeVInt(0) # Leaderboard Global TID (Asia, Global)
        self.writeVInt(self.player.highest_trophies)
        self.writeVInt(self.player.highest_trophies)

        self.writeBoolean(False)  # "token limit reached message" if true
        self.writeVInt(1)
        self.writeBoolean(True)

        self.writeVInt(self.player.tokensdoubler)  # Token doubler ammount
        self.writeVInt(0)  # Season End Timer

        self.writeByte(8)  # related to shop token doubler

        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0)
        self.writeVInt(0)

        # Shop offers
        Shop.encodeShopOffers(self) # offers

        self.writeVInt(0)  # array

        self.writeVInt(self.player.battle_tokens)
        self.writeVInt(0)  # Time till Bonus Tokens (seconds)

        self.writeVInt(0)  # array

        self.writeVInt(self.player.tickets)  # Tickets
        self.writeVInt(0)

        self.writeDataReference(16, self.player.brawler_id)  # Selected Brawler

        self.writeString(self.player.region)  # Location
        self.writeString()  # Supported Content Creator

        self.writeVInt(3) #Animation Count
        self.writeInt(3)
        self.writeInt(self.player.tokensAnim)
        self.writeInt(4)
        self.writeInt(self.player.trophiesAnim)
        self.writeInt(5)
        self.writeInt(self.player.bigTokensAnim)

        self.player.tokensAnim = 0
        self.player.trophiesAnim = 0
        self.player.bigTokensAnim = 0

        self.writeVInt(2019049)

        self.writeVInt(100) # Ammount of tokens needed for 1 brawl box

        self.writeVInt(10)

        for item in Shop.boxes:
            self.writeVInt(item['Cost'])
            self.writeVInt(item['Multiplier'])

        self.writeVInt(Shop.token_doubler['Cost'])
        self.writeVInt(Shop.token_doubler['Amount'])

        self.writeVInt(500)
        self.writeVInt(50)
        self.writeVInt(999900)

        self.writeVInt(0)  # array

        self.writeVInt(7)  # array

        for i in range(7):
            self.writeVInt(i)

        # Logic Events
        Events.offset(self)
        Events.newOffset(self)

        # Logic Shop
        self.writeVInt(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVInt(i)

        self.writeVInt(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVInt(i)

        self.writeVInt(3)
        for i in [10, 30, 80]:  # Tickets price
            self.writeVInt(i)

        self.writeVInt(3)
        for i in [6, 20, 60]:  # Tickets amount
            self.writeVInt(i)

        self.writeVInt(len(Shop.gold))
        for item in Shop.gold:
            self.writeVInt(item['Cost'])

        self.writeVInt(len(Shop.gold))
        for item in Shop.gold:
            self.writeVInt(item['Amount'])

        self.writeVInt(0)  # Unknown
        self.writeVInt(200)  # Max Tokens
        self.writeVInt(20)  # Plus Tokens

        self.writeVInt(8640)
        self.writeVInt(10)
        self.writeVInt(5)

        self.writeVInt(6)

        self.writeVInt(50)
        self.writeVInt(604800)

        self.writeBoolean(True)  # Box boolean

        self.writeVInt(0)  # array

        self.writeVInt(1)  # Menu Theme
        self.writeInt(1)
        self.writeInt(self.player.theme_id)  # Theme ID

        self.writeInt(self.player.high_id)  # High Id
        self.writeInt(self.player.low_id)  # Low Id
        
        self.writeVInt(0)

        self.writeBoolean(False)

        self.writeVInt(0)
        self.writeVInt(0)