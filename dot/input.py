with open("test.txt","r") as f:
    data = f.read()
split_data = data.split("\n")[:-1]
# data = [a.split() for a in split_data]

with open("passing.txt", "w") as f:
    data = [i for i in split_data[0]]
    f.write('["' + '", "'.join(data) + '"],\n')

with open("passing.txt", "a") as f:
    for a in split_data[1:]:
        data = [i for i in a]
        f.write('["' + '", "'.join(data) + '"],\n')