"""Returns the first recurring character in a string, or null if there is no recurring character.
"""

def findFirstRepeatingChar(string: str):
    """ Finds the first occurrence of a repeated character by using hashing
    Reading time complexity: O(1)
    Following steps are performed:
    - Create a hash table. 
    - Iterate through the string. 
    - If the character is already in the hash table, return the character. 
    - Otherwise, add the character to the hash table. 
    - If you iterate through the whole string and haven't returned anything, return None.

    Args:
        string (str): the string to search for the first occurrence

    Returns:
        None or char: it either returns the first occurrence or None
    """    

    h = {} # empty hash

    for c in string:
        if c in h:
            return c
        else:
            h[c] = 0
    
    return None


def main():
    result = findFirstRepeatingChar("acbbac")
    print(result)


if __name__=="__main__":
    main()