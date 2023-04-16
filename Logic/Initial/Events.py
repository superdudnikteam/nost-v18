from Titan.Helpers import Helpers
import time, json, random

class Events:

    def loadEvents(self):
    	with open("Logic/Json/Events.json", "r") as f:
    		data=json.load(f)
    		return data

    def loadNewEvents(self):
    	with open("Logic/Json/New_Events.json", "r") as f:
    		data=json.load(f)
    		return data

    def offset(self):
        events = Events.loadEvents(self)

        count = len(events)
        self.writeVInt(count)

        maps = events.values()

        for event in maps:

            self.writeVInt(list(maps).index(event) + 1)
            self.writeVInt(list(maps).index(event) + 1)
            self.writeVInt(0)  # IsActive | 0 = Active, 1 = Disabled
            self.writeVInt(Helpers.Timer(self))  # Timer

            self.writeVInt(event['Tokens'])
            self.writeDataReference(15, event["ID"])

            if self.player.low_id in event["Collected"]:
                self.writeVInt(1)
            else:
                self.writeVInt(2)

            self.writeString() # "Double Experience Event" Text
            self.writeVInt(0)

            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(1)
            else:
                self.writeBoolean(False)

            self.writeVInt(0)

    def newOffset(self):
        events = Events.loadNewEvents(self)

        count = len(events)
        self.writeVInt(count)

        maps = events.values()

        for event in maps:

            self.writeVInt(list(maps).index(event) + 1)
            self.writeVInt(list(maps).index(event) + 1)
            self.writeVInt(Helpers.Timer(self))  # IsActive | 0 = Active, 1 = Disabled
            self.writeVInt(Helpers.Timer(self))  # Timer

            self.writeVInt(event['Tokens'])
            self.writeDataReference(15, event["ID"])

            self.writeVInt(2)

            self.writeString() # "Double Experience Event" Text
            self.writeVInt(0)

            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(1)
            else:
                self.writeBoolean(False)

            self.writeVInt(0)