
def read_file(fileName):
    print("Processing: " + fileName)
    read_line(fileName)
    return

def read_line(file):
    with open(file, 'rt') as fd:
        lines = fd.readlines()
        for line in lines:
            print(line)


