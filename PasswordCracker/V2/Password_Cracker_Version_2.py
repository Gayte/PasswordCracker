# Importing necessary files.

import pickle
import random
import time
import sys

#Resetting averages by unhashing

times = {1: [], 2: [], 3: [], 4: [], 5: []}
with open("avgs.pkl", "wb") as data:
    pickle.dump(times, data)

# Resetting variables and list of letters.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Defining exit function
def DoExit():
    Exit = input("Exit the password cracker? Y/N:")
    if Exit.upper() == "Y":
        sys.exit()
    elif Exit.upper() == "N":
        PwCrack()
    else:
        print("Enter either Y or N for yes or no.")
        DoExit()


def PwCrack():
    found = False
    valid = False
    badcharacter = False
    counter = 0

    # Checking is the password is the correct length.

    while not valid:
        badcharacter = False
        password = input("Please enter a password: ")
        if len(password) > 8:
            print("Sorry, that password is too long. Please try again")
            continue

        # Checking if any characters are actually entered.

        if len(password) == 0:
            print("Sorry, the password must be at least 1 character long. Please try again")
            continue

        # Checking that the password only contains letters.

        for i in password.lower():
            if i not in letters:
                badcharacter = True
                continue
        if badcharacter:
            print("Sorry, the password must only contain letters. please try again")
            continue

        # Checking that all letters in the password are lowercase.

        # if not password.islower():
        #  print("Sorry, the password must be all lowercase. Please try again")
        #   continue

        # Starting timer

        valid = True
        starttime = time.time()

    # Going through 1 letter passwords.

    for i in random.sample(letters, 26):
        counter += 1
        if i == password:
            print("Password cracked:", i)
            print(counter, "tries")
            found = True
            break

    # Going through 2 letter passwords.

    if not found:
        for i in random.sample(letters, 26):
            for j in random.sample(letters, 26):
                counter += 1
                if i + j == password:
                    print("password cracked:", i + j)
                    print(counter, "tries")
                    found = True
                    break

    # Going through 3 letter passwords.

    if not found:
        for i in random.sample(letters, 26):
            for j in random.sample(letters, 26):
                for k in random.sample(letters, 26):
                    counter += 1
                    if i + j + k == password:
                        print("password cracked:", i + j + k)
                        print(counter, "tries")
                        found = True
                        break

    # Going through 4 letter passwords

    if not found:
        for i in random.sample(letters, 26):
            for j in random.sample(letters, 26):
                for k in random.sample(letters, 26):
                    for l in random.sample(letters, 26):
                        counter += 1
                        if i + j + k + l == password:
                            print("password cracked:", i + j + k + l)
                            print(counter, "tries")
                            found = True
                            break

    # Going through 5 letter passwords.

    if not found:
        for i in random.sample(letters, 26):
            for j in random.sample(letters, 26):
                for k in random.sample(letters, 26):
                    for l in random.sample(letters, 26):
                        for m in random.sample(letters, 26):
                            counter += 1
                            if i + j + k + l + m == password:
                                print("password cracked:", i + j + k + l + m)
                                print(counter, "tries")
                                found = True
                                break

    # Calculating and displaying time.

    endtime = time.time()
    print(f"Your time is: {str(endtime - starttime)} seconds")

    # Saving times

    with open("avgs.pkl", "rb") as olddata:
        olddatadict = pickle.load(olddata)
        x = olddatadict[len(password)]
        x.append(endtime - starttime)
        olddatadict[len(password)] = x

    with open("avgs.pkl", "wb") as olddatatowrite:
        pickle.dump(olddatadict, olddatatowrite)

    with open("avgs.pkl", "rb") as data:
        avgdict = pickle.load(data)

    def mean(lst):
        total = 0
        for i in lst:
            total = total + i
        return total / len(lst)

    # Averaging and displaying average times.

    if len(password) == 1:
        print(f"Average time (1 letter): {str(mean(avgdict[len(password)]))} seconds")
    else:
        print(
            f"Average time  ({len(password)} letters): {str(mean(avgdict[len(password)]))} seconds"
        )
        DoExit()


PwCrack()
