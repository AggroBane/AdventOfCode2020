from utils.aoc_utils import AOCDay, day

@day(7)
class Day7(AOCDay):
    def common(self):
        lstDicBag = []

        for line in self.inputData:
            dicBag = {}

            line = line.replace(' ', '').replace('.', '')
            name, containers = line.split('bagscontain')
            lstContainers = []

            if containers != "nootherbags":
                containers = containers.split(',')
                for contain in containers:
                    dicContainers = {}
                    contain = contain.replace('bags', '').replace('bag', '')
                    qt = int(contain[0])
                    nameContained = contain[1:]
                    dicContainers["name"] = nameContained
                    dicContainers["qt"] = qt
                    lstContainers.append(dicContainers)

            dicBag["name"] = name
            dicBag["containers"] = lstContainers
            lstDicBag.append(dicBag)

        self.inputData = lstDicBag



    def canHold(self, bagName, lstCanHold):
        for rule in self.inputData:
            if rule["name"] == bagName:
                continue
            else:
                lstContainers = rule["containers"]
                for bag in lstContainers:
                    if bag["name"] == bagName and rule["name"] not in lstCanHold:
                        lstCanHold.append(rule["name"])
                        lstCanHold = self.canHold(rule["name"], lstCanHold)
                        break;

        return lstCanHold
                
    def countBag(self, bagName):
        total = 0

        for rule in self.inputData:
            if rule["name"] == bagName:
                lstContainers = rule["containers"]
                for bag in lstContainers:
                    total += bag["qt"]
                    total += bag["qt"] * self.countBag(bag["name"])

        return total



    def part1(self):
        return len(self.canHold("shinygold", []))
    
    def part2(self):
        return self.countBag("shinygold")