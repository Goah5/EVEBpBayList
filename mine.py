from icecream import *
from icecream import ic


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
            if i == j[j.index(' ')+1:-1]:
                BpList.remove(j)

    return BpList


def out_BayBpList(BpList: list):
    with open("BayBpList.txt", "w", encoding="utf8") as f:
        for i in BpList:
            f.write(i)

    return None


def clearBpList_logic(BpList: list[str], id) -> list[str]:
    empty = None

    if BpList[id] == BpList[-1]:
        empty = True
        return empty

    for i in BpList[id+1:]:
        bpLlen = len(BpList[id][:BpList[id].index(" ")])
        ilen = len(i[:i.index(" ")])
        # ic(BpList[id], i, bpLlen, ilen)
        if i.startswith("+"):
            if ilen == bpLlen:  # ++ ++
                empty = True
                break
            elif ilen-1 == bpLlen:  # ПодПопка + ++
                empty = False
                break

        elif i.startswith("-"):
            if ilen == bpLlen:  # ++ --
                empty = False
                break
            elif ilen > bpLlen:  # ++ ---
                empty = True
                break
            elif ilen < bpLlen:  # ++ -
                empty = True
                break

    return empty


def removeEmptyBpList(BpList: list[str]) -> list[str]:
    outBpList = BpList.copy()

    for id, i in enumerate(BpList):
        empty = False

        if i.startswith("+"):
            empty = clearBpList_logic(BpList, id)

        if empty:
            # print(i,j,outBpList[i])
            outBpList[id] = ""

    return outBpList


def clearXBp(BpList: list[str], keys: set[str]) -> list[str]:
    if not keys:
        return BpList
    
    outBpList = BpList.copy()
    for id, i in enumerate(BpList):
        for j in keys:
            if j in i:
                outBpList[id] = ""
    for id, s in enumerate(outBpList[::-1]):
        if s == "":
            outBpList.remove(s)

    return outBpList

def gen_remKeys(X):
    keys = set()
    if X.remXL:
        keys.add(" XL ")
        keys.add("Capital ")
    if X.remStandup:
        keys.add("Standup ")
    if X.remCivilian:
        keys.add("Civilian ")
    return keys

def mine(s):
    #experimental
    s.remOn =       False # On/Off

    s.remXL =       False # XL/Capital
    s.remStandup =  True  # Standup
    s.remCivilian = True  # Civilian
    
    keys = gen_remKeys(s)

    BpList = get_AllBpList()
    MyBpList = get_MyBpList()
    temp = gen_BayBpList(BpList, MyBpList)
    if s.remOn:
        temp = clearXBp(temp, keys)
    temp = removeEmptyBpList(temp)
    out_BayBpList(temp)

class S:
    def __init__(self):
        self.remXL = False
        self.remStandup = False
        self.remCivilian = False

# ic.disable()
if __name__ == "__main__":
    mine(S())
