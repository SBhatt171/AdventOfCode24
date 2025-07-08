master = []

def list_creation(master):
    with open("Day2", "r") as fobj:
        data = fobj.readlines()
        for i in data:
            temp = i.strip().split()
            master.append(list(map(int, temp)))

def is_safe(report):
    if len(report) < 2:
        return False

    increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if not (1 <= abs(diff) <= 3):
            return False

        if increasing and diff < 0:
            return False
        if not increasing and diff > 0:
            return False

    return True

def salvage(report):
    for k in range(len(report)):
        new_report = report[:k] + report[k+1:]
        if is_safe(new_report):
            print(report, "is Truly salvagable")
            return True
    print(report, "is NOT salvagable")
    return False

def safe_counter(master):
    safe = 0
    safe_with_modification = 0

    for report in master:
        if is_safe(report):
            safe += 1
        elif salvage(report):
            safe_with_modification += 1

    print("Safe:", safe)
    print("Safe With Modification (Dampener):", safe_with_modification)
    print("Total Safe Reports (with Dampener):", safe + safe_with_modification)

# Run
list_creation(master)
safe_counter(master)
