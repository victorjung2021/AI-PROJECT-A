fruit = ["사과","바나나","바나나","사과","자두","복숭아","자두","사과","포도","포도","자두"]
d = {}
for f in fruit:
    if f in d: 
        d[f]=d[f]+1
    else:
        d[f]=1
print(d)

key_list = ["name","hp","mp","level"]
value_list = ["기사",200,30,5]
character = {}

for i in range(len(value_list)):
    character[key_list[i]]=value_list[i]

print(character)