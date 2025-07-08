list_1,list_2 = [],[]
def list_creation():
    with open("data","r") as fobj:
        data = fobj.readlines()
        for i in data:
            temp = i.split("   ")
            list_1.append(int(temp[0]))
            list_2.append(int(temp[1]))

def actual(list_1,list_2):
    l1 = sorted(list_1)
    l2 = sorted(list_2)
    total = 0
    for i in range(len(list_1)):
        c = abs(l1[i] - l2[i])
        total = total + c

    print(total)

def similarity_score(list_1,list_2):
    score = 0
    for i in list_1:
        score += (i*(list_2.count(i)))
    print(score)

list_creation()
actual(list_1,list_2)
similarity_score(list_1,list_2)