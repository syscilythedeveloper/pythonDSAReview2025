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

'''
space complexity -> O(n) because making a charMap based on the number of chars in the string
time complexity -> O(2n) -> 0(n) because iterating through word once and charMap once
'''


#1a. What if you can't use additional data strucutures?
def isUnique2(word):
    word = word.lower()
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True

'''
space ->  O(1) - no additional data strucutres
time  -> O(n^2) - nested loop 
'''

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
'''
space -> O(n) -> Creating additional hashmap with n as number of chars
time -> O(n)  n in the length of strings to interate through 

''' 
#print(checkPermutation("car", "rac"))

#3. URLify - replace all spacees ina string with '%20'
def URLify(str):
    str = str.strip()
    for i in range(len(str)):
        if str[i] == " ":
            str = str.replace(str[i], "%20")
    return str

print(URLify("      Syscily Nicole Brown   "))