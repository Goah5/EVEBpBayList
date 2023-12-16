def get_AllBpList() -> list:
    with open("AllBp.txt", "r", encoding="utf8") as f:
        AllBp = f.readlines()
    return AllBp


def get_MyBpList() -> set:
    with open("MyBpList.txt", "r", encoding="utf8") as f:
        MyBpList = f.readlines()
    MyBpList = set(l[0:l.index("*")] for l in MyBpList)
    l = []
    for s in MyBpList:
        if s[s.index(" "):s.index(" ")+3] == " x ":
            l.append(s[s.index(" ")+3:])
        else:
            l.append(s)
    return l


def gen_BayBpList(BpList: list, MyBpList: set) -> list:
    for i in MyBpList:
        for j in BpList:
            if i in j:
                BpList.remove(j)
    return BpList


def out_BayBpList(BpList: list):
    with open("BayBpList.txt", "w", encoding="utf8") as f:
        for i in BpList:
            f.write(i)
    return None


def clearBpList(BpList: list) -> list:
    outBplist = BpList.copy()
    loopOn = 4
    while loopOn:
        for i in range(len(BpList)-1)[::-1]:
            one = BpList[i][:BpList[i].index(' ')]
            nex = BpList[i+1][:BpList[i+1].index(' ')]
            if not "-" in one:
                if not "-" in nex:
                    if len(one) >= len(nex):
                        outBplist[i] = '\n'
                        # print(outBplist[i], BpList[i], BpList[i+1])
        outBplist = [s for s in outBplist if s != "\n"]
        loopOn -= 1

    return outBplist


def mine():
    BpList = get_AllBpList()
    MyBpList = get_MyBpList()
    temp = gen_BayBpList(BpList, MyBpList)
    temp = clearBpList(temp)
    out_BayBpList(temp)


if __name__ == "__main__":
    mine()
