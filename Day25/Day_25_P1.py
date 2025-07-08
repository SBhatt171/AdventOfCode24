available_Locks = []
available_Keys = []

def check_compatibilty():
    Comp_score = 0
    for i in available_Locks:
        for j in available_Keys:
            flag = True
            for k in range(5):
                if i[k] + j[k] <= 5:
                    pass
                else:
                    flag = False
                    break
            if flag == True:
                Comp_score += 1
    print(Comp_score)

def read():
    with open("Day2", "r") as fobj:
        data = fobj.readlines()
        for i in range(0,len(data),8):
            group = data[i:i + 7]
            temp = []
            for k in range(5):
                s = -1
                for j in group:
                    if j[k] == "#":
                        s += 1
                temp.append(s)
            if group[-1].strip() == ".....":
                available_Locks.append(temp)
            else:
                available_Keys.append(temp)

read()
check_compatibilty()
