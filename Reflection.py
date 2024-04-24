from mine import get_AllBpList

def get_BayBpList() -> list:
    with open("BayBpList.txt", "r", encoding="utf8") as f:
        BpList = f.readlines()
    return BpList

def out_ReflectionBayBpList(BpList: list):
    with open("ReflectionBayBpList.txt", "w", encoding="utf8") as f:
        for i in BpList:
            f.write(i)
    return None

def gen_ReflectionBayBpList(AllBpList: list, BayBpList: list) -> list:
    outBpList = AllBpList.copy()
    for i, j in enumerate(AllBpList):
        if j in BayBpList:
            outBpList[i] = ""
    return outBpList

AllBpList = get_AllBpList()
BayBpList = get_BayBpList()
t = gen_ReflectionBayBpList(AllBpList, BayBpList)
out_ReflectionBayBpList(t)