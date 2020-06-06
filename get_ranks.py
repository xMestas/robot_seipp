import requests
import query

def main():
	response = query.query_summoners_byname("doublelift")
	print(response.json())

if __name__ == "__main__":
	main()
