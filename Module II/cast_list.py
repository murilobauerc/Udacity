def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.split(',')
            cast_list.append(line[0])
    return cast_list
    
print (create_cast_list("flying_circus_cast.txt"))

