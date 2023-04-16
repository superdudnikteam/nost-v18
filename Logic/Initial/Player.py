import json

from Files.Characters import Characters
from Files.Skins import Skins
from Files.Cards import Cards

class Players:
	try:
		settings = json.loads(open("src/config.json", 'r').read())
	except:
		settings = json.loads(open("config.json", 'r').read())

	name = settings["Name"]
	nameset = True
	
	profile_icon = 0
	name_color = 0

	trophy_road = 1
	player_experience = 0

	trophies = settings["Trophies"]
	highest_trophies = settings["HighestTrophies"]

	gems = settings["Gems"]
	gold = settings["Gold"]
	tickets = settings["Tickets"]
	
	theme_id = 41000000 + settings['ThemeID']

	starpower = 76
	
	tokensdoubler = 0
	battle_tokens = 200
	
	brawl_boxes = 0
	big_boxes = 0
	
	high_id = 0
	low_id = 0
	
	box_id = 0
	map_id = 7
	
	brawler_id = 0
	skin_id = 0
	
	status = 0
	
	club_high_id = 0
	club_low_id = 0
	club_role = 0

	region = "RU"
	
	tokensAnim = 0
	trophiesAnim = 0
	bigTokensAnim = 0
	
	tutorialState = 2
	
	skins_id = Skins.get_skins_id()
	brawlers_id = Characters.get_brawlers_id()
	card_skills_id = Cards.get_spg_id()
	card_unlock_id = Cards.get_brawler_unlock()

	brawler_trophies_for_rank = 0
	brawler_trophies = 0
	brawler_upgrade_points = 0
	brawler_power_level = 0
	brawler_star_power = 0
	
	brawlers_trophies = {}
	for id in brawlers_id:
		brawlers_trophies.update({f'{id}': brawler_trophies_for_rank})

	brawlers_skins = {}
	for id in brawlers_id:
		brawlers_skins.update({f'{id}': 0})

	brawlers_trophies_in_rank = {}
	for id in brawlers_id:
		brawlers_trophies_in_rank.update({f'{id}': brawler_trophies_for_rank})

	Brawler_level = {}
	for id in brawlers_id:
		Brawler_level.update({f'{id}': brawler_power_level})

	Brawler_starPower = {}
	for id in brawlers_id:
		Brawler_starPower.update({f'{id}': brawler_star_power})

	brawlers_upgradium = {}
	for id in brawlers_id:
		brawlers_upgradium.update({f'{id}': brawler_upgrade_points})

	battle_result = 0
	game_type = 0
	use_gadget = 1
	rank = 0
	team = 0
	isReady = 0

	bot1 = 0
	bot1_n = None
	bot2 = 0
	bot2_n = None
	bot3 = 0
	bot3_n = None
	bot4 = 0
	bot4_n = None
	bot5 = 0
	bot5_n = None

	def CreateNewBrawlersList():
		Players.BrawlersUnlockedState = {}
		for id in Players.brawlers_id:
			if id == 0:
				Players.BrawlersUnlockedState[str(id)] = 1
			else:
				Players.BrawlersUnlockedState[str(id)] = 0
		return Players.BrawlersUnlockedState

	def __init__(self, device):
		self.device = device