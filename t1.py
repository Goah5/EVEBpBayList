bp = {}
with open("MyBpList.txt", "r", encoding="utf8") as f:
    MyBpList = f.readlines()
MyBpList = set(l[0:l.index("*")] for l in MyBpList)
for s in MyBpList:
    try:
        if s[s.index(" "):s.index(" ")+3] == " x ":
            bp[s[s.index(" ")+3:]] += int(s[:s.index(" ")])
        else:
            bp[s] += 1
    except:
        if s[s.index(" "):s.index(" ")+3] == " x ":
            bp[s[s.index(" ")+3:]] = int(s[:s.index(" ")])
        else:
            bp[s] = 1

tp = []
for i in bp:
    if bp[i] < 2:
        print(i, bp[i])
        # tp.append(i)
        tp.append(f'{i}* {bp[i]}\n')



with open("t1.txt", "w", encoding="utf8") as f:
    for i in tp:
        f.write(i)
