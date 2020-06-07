import query

def main():
	response = query.query_summoners_by_name("boringness")

	if not response:
		print("Recieved an error")
		exit(1)

	response = query.query_league_by_encrypted_summoner_id(response["id"])
	
	if not response:
		print("Recieved an error")
		exit(1)
	
	print(response)

if __name__ == "__main__":
	main()
