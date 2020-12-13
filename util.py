# A utility file that holds functions used by multiple services


# Read an API key from the API key file.
#
# key_file_name (string): The relative path from the service to the key file
#
# Returns (string): The API key from the file.
def read_key(key_file_name):
        key_file = open(key_file_name, "r") # Open the file
        return key_file.readline().rstrip() # Read the file and strip the new line.
