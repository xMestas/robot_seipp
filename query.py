import requests

def read_key():
	key_file = open("keys/riot_api.key", "r")
	return key_file.readline().rstrip()

def check_response(response):
	if response.ok:
		return response.json()
	elif response.status_code == 429:
		print("Rate limit exceeded.  Aborting so riot doesn't ban us.")
		exit(1)
	else:
		print("Uh oh, we got an issue!  Call a developer!  Error message:")
		print(response.text)
		return {}

def query_summoners_by_name(name):
	header = {"X-Riot-Token" : read_key()}
	response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name, headers = header)
	return check_response(response)

def query_league_by_encrypted_summoner_id(id):
	header = {"X-Riot-Token" : read_key()}
	response = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id, headers = header)
	return check_response(response)
