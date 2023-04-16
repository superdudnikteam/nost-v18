from Titan.Helpers import Helpers
import json
import time

class Shop:
    """
    << Shop Offers IDs List >>

    0 = Free Brawl Box
    1 = Gold
    2 = Random Brawler
    3 = Brawler
    4 = Skin
    5 = StarPower/ Gadget
    6 = Brawl Box
    7 = Tickets
    8 = Power Points (for a specific brawler)
    9 = Token Doubler
    10 = Mega Box
    11 = Keys (???)
    12 = Power Points
    13 = EventSlot (???)
    14 = Big Box
    15 = AdBox (not working anymore)
    16 = Gems

    """



    offers = []

    def loadOffers(self):
    	self.offers=[]        
    	with open("Logic/Json/Offers.json", "r") as f:
    		data = json.load(f)
    		for i in data.values():
    			self.offers.append(i)
    def UpdateOfferData(self, i):
    	with open("Logic/Json/Offers.json", "r") as f:
    		data = json.load(f)
    	data[str(i)]["WhoBuyed"].append(int(self.player.low_id))
    	with open("Logic/Json/Offers.json", "w") as f:
    		json.dump(data, f, ensure_ascii=False)
    def RemoveOffer(self, i):
    	with open("Logic/Json/Offers.json", "r") as f:
    		data = json.load(f)
    	data.pop(str(i))
    	with open("Logic/Json/Offers.json", "w") as f:
    		json.dump(data, f, ensure_ascii=False)
    
    gold = [
        {
            'Cost': 20,
            'Amount': 150
        },

        {
            'Cost': 50,
            'Amount': 400
        },

        {
            'Cost': 140,
            'Amount': 1200
        }

    ]

    boxes = [
        {
            'Name': 'Big Box',
            'Cost': 30,
            'Multiplier': 1
        },

        {
            'Name': 'Mega Box',
            'Cost': 80,
            'Multiplier': 1
        }

    ]


    token_doubler = {

        'Cost': 50,
        'Amount': 1000
    }

    def encodeShopOffers(self):
        Shop.loadOffers(self)
        wow = self.offers
        count = len(wow)
        self.writeVInt(count)
        for i in range(count):
            item = wow[i]

            self.writeVInt(1)

            self.writeVInt(item['ID']) # ItemID
            self.writeVInt(item['Multiplier']) # Amount
            self.writeDataReference(16, item['BrawlerID'])
            self.writeVInt(item['SkinID']) # SkinID
            self.writeVInt(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]
            
            self.writeVInt(item['Cost'])  # Cost
            
            self.writeVInt(Helpers.Timer(self)) # Timer

            self.writeVInt(2)
            self.writeVInt(100)
            
            if self.player.low_id in item["WhoBuyed"]:
            		self.writeBoolean(True)
            else:
            		self.writeBoolean(False)

            self.writeBoolean(False)
            self.writeVInt(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            self.writeVInt(item['OldCost'])
            self.writeVInt(0)

            self.writeInt(0)
            self.writeStringReference(item['OfferTitle']) # Item name

            self.writeBoolean(False)