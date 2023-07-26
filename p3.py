import itertools
#arr = {"палатка" : 5, "спальный мешок" : 1, "сидушка": 0.2, "топор": 1.5, "Средства для розжига": 1, "дождевик": 0.2, "свитер": 0.3, "куртка": 1, "перчатки": 0.1, "шляпа": 0.1, "бутылка": 1.5, "еда": 3}
arr = {"палатка" : 5, "спальный мешок" : 1, "сидушка": 0.2, "топор": 1.5, "Средства для розжига": 1, "дождевик": 0.2}

m = int(input("Введите грузоподьёмность рюкзака: "))

ss = list(arr.keys())
result = []
temp = []
perm_set = itertools.permutations(ss)

for item in perm_set:
    massa = 0
    for i in range(0, len(item)):
        massa += arr[item[i]]
        if massa < m:
            temp.append(item[i])
        else:
            break
    if sorted(temp) not in result and len(temp) != 0:
        result.append(sorted(temp))
    temp.clear()

for item in result:
    print(item)
