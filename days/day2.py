from utils.aoc_utils import AOCDay, day

@day(2)
class Day2(AOCDay):
    def common(self):
        # Amélioration possible: Mettre ça dans un dictionnaire?
        self.passwords = []
        self.chars = []
        self.left = []
        self.right = []

        for line in self.inputData:
            result = line.split(':')
            policy = result[0]

            self.passwords.append(result[1].strip())

            result = policy.split(' ')
            self.chars.append(result[1])

            result = result[0].split('-')
            self.left.append(int(result[0]))
            self.right.append(int(result[1]))


    def part1(self):
        cpt = 0
        for i in range(len(self.passwords)):
            occ = self.passwords[i].count(self.chars[i])

            if occ >= self.left[i] and occ <= self.right[i]:
                cpt = cpt + 1

        return cpt
    
    def part2(self):
        cpt = 0
        for i in range(len(self.passwords)):
            password = self.passwords[i]

            if bool(password[self.left[i] - 1] == self.chars[i]) ^ bool(password[self.right[i] - 1] == self.chars[i]):
                cpt = cpt + 1 

        return cpt