from os import popen
import random


POPULATION = []
MAX_WEGHT = 500
INITIAL_SELECITON = 20
MUTATION_RATE = 0.0001
GENERATIONS = 100

my_utility = []
my_weight = []

# opens file
#data = open("testFile.txt")
data = open("Program2Input.txt")


def main():
    read_file()
    generate_pop()
    # testOutput()
    data.close()

# reads and fills utility and weight lists


def read_file():
    dataString = data.read()
    dataList = dataString.split()

    # convert string to float
    for i in range(0, len(dataList)):
        dataList[i] = float(dataList[i])
    # add utility to a list
    for j in range(0, len(dataList), 2):
        my_utility.append(dataList[j])
    # add weight to list
    for k in range(1, len(dataList), 2):
        my_weight.append(dataList[k])


# generate a pop. of 1,000 x 400
def generate_pop():
    rows = 1000
    cols = 400
    for i in range(0, rows):
        # appends list with a 0 or 1
        POPULATION.append([getRand() for j in range(0, cols)])

# returns a random int between 0 and 1


def getRand() -> int:
    bit = random.randint(0, 1)
    return bit


def testOutput():
    # print("my utility")
    # for i in range(0, len(my_utility)):
    #     print(my_utility[i], end=' ')
    # print("\nmy weight:")
    # for i in range(0, len(my_weight)):
    #     print(my_weight[i], end=' ')

    # output population, for testing purposes.
    for i in range(0, 50):
        for j in range(0, 50):
            print(POPULATION[i][j], end=' ')


if __name__ == '__main__':
    main()
