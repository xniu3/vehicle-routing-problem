import csv
file = open('position.csv')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
file.close()
print(rows)
rows = rows[1:]
distance = []
for i in range(len(rows)-1):
    latitude_i = rows[i][1]
    longitude_i = rows[i][2]
    distance.append([])
    for j in range(0,i-1):
        latitude_j = rows[j][1]
        longitude_j = rows[j][2]
        dis = ((latitude_i - latitude_j) ** 2 + \
            (longitude_i - longitude_j) ** 2 ) ** 0.5
        distance[i].append(dis)
    for j in range(i+1,len(rows)):
        latitude_j = rows[j][1]
        longitude_j = rows[j][2]
        dis = ((latitude_i - latitude_j) ** 2 + \
            (longitude_i - longitude_j) ** 2 ) ** 0.5
        distance[i].append(dis)


with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for dis_list in distance:
        spamwriter.writerow(dis_list)
file.close()