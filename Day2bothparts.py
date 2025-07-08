master = []

def list_creation(master):
    with open("data.txt","r") as fobj:
        data = fobj.readlines()
        for i in data:
            temp = i.split(" ")
            temp_list = []
            for j in temp:
                temp_list.append(int(j))
            master.append(temp_list)

def Salvage(report):
    isSafe = True
    isAscending = True
    isAcceptable = True

    for k in range(len(report)):
        isAscending = True
        i = report.copy()
        i.pop(k)
        if (i[0] > i[1]):
            isAscending = False

        for j in range(len(i)-2):
            if (isAscending == False):
                if (i[j] < i[j + 1]):
                    isAcceptable = False
            elif (i[j] > i[j + 1]):
                isAcceptable = False

            if (isAcceptable == True):
                isAcceptable = (1 <= abs(i[j] - i[j + 1]) <= 3)

        if(isAcceptable == True):
            print(report, "is Truly salvagable", isAcceptable)
            return True

    print(report, "is salvagable",isAcceptable)
    return isAcceptable

def safe_counter(master):
    safe = 0
    safeWithModification = 0

    for i in master:
        isSafe = True
        isAscending = True
        isAcceptable = True

        if (i[0] > i[1]):
            isAscending = False

        for j in range(len(i) - 1):
            if (isAscending == False):
                if (i[j] < i[j + 1]):
                    isAcceptable = False
            elif (i[j] > i[j + 1]):
                isAcceptable = False

            if (isAcceptable == True):
                isAcceptable = (1 <= abs(i[j] - i[j + 1]) <= 3)

        if (isAcceptable == True):
            safe += 1

        # if not acceptable try if we can make it acceptable
        if(isAcceptable == False):
            isSalvagable = Salvage(i)
            if (isSalvagable == True):
                safeWithModification += 1

    print("safe:", safe)
    print("Safe With Modification:", safeWithModification)


list_creation(master)
safe_counter(master)
