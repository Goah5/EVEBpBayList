from icecream import *


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
        print(s)
        if s[s.index(" "):s.index(" ")+3] == " x ":
            l.append(s[s.index(" ")+3:])
        else:
            l.append(s)
    return l


def gen_BayBpList(BpList: list, MyBpList: set) -> list:
    ic(BpList, MyBpList)
    for i in MyBpList:
        for j in BpList:
            if i == j[j.index(' ')+1:-1]:
                BpList.remove(j)
    return BpList


def out_BayBpList(BpList: list):
    with open("BayBpList.txt", "w", encoding="utf8") as f:
        for i in BpList:
            f.write(i)
    return None

def rec_clearBpList(BpList: list[str],id) -> list[str]:
    outBpList = BpList.copy()
    


def clearBpList(BpList: list[str]) -> list[str]:
    # ic.disable()
    outBpList = BpList.copy()

    for id, j in enumerate(BpList[:-1]):
        if j.startswith("+"):
            empty = None
            deep = len(j[:j.index(' ')])
            start_deep = int(deep)
            for k in BpList[id+1:]:
                
                if k.startswith("-"):
                    if k[:k.index(' ')] == "-"*deep:
                        # print(1,k[:k.index(' ')], "-"*deep)
                        empty = False
                        ic(id, j, k, deep, empty)
                        break
                    if len(k[:k.index(' ')]) < deep:
                        # print(2,k[:k.index(' ')],deep)
                        empty = True
                        ic(id, j, k, deep, empty)
                        break

                elif k.startswith("+"):
                    if len(k[:k.index(' ')]) > deep:
                        deep += 1
                        ic(id, j, k, deep, empty)
                        
                    elif len(k[:k.index(' ')]) == start_deep:
                        # print(3, k[:k.index(' ')], start_deep)
                        ic(id, j, k, deep, empty)
                        break
                    elif len(k[:k.index(' ')]) < deep:
                        deep += -1
                        ic(id, j, k, deep, empty)
                        
        if start_deep > deep:
            print("deep")
            empty = True
        if empty:
            # print(i,j,outBpList[i])
            outBpList[id] = ""

    return outBpList


# def clearBpList(BpList: list[str]) -> list[str]:

def mine():
    BpList = get_AllBpList()
    MyBpList = get_MyBpList()
    temp = gen_BayBpList(BpList, MyBpList)
    temp = clearBpList(temp)
    out_BayBpList(temp)

# ic.disable()
if __name__ == "__main__":
    mine()
