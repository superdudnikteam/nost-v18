from DataStream.ByteStream import Writer

class LogicClientAvatar(Writer):
    def encode(self):
        self.writeVInt(self.player.high_id)  # High Id
        self.writeVInt(self.player.low_id)  # Low Id

        self.writeVInt(self.player.high_id)  # High Id
        self.writeVInt(self.player.low_id)  # Low Id

        self.writeVInt(self.player.high_id)  # High Id
        self.writeVInt(self.player.low_id)  # Low Id

        if self.player.name == "Guest":
            self.writeString("Guest")  # Player Name
            self.writeVInt(0)
        else:
            self.writeString(self.player.name)  # Player Name
            self.writeVInt(1)

        self.writeString()

        self.writeVInt(8)

        # Unlocked Brawlers & Resources array
        self.writeVInt(len(self.player.card_unlock_id) + 4)  # count

        index = 0
        for unlock_id in self.player.card_unlock_id:
            self.writeVInt(23)
            self.writeVInt(unlock_id)
            try:
                self.writeVInt(self.player.BrawlersUnlockedState[str(index)])
            except:
                self.writeVInt(1)

            index += 1

        self.writeVInt(5)  # csv id
        self.writeVInt(1)  # resource id
        self.writeVInt(self.player.brawl_boxes)  # resource amount

        self.writeVInt(5)  # csv id
        self.writeVInt(8)  # resource id
        self.writeVInt(self.player.gold)  # resource amount

        self.writeVInt(5)  # csv id
        self.writeVInt(9)  # resource id
        self.writeVInt(self.player.big_boxes)  # resource amount

        self.writeVInt(23)  # csv id
        self.writeVInt(0)  # resource id
        self.writeVInt(0)  # resource amount

        # Brawlers Trophies array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(self.player.brawlers_trophies[str(brawler_id)])

        # Brawlers Trophies for Rank array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(self.player.brawlers_trophies_in_rank[str(brawler_id)])

        self.writeVInt(0)  # array

        # Brawlers Upgrade Points array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(self.player.brawlers_upgradium[str(brawler_id)])

        # Brawlers Power Level array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(self.player.Brawler_level[str(brawler_id)])

        # Gadgets and Star Powers array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(self.player.Brawler_starPower[str(brawler_id)])

        # "new" Brawler Tag array
        self.writeVInt(0)  # brawlers count

        self.writeVInt(self.player.gems)  # Player Gems
        self.writeVInt(self.player.gems)
        self.writeVInt(self.player.player_experience)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)