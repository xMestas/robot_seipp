import query
import json

def get_soloqueue(leagues_info):
	for i in leagues_info:
		if i["queueType"] == "RANKED_SOLO_5x5":
			return i
	return {}

def main():
	output_dict = {}

	response = query.query_summoners_by_name("boringness")

	if not response:
		print("Recieved an error")
		exit(1)

	response = query.query_league_by_encrypted_summoner_id(response["id"])
	
	if not response:
		print("Recieved an error")
		exit(1)

	solo_queue_info = get_soloqueue(response)
	if not solo_queue_info:
		print("Summoner does not play solo queue")
		exit(1)
	
	output_dict[solo_queue_info["summonerName"]] = solo_queue_info
	print(output_dict)

if __name__ == "__main__":
	main()
