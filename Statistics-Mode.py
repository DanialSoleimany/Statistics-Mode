l1 = []
l2 = []
mode = []

for i in range(1, 7):
    x = float(input("num: "))
    l1.append(x)

for i in range(0, len(l1)):
    l2.append(l1.count(l1[i]))

if(max(l2) == 1):
    print("No mode")
if(max(l2) > 1):
    for i in range(0, len(l2)):
        if(l2[i] == max(l2)):
            mode.append(l1[i])
    set = set(mode)
    mode = list(set)
    if(len(mode) > 1):
        print("More than one mode")
        print(mode)
    else:
        mode = list(set)
        print("One mode")
        print(mode)
