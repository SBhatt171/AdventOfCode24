my_dict = {}
removal_items = []
tracker = []

def read(my_dict):
    global removal_items
    with open("data.txt", "r") as fobj:
        text = fobj.readlines()
        for i in range (len(text)):
            if text[i] == "\n":
                break
            else:
                temp = text[i].split(": ")
                my_dict[temp[0]] = int(temp[1].strip())
        for j in text[i+1::]:
            temp = j.split()
            tracker.append(temp)
        removal_items = list(my_dict.keys())


def binary_creation():
    global tracker
    while len(tracker) != 0:
        for i in tracker:
            if i[0] in my_dict.keys() and i[2] in my_dict.keys():
                if i[1] == "XOR":
                    my_dict[i[4]] = str(int(my_dict[i[0]]) ^ int(my_dict[i[2]]))
                elif i[1] == "AND":
                    my_dict[i[4]] = str(int(my_dict[i[0]]) and int(my_dict[i[2]]))
                elif i[1] == "OR":
                    my_dict[i[4]] = str(int(my_dict[i[0]]) or int(my_dict[i[2]]))
                tracker.remove(i)

            else:
                pass

def sort_then_binary():
    new = {}
    for i in list(my_dict.keys()):
        if i in removal_items:
            my_dict.pop(i)

    for i in sorted(my_dict):
        if i.startswith("z"):
            new[i] = my_dict[i]

    print(list(new.values()))

    a = "".join(list(new.values()))[::-1]
    print(int(a,2))

read(my_dict)
binary_creation()
sort_then_binary()
