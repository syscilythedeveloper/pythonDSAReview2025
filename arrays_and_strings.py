from collections import defaultdict
#Arrays and lists 

#1 Is Unique. Implement and algorithm to determine if a string has all unique characters? W

def isUnique(word):
    word = word.lower()
    charMap = defaultdict(int)
    for char in word: 
            charMap[char]+=1
    for key in charMap:
        if charMap[key] >1:
            return False
    return True


#1a. What if you can't use additional data strucutures?
def isUnique2(word):
    word = word.lower()
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True


#2. Is permutation 
def checkPermutation(str1, str2):
    charMap1 = {}
    charMap2 = {}
    if len(str1) != len(str2):
        return False 
    for char in str1: 
        charMap1[char] = charMap1.get(char, 0) +1
    for char in str2: 
        charMap2[char] = charMap2.get(char, 0) +1
    return charMap1 == charMap2

#3. URLify - replace all spacees ina string with '%20'
def URLify(str):
    trimmed = str.strip()
    return trimmed.replace(" ", "%20")   

#4 palindrome permutation 
def palindrome_perm(str):

    alphaChars = ''.join(c.lower() for c in str if c.isalpha())
    charCount = defaultdict(int)
    for char in alphaChars:
        charCount[char] +=1
    oddBall = set()
    for key in charCount:
        if charCount[key] % 2 != 0:
            oddBall.add(charCount[key])
    return len(oddBall) <= 1

