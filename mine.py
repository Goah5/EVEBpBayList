from icecream import ic


class Blueprint:
    def __init__(self, neme: str, me: int, te: int, runs: int, type_group: str, corp : bool = False ):
        """
        :param neme: Name blueprint
        :param me: Material Efficiency
        :param me: Time Efficiency
        :param runs: Number of runs
        :param storage: Storage
        :param type_group: Type group
        """
        self.name = neme
        self.me = me
        self.te = te
        self.runs = runs
        self.orig = (runs == -1)
        self.type_group = type_group
        self.corp = corp


class BlueprintDataBase:
    def __init__(self, *blueprints: list[Blueprint]):
        temp = {}
        temp2 = []
        for b in [b for b in sum(blueprints, [])]:
            if b.name in temp.keys():
                temp[b.name].append(b)
            else:
                temp[b.name] = [b,]
        self.blueprints = temp

    def get_blueprints(self, name: str, BpO=True, BpC=True) -> list[Blueprint]:
        temp = []
        if (BpO == BpC):
            return self.blueprints[name]
        elif BpO == True:
            for i in self.blueprints[name]:
                if i.orig:
                    temp.append(i)
        elif BpC == True:
            for i in self.blueprints[name]:
                if not i.orig:
                    temp.append(i)

        return temp

    def get_blueprint_run(self, name: str) -> int:
        """
        0 if not found,
        -1 if orig, 
        -2 if corp orig,
        else sum runs
        """
        if not (name in self.blueprints.keys()):
            return 0

        temp = self.get_blueprints(name)

        flag = False
        for bruns, bcorp in [(b.runs,b.corp ) for b in temp]:
            if bruns == -1 and not bcorp:
                return -1
            elif bruns == -1 and bcorp:
                flag = True
        if flag:
            return -2


        return sum([b.runs for b in temp])


def get_MyBpList() -> BlueprintDataBase:
    with open("#MyBpList.txt", "r", encoding="utf8") as f:
        MyBpList = f.readlines()
    temp = []
    for s in MyBpList:
        if (t := s.split(' ')[0]).isdigit():
            t = int(t)
            s = s[s.index(" ")+3:]
        else:
            t = 1
        b = s.replace("\n", "").replace("*", "").split("	")
        # ic(b)
        for _ in range(t):
            temp.append(Blueprint(b[0], int(b[1]),
                        int(b[2]), int(b[3]), b[-1]))
    # ic(temp)
    return (temp)

def get_CorpBpList()-> BlueprintDataBase:
    with open("#CorpBpList.txt", "r", encoding="utf8") as f:
        MyBpList = f.readlines()
    temp = []
    for s in MyBpList:
        if (t := s.split(' ')[0]).isdigit():
            t = int(t)
            s = s[s.index(" ")+3:]
        else:
            t = 1
        b = s.replace("\n", "").replace("*", "").split("	")
        # ic(b)
        for _ in range(t):
            temp.append(Blueprint(b[0], int(b[1]),
                        int(b[2]), int(b[3]), b[-1], corp= True))
    # ic(temp)
    return (temp)


def get_AllBpList() -> list:
    with open("#AllBp.txt", "r", encoding="utf8") as f:
        AllBp = f.readlines()
    return AllBp




def removeEmptyBpList(BpList):
    prevhash = 0
    while hash(str(BpList)) != prevhash:
        prevhash = hash(str(BpList))
        for s in BpList:
            if s == "":
                BpList.remove(s)
        for id, s in enumerate(BpList):
            empty = True
            if s.startswith("-"):
                continue
            elif s == "":
                break
            deep = len(s[:s.index(' ')])
            for ss in BpList[id+1:]:
                # ic(ss)
                if ss == "":
                    break
                elif ss.startswith("-"):
                    empty = False
                    break
                elif len(ss[:ss.index(' ')]) <= deep:
                    break

            if empty:
                BpList[id] = ""

    return BpList


def out_BayBpList(BpList: list):
    with open("#BayBpList.txt", "w", encoding="utf8") as f:
        for i in BpList:
            f.write(i)

    return None


def main():
    BpDB = BlueprintDataBase(get_MyBpList(),get_CorpBpList())
    BpList = get_AllBpList()
    for id, s in enumerate(BpList):
        if s[0] == "+":
            continue
        t = BpDB.get_blueprint_run(s[s.index(' ')+1:-1])
        match t:
            case -1:
                BpList[id] = ""
            case -2:
                BpList[id] = f"{BpList[id][:-1]} [Corp]\n"
            case 0:
                pass
                # print(0)
            case _:
                BpList[id] = f"{BpList[id][:-1]} [{t}]\n"

    out_BayBpList(removeEmptyBpList(BpList))

# BpDB = BlueprintDataBase(get_MyBpList())
# ic(BpDB.blueprints["Civilian Data Analyzer Blueprint"])


if __name__ == "__main__":

    main()
