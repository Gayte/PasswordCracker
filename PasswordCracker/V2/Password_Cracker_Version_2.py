# Importing necessary files.
import random
import time
import sys
import pickle
# Resetting variables and list of letters.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Unhash to reset averages

times = {1:[],2:[],3:[],4:[],5:[]}
with open("avgs.pkl", "wb") as data:
pickle.dump(times, data)

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
    bad_character = False
    counter = 0
    # Checking if the Password is the correct length.
    while not valid:
        bad_character = False
        Password = input("Please enter a Password: ")
        if len(Password) > 6:
            print("Sorry, that Password is too long. Please try again")
            continue

        # Checking if any characters are actually entered.
        if len(Password) == 0:
            print("Sorry, the Password must be at least 1 character long. Please try again")
            continue

        # Checking that the Password only contains letters.
        for q in Password.lower():
            if q not in letters:
                bad_character = True
                continue
        if bad_character:
            print("Sorry, the Password must only contain letters. please try again")
            continue

        # Starting timer
        valid = True
        start_time = time.time()

    # Going through 1 letter Passwords.
    for q in random.sample(letters, 52):
        counter += 1
        if q == Password:
            print("Password cracked.:", q)
            print(counter, "tries")
            found = True
            break

    # Going through 2 letter Passwords.
    if not found:
        for q in random.sample(letters, 52):
            for w in random.sample(letters, 52):
                counter += 1
                if q + w == Password:
                    print("Password cracked.:", q + w)
                    print(counter, "tries")
                    found = True
                    break

    # Going through 3 letter Passwords.
    if not found:
        for q in random.sample(letters, 52):
            for w in random.sample(letters, 52):
                for e in random.sample(letters, 52):
                    counter += 1
                    if q + w + e == Password:
                        print("Password cracked.:", q + w + e)
                        print(counter, "tries")
                        found = True
                        break

    # Going through 4 letter Passwords
    if not found:
        for q in random.sample(letters, 52):
            for w in random.sample(letters, 52):
                for e in random.sample(letters, 52):
                    for r in random.sample(letters, 52):
                        counter += 1
                        if q + w + e + r == Password:
                            print("Password cracked.:", q + w + e + r)
                            print(counter, "tries")
                            found = True
                            break

    # Going through 5 letter Passwords.
    if not found:
        for q in random.sample(letters, 52):
            for w in random.sample(letters, 52):
                for e in random.sample(letters, 52):
                    for r in random.sample(letters, 52):
                        for t in random.sample(letters, 52):
                            counter += 1
                            if q + w + e + r + t == Password:
                                print("Password cracked.:", q + w + e + r + t)
                                print(counter, "tries")
                                found = True
                                break
        # Going through 6 letter Passwords.
        if not found:
            for q in random.sample(letters, 52):
                for w in random.sample(letters, 52):
                    for e in random.sample(letters, 52):
                        for r in random.sample(letters, 52):
                            for t in random.sample(letters, 52):
                                for y in random.sample(letters, 52):
                                    counter += 1
                                    if q + w + e + r + t + y == Password:
                                        print("Password cracked.:", q + w + e + r + t + y)
                                        print(counter, "tries")
                                        found = True
                                        break

               # Calculating and displaying time.
               end_time = time.time()
               print("Your time is: " + str(end_time - start_time) + " seconds")
               time.sleep(1)
               DoExit()

               #Saving times

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
                   average = total/len(lst)

                   return average



               #Averaging and displaying average times.

               if len(password) == 1:
                   print("Average time (1 letter): " + str(mean(avgdict[len(password)])) + " seconds")
               else:
                   print("Average time  (" + str(len(password)) +  " letters): "  + str(mean(avgdict[len(password)])) + " seconds")


PwCrack()
