from utils.aoc_utils import AOCDay, day
import re

@day(4)
class Day4(AOCDay):
    def common(self):
        validKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        passports = []
        strPassport = ""

        for line in self.inputData:
            if line != "":
                strPassport += line + " "
            else:
                dicPassport = {}
                values = strPassport.split(' ')

                for value in values:
                    if(value != ""):
                        key, val = value.split(':')
                        if key in validKeys:
                            dicPassport[key] = val
                passports.append(dicPassport)
                strPassport = ""

        if(strPassport != ""):
            for value in values:
                if(value != ""):
                    key, val = value.split(':')
                    if key in validKeys:
                        dicPassport[key] = val
            passports.append(dicPassport)
            strPassport = ""

        self.inputData = passports


    def part1(self):
        valid = 0

        for passport in self.inputData:
            if(len(passport) == 7):
                valid += 1


        return valid
    
    #155 too high
    def part2(self):
        cpt = 0

        for passport in self.inputData:
            if(len(passport) == 7):
                valid = True

                validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                for key in passport:

                    
                    val = passport[key]

                    if key == "byr":
                        if len(val) != 4:
                            valid = False
                        elif int(val) < 1920 or int(val) > 2002:
                            valid = False
                    elif key == "iyr":
                        if len(val) != 4:
                            valid = False
                        elif int(val) < 2010 or int(val) > 2020:
                            valid = False
                    elif key == "eyr":
                        if len(val) != 4:
                            valid = False
                        elif int(val) < 2020 or int(val) > 2030:
                            valid = False
                    elif key == "hgt":
                        if "cm" in val:
                            val = val[:-2]
                            if int(val) < 150 or int(val) > 193:
                                valid = False
                        elif "in" in val:
                            val = val[:-2]
                            if int(val) < 59 or int(val) > 76:
                                valid = False
                        else:
                            valid = False
                    elif key == "hcl":
                        if not re.search("^#[0-9a-f]{6}$", val):
                            valid = False
                    elif key == "ecl":
                        if val not in validEcl:
                            valid = False
                    elif key == "pid":
                        if not re.search("^[0-9]{9}$", val):
                            valid = False

                if valid:
                    cpt += 1

        return cpt