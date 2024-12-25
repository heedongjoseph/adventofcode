f = open('data.txt', 'r')

x = []
y = []

for line in f.readlines():
    data = line.split("   ")
    x.append(int(data[0]))
    y.append(int(data[1].replace('\n', '')))

f.close()

distance = 0

while True:
    min_x = min(x)
    min_y = min(y)

    distance += abs(min_x - min_y)

    x.remove(min_x)
    y.remove(min_y)

    if len(x) == 0:
        break

print(distance)