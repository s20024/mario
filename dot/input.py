with open("test.txt","r") as f:
    data = f.read()
split_data = data.split("\n")[:-1]
# data = [a.split() for a in split_data]

# print(split_data)
total_moji = []
for i in split_data:
    for j in i:
        if j not in total_moji:
            total_moji.append(j)

print("変換する文字一覧")
print(total_moji)
print()

dict_total_moji = {}
for i in total_moji:
    rp = input(str(i) + ":")
    dict_total_moji[i] = rp
print()
print("変換した文字の対")
print(dict_total_moji)

with open("passing.txt", "w") as f:
    data = [dict_total_moji[i] for i in split_data[0]]
    f.write('["' + '", "'.join(data) + '"],\n')

with open("passing.txt", "a") as f:
    for a in split_data[1:]:
        data = [dict_total_moji[i] for i in a]
        f.write('["' + '", "'.join(data) + '"],\n')