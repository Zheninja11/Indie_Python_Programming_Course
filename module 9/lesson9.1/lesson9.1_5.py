def file_read(file_name):
    file = open(file_name)
    print(file.read())
    file.close()
