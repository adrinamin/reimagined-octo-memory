import time

def main():
    print("Please give a random number between 1 and 100 for countdown")
    number = int(input())
    print("Starting countdown...")
    time.sleep(1)
    while number > 0:
        print(number)
        number = number - 1
        time.sleep(1)

    print("Countdown done!")


if __name__=="__main__":
    main()