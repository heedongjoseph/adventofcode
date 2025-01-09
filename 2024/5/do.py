import math

f = open("data.txt", "r")

sec1 = []
sec2 = []

is_sec1_end = False
for line in f.readlines():
    data = line
    if data == "\n":
        is_sec1_end = True
        continue

    data = data.replace("\n", "")
    if not is_sec1_end:
        sec1.append(data.split("|"))
    else:
        sec2.append(data.split(","))

rs = 0
for idx, s2 in enumerate(sec2):
    is_ok = True
    for idx, x in enumerate(s2):
        if idx == len(s2) - 1:
            break

        after_x = s2[idx + 1 :]

        valid_after_x_list = []
        for s1 in sec1:
            if s1[0] == x:
                valid_after_x_list.append(s1[1])

        for ax in after_x:
            if ax not in valid_after_x_list:
                is_ok = False
                break
    if is_ok:
        rs += int(s2[math.floor(len(s2) / 2)])

print(rs)

# mac: ython3 --version
