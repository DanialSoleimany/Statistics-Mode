list = []
for i in range(1, 3):
    name = str(input("name: "))
    tedad = int(input("tedad: "))
    for j in range(1, tedad+1):
        nomre = float(input("nomre: "))
        list.append(nomre)
        count = 0
        
mode = "No mode"        
for i in range(0, len(list)):
    temp = list.count(list[i])
    if (temp > count):
        count = temp
        index = i
                
if (count > 1):
    mode = list[index]

print("{0}".format(mode))



        
    
    
        
