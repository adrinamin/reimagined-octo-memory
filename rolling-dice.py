import random


def main():
    print("Hi")
    print("Hit enter to roll two dices")
    input()
    dice1 = [1,2,3,4,5,6]
    dice2 = [1,2,3,4,5,6]

    res1 = random.sample(dice1, 1)
    res2 = random.sample(dice2, 1)

    print("Dice 1:", res1)
    print("Dice 2:", res2)


if __name__=="__main__":
    main()