from utils.aoc_utils import AOCDay, day

@day(11)
class Day11(AOCDay):
    def common(self):
        return 0


    def getNeighbours(self, matrix, i, j):
        neighbours = []

        if i - 1 >= 0:
            # Up
            neighbours.append(matrix[i - 1][j])
        if i - 1 >= 0 and j - 1 >= 0:
            # Up-left
            neighbours.append(matrix[i - 1][j - 1])
        if i - 1 >= 0 and j + 1 <= len(matrix[0]) - 1:
            # Up-right
            neighbours.append(matrix[i - 1][j + 1])
        if i + 1 <= len(matrix) - 1:
            # Down
            neighbours.append(matrix[i + 1][j])
        if i + 1 <= len(matrix) - 1 and  j - 1 >= 0:
            # Down-left
            neighbours.append(matrix[i + 1][j - 1])
        if i + 1 <= len(matrix) - 1 and j + 1 <= len(matrix[0]) - 1:
            # Down-right
            neighbours.append(matrix[i + 1][j + 1])
        if j - 1 >= 0:
            # Left
            neighbours.append(matrix[i][j - 1])
        if j + 1 <= len(matrix[0]) - 1:
            # Right
            neighbours.append(matrix[i][j + 1])

        occupied = 0
        for neighbour in neighbours:
            if neighbour == '#':
                occupied += 1

        return occupied

    def getOccupiedInDirection(self, matrix, i, j, iStep, jStep):
        occupied = 0
        
        i2 = i + iStep
        j2 = j + jStep

        while i2 >= 0 and j2 >= 0 and i2 <= len(matrix) - 1 and j2 <= len(matrix[0]) - 1:
            if matrix[i2][j2] == '#':
                occupied += 1
                break
            elif matrix[i2][j2] == 'L':
                break

            i2 += iStep
            j2 += jStep

        return occupied

    def getSeatInSight(self, matrix, i , j):
        occupied = 0

        # Left
        occupied += self.getOccupiedInDirection(matrix, i, j, 0, -1)

        # Right
        occupied += self.getOccupiedInDirection(matrix, i, j, 0, 1)

        # Up
        occupied += self.getOccupiedInDirection(matrix, i, j, 1, 0)

        # Up-Left
        occupied += self.getOccupiedInDirection(matrix, i, j, 1, -1)

        # Up-Right
        occupied += self.getOccupiedInDirection(matrix, i, j, 1, 1)

        # Down
        occupied += self.getOccupiedInDirection(matrix, i, j, -1, 0)

        # Down-left
        occupied += self.getOccupiedInDirection(matrix, i, j, -1, -1)

        # Down-right
        occupied += self.getOccupiedInDirection(matrix, i, j, -1, 1)

        return occupied

    def iteration(self, seatMatrix):
        newSeatMatrix = []

        for i in range(len(seatMatrix)):
            newSeatMatrix.append([])

            for j in range(len(seatMatrix[0])):
                qtNeightbours = self.getNeighbours(seatMatrix, i, j)

                if seatMatrix[i][j] == 'L' and qtNeightbours == 0:
                    newSeatMatrix[i].append('#')
                elif seatMatrix[i][j] == '#' and qtNeightbours >= 4:

                    newSeatMatrix[i].append('L')
                else:
                    newSeatMatrix[i].append(seatMatrix[i][j])

        return newSeatMatrix

    def iteration2(self, seatMatrix):
        newSeatMatrix = []

        for i in range(len(seatMatrix)):
            newSeatMatrix.append([])

            for j in range(len(seatMatrix[0])):
                qtNeightbours = self.getSeatInSight(seatMatrix, i, j)

                if seatMatrix[i][j] == 'L' and qtNeightbours == 0:
                    newSeatMatrix[i].append('#')
                elif seatMatrix[i][j] == '#' and qtNeightbours >= 5:
                    newSeatMatrix[i].append('L')
                else:
                    newSeatMatrix[i].append(seatMatrix[i][j])

        return newSeatMatrix

    def part1(self):
        oldSeatMatrix = self.inputData.copy()
        seatMatrix = self.iteration(oldSeatMatrix)

        while seatMatrix != oldSeatMatrix:
            oldSeatMatrix = seatMatrix.copy()
            seatMatrix = self.iteration(oldSeatMatrix)

        occupied = 0
        for line in seatMatrix:
            occupied += line.count('#')

        return occupied
    
    def part2(self):
        oldSeatMatrix = self.inputData.copy()
        seatMatrix = self.iteration2(oldSeatMatrix)

        while seatMatrix != oldSeatMatrix:
            oldSeatMatrix = seatMatrix.copy()
            seatMatrix = self.iteration2(oldSeatMatrix)

        occupied = 0
        for line in seatMatrix:
            occupied += line.count('#')

        return occupied