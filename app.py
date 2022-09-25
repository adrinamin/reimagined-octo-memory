

def main():
    print("please provide 3 numbers")
    a = int(input())
    b = int(input())
    c = int(input())

    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)
    print("Your numbers are: ")
    print(arr)

    if (a*a) + (b*b) == (c*c):
        print("Pythogorean triplet")
    else:
        print("no Pythogorean triplet")

if __name__=="__main__":
    main()