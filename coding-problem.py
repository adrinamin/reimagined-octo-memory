"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def twoSum(ar, k: int):
    """checks whether two numbers in the list are equal to k

    Args:
        ar (list): the list to be searched for two numbers
        k (int): the number to search for
    """    

    flag=False
    hashSet=set(ar)
    for i in range(len(ar)):
        if k-ar[i] in hashSet:
            flag=True
            break

    if flag:
        print("YES PRESENT")
    else:
        print("NOT PRESENT")

def main():
    ar = [10, 15, 3, 1]
    twoSum(ar, 17)


if __name__=="__main__":
    main()