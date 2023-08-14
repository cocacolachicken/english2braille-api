# a = chr(10256) + chr(10255)
# print(a)
# part,10256,10255
import string
import pandas as pd


def arrayWordOrSign(string):
    # define and init vars
    arr = []
    i = 0
    currentWord = ""
    currentTuple = (True,"")
    wordCheck = False
    if string[0].isalpha():
        wordCheck = True
    count = 0

    # separate words and punctuation/digits
    while i<len(string):
        if string[i] == '\'' or string[i].isalpha():
            if wordCheck:
                currentWord += string[i]
            else:
                currentTuple = (False, currentWord)
                arr.append(currentTuple)  # append the word
                wordCheck = True
                count+=1
                currentWord = string[i]
        else:
            if wordCheck:
                currentTuple = (True, currentWord)
                arr.append(currentTuple)  # append the word
                wordCheck = False
                count += 1
                currentWord = string[i]
            else:
                currentWord += string[i]
        if i == len(string) - 1:
            currentTuple = (wordCheck, currentWord)
            arr.append(currentTuple)  # append the word
        i += 1
    return arr


arr = arrayWordOrSign('hello, hey ha!')
# print(arr[1][1].isalpha())


def getNextWord(arr):
    ans = ''
    isPunctuation = False
    for i in range(len(arr)):
        if arr[i][0]:
            string_before = list(arr[max(i - 1, 0)][1])
            string_after = list(arr[min(i + 1, len(arr)-1)][1])
            if string_before != list(arr[0][1]):
                if string_before[len(string_before)-1] in string.punctuation:
                    isPunctuation = True

            if string_after[0] in string.punctuation:
                isPunctuation = True

            if isPunctuation:
                print("normal word")
                isPunctuation = False

            else:
                print("Isolation!")

        else:
            print("punctuation treatment")



    return ans


print(getNextWord(arr))


# a = ' ,'
# b = list(',fdb')
# c = list(a)
# for i in b:
#     if i in c:
#         print('yes')
