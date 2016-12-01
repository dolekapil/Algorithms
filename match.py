"""
CSCI-665 Homework 1: Problem 4
This program finds out if there are multiple stable matching for given
preference list or not based on stable matching algorithm and prints
"YES" if multiple stable matching is possible or else "NO".

author: Kapil Dole
author: Chirag Kular
"""

def stableMatching(menPreference, womenPreference):
    """
    This function runs stable matching algorithm based on the preference
    list give by men and women and gives stable matching pairing.
    :param menPreference: List of list containing men preferences.
    :param womenPreference: List of list containing women preferences.
    :return: Dictionary containing stable matching.
    """

    # Initialize each person to be free.
    freeMen = [n for n in range(len(menPreference))]
    freeWomen = [n for n in range(len(womenPreference))]
    n = len(menPreference)
    man_woman = {}

    # Some man is free and hasn't proposed to every woman.
    for man in freeMen:
        if menPreference[man]:
            woman = menPreference[man][0]
            menPreference[man].remove(woman)

            # If woman is free then, assign man and woman to be partners.
            if woman in freeWomen:
                man_woman[man] = woman
                freeWomen.remove(woman)

            else:
                # Else get the current partner(man'), of the woman.
                for pairedMan, pairedWoman in man_woman.items():
                    if pairedWoman == woman:
                        currentMan = pairedMan

                # Check if woman prefers man to her current partner man' and if so,
                # Assign man and woman to be partners, and man' to be free
                if womenPreference[woman].index(man) < womenPreference[woman].index(currentMan):
                    del man_woman[currentMan]
                    freeMen.append(currentMan)
                    man_woman[man] = woman

                else:
                    # Woman rejects man.
                    pass

    return man_woman


def checkMultipleMatching(matching1, matching2):
    """
    This function takes two stable matching and checks if those are
    one and the same or different.
    :param matching1: Dictionary containing stable matching.
    :param matching2: Dictionary containing stable matching.
    :return: None.
    """

    keys = matching1.keys()
    multipleMatching = False

    # Checking if both stable matching are same or not.
    for key in keys:
        if matching1[key] != matching2[key]:
            multipleMatching = True
            break

    if multipleMatching:
        print("YES")
    else:
        print("NO")


def main():
    """
    This is main function of our program which take input from standard input.
    The first line contains the value n, indicating the number of elements in each group.
    Following this is 2*n lines of data, which contains preference list for men and women.
    Here, we are running stable matching by passing first men preference and women preference
    and then passing the inverse women preference and men preference and then check both
    stable matching.
    :return: None.
    """

    n = int(input().strip())
    menPreference = [[] for counter in range(n)]
    womenPreference = [[] for counter in range(n)]

    for counter in range(n):
        menPreference[counter] = [int(num) for num in input().strip().split(' ')]

    for counter in range(n):
        womenPreference[counter] = [int(num) for num in input().strip().split(' ')]

    matching1 = stableMatching(menPreference, womenPreference)
    matching2 = {value: key for key, value in stableMatching(womenPreference, menPreference).items()}

    checkMultipleMatching(matching1, matching2)


if __name__ == '__main__':
    main()