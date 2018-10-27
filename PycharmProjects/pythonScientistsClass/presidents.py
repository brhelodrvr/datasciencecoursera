
presidents = []
with open('/Users/brwarn/Documents/Training/Python/py3sci3day/DATA/presidents.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        [*arg] = line.split(":")
        vid = arg[0]
        lname = arg[1]
        fname = arg[2]
        name = fname + ' ' + lname
        print("name is", name)
        presidents.append(name)
print(presidents)