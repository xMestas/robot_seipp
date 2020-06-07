import query
import json

def get_soloqueue(leagues_info):
	for i in leagues_info:
		if i["queueType"] == "RANKED_SOLO_5x5":
			return i
	return {}

def main():
	output_dict = {}
	example_input = ["boringness", "seippy", "fuckthatguydoublelift", "best ieona na"]

	for i in example_input:

		response = query.query_summoners_by_name(i)

		if not response:
			print("Summoner does not exist")
			continue

		response = query.query_league_by_encrypted_summoner_id(response["id"])
	
		if not response:
			print("Summoner does not play ranked")
			continue

		solo_queue_info = get_soloqueue(response)
		if not solo_queue_info:
			print("Summoner does not play solo queue")
			continue
	
		output_dict[solo_queue_info["summonerName"]] = solo_queue_info
	
	with open("summoner_ranks.json", "w") as outfile:
		json.dump(output_dict, outfile)

if __name__ == "__main__":
	main()
