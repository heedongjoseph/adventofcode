import re

f = open('data.txt', 'r')

result = 0

# mul(X,Y)

for line in f.readlines():
    while True:
        x = re.search(r"mul\(\d{1,3},\d{1,3}\)", line)
        if x:
            x_str = x.group()

            line = line.replace(x_str, '', 1)

            x_str = x_str.replace("mul(", "")
            x_str = x_str.replace(")", "")
            x_nums = x_str.split(",")
            result += int(x_nums[0]) * int(x_nums[1])
        else:
            break
f.close()
print(result)
    