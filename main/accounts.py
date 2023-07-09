import random
import csv
id = []
pw = []
f = open('main/account.csv','w', newline='')
wr = csv.writer(f)
for x in range(21, 24):
    for y in range(1, 9):
        for z in range(1, 26):
            if (z < 10):
                id.append(str(x)+"1"+str(y)+"0"+str(z))
            else:
                id.append(str(x)+"1"+str(y)+str(z))
            pw.append(random.randint(100000, 999999))
            wr.writerow([id[-1], pw[-1]])
f.close()
