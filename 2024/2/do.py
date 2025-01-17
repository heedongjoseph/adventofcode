f = open('data.txt', 'r')

safe_cnt = 0

for line in f.readlines():
    data = line
    data = data.replace('\n', '')
    data = data.split(" ")
    data = [int(x) for x in data]

    x = None
    is_increase = None
    is_safe = True
    for y in data:
        if x is None:
            x = y
        else:
            # The levels are either all increasing or all decreasing.  
            if is_increase is None:
                is_increase = y > x
            elif x == y or is_increase != (y > x):
                is_safe = False
                break

            # Any two adjacent levels differ by at least one and at most three.
            if not (1 <= abs(x - y) <= 3):
                is_safe = False
                break

            x = y

    if is_safe:
        safe_cnt += 1

f.close()

print(safe_cnt)
