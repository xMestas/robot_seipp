import requests
import query

def main():
	response = query.query_summoners_byname("doublelift")

	if not response:
		print("Recieved an error")
		exit(1)
	print(response)

if __name__ == "__main__":
	main()
