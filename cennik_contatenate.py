import csv

cena = []
price = []
tmp_price = []
kod = []
code = []
tmp_kod = []
x = []

with open('ceny.csv', newline='') as f: # Nacita partnumbery a ceny do premenne
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        cena.append(row)

for i in range(len(cena)):      # Preroby partnumber na velke pismena
    tmp1 = cena[i][0].upper()
    tmp2 = cena[i][1].upper()
    tmp3 = tmp1, tmp2
    price.append(tmp3)

for a in range(len(price)):     # Vycisti partnumber a ceny
    ize = price[a][0].strip(" ")
    tmp = ize,price[a][1].strip(" ")
    tmp_price.append(tmp)

with open('kody.csv', newline='') as f: # Nacita kody a partnumbery do premenne
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        kod.append(row)

for i in range(len(kod)):       # Preroby partnumber na velke pismena
    tmp1 = kod[i][0].upper()
    tmp2 = kod[i][1].upper()
    tmp3 = tmp1, tmp2
    code.append(tmp3)

for a in range(len(code)):      # Vycisti kody a partnumber
    ize = code[a][0].strip(" ")
    tmp = ize,code[a][1].strip(" ")
    tmp_kod.append(tmp)

for i, o in tmp_kod:            # porovne partnumbery a pripise ceny
    for j, k in tmp_price:
        if str(j) == str(o):
            g = i,j,k
            x.append(g)

with open('done.csv', 'w', newline='') as f: # Exportuje vysledok do csv
    writer = csv.writer(f, delimiter=';')
    writer.writerows(x)