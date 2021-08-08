import csv
rows=[]
with open("final_data.csv","r") as ssname:
    csvr=csv.reader(ssname)
    for i in csvr:
        rows.append(i)
    
header=rows[0]
star=rows[1:]
print(header)
print(star[0])
header[0]="Row Number"
Mass={}
for pds in star:
    if Mass.get(pds[3]):
        Mass[pds[3]]*(1.989e+30)
    else:
        Mass[pds[3]]=1

maxstar=max(Mass,key=Mass.get)
print("Star {} has mass {}".format(maxstar,Mass[maxstar]))

Radius=list(star)

for pds in Radius:
    Radius=pds[3]
    if Radius.get(pds[4]):
        Radius[pds[4]]*(6.957e+8)
    else:
        Radius[pds[4]]=1

maxstar=max(Radius,key=Radius.get)
print("Star {} has radius {} ".format(maxstar,Radius[maxstar]))

G= 6.67*(1/100000000000)
g=G*(Mass/(Radius*Radius))
print(g)