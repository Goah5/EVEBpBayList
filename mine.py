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

def clearBpList_logic(BpList: list[str],id) -> list[str]:
    empty = None

    for i in BpList[id+1:]:
        bpLlen = len(BpList[id][:BpList[id].index(" ")])
        ilen = len(i[:i.index(" ")])

        if i.startswith("+"):
            if ilen == bpLlen: # ++ ++
                empty = True
                break
            elif ilen-1 == bpLlen: #ПодПопка + ++
                empty = False
                break
        
        elif i.startswith("-"):
            if ilen == bpLlen: # ++ --
                empty = False
                break
            elif ilen > bpLlen: # ++ ---
                empty = True
                break
            elif ilen < bpLlen: # ++ -
                empty = True
                break

    return empty



def clearBpList(BpList: list[str]) -> list[str]:
    outBpList = BpList.copy()

    for id, j in enumerate(BpList[:-1]):
        empty = False

        if j.startswith("+"):
            empty = clearBpList_logic(BpList, id)                       
        
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

ic.disable()
if __name__ == "__main__":
    mine()
