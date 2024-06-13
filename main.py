
def getYellow():
    final = []
    ans = "a"
    while ans != "":
        try:
            ans = [int(input("placement: "))-1,input("letter: ")]
            final.append(ans)
        except:
            ans = ""
            pass
    print(final)
    return final


# import ascii
green = ["","o","","",""]
yellow = list("ger")
grey = list("tuiadlmn")

# yellowCriteria = getYellow()
yellowCriteria = [[3, 'e'], [1, 'r'], [2, 'o'], [1, 'e'], [3, 'o'], [0, 'r'], [2, 'g'], [4, 'r']]

import urllib.request
url = 'https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/6bfa15d263d6d5b63840a8e5b64e04b382fdb079/valid-wordle-words.txt'
validFilename = 'valid-wordle-words.txt'
answerFilename = 'valid-answer-words.txt'

try:
    urllib.request.urlretrieve(url, validFilename)
except:
    userInput = input("using validFilename instead:")
    if userInput != "":
        validFilename = userInput

wordList = []
with open(validFilename, 'r') as f:
    wordList = f.read().splitlines()

with open(answerFilename, 'r') as f:
    answerWordList = f.read().splitlines()


finalWords = [[],[],[],[],[]]
for i in wordList:
    letters = 0
    
    works = True
    
    for pos in range(len(green)):
        if (green[pos] != i[pos]) and (green[pos] != ""):
            works = False
            

    for letter in grey:
        if letter in i:
            works = False

    if works:
        letters += len("".join(green))
        for j in yellow:
            if j in i:
                letters += 1
        if letters != 0:
            finalWords[5-letters].append(i)

count = [0,1,2,3,4]
finalWords = [i for i in finalWords if i != []]
completedWords = finalWords[0]

"""
# if finalWords[0] != []:
#     completedWords = finalWords[0]
#     print("5 match")
# elif finalWords[1] != []:
#     completedWords = finalWords[1]
#     print("4 match")
# elif finalWords[2] != []:
#     completedWords = finalWords[2]
#     print("3 match")
# elif finalWords[3] != []:
#     completedWords = finalWords[3]
#     print("2 match")
# elif finalWords[4] != []:
#     completedWords = finalWords[4]
#     print("1 match")
# else:
    # print("0 match")
"""

endingWords = []



for word in completedWords:
    works = True
    for criteria in yellowCriteria:
        if word[criteria[0]] == criteria[1]:
            works = False
    if works:
        endingWords.append(word)

answerEndingWords = []
for word in endingWords:
    if word in answerWordList:
        answerEndingWords.append(word)

print(endingWords)
print(answerEndingWords)