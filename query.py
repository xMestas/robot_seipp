import requests

def read_key():
	key_file = open("keys/riot_api.key", "r")
	return key_file.readline().rstrip()

def query_summoners_byname(name):
	header = {"X-Riot-Token" : read_key()}

	response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name, headers = header)
	return response
