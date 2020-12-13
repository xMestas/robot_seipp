def read_key(key_file_name):
        key_file = open(key_file_name, "r")
        return key_file.readline().rstrip()
