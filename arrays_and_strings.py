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

#5 One away 

#########Review 
#6 String compression

def string_compression(input_s):
    compressed = ""
    count = 1 
    i = 1  
    while i < len(input_s):
        if input_s[i] == input_s[i-1]:
            count+=1
        else: 
            compressed+= input_s[i-1]
            compressed+= str(count)
            count = 1 
        i+=1
    compressed+= input_s[i-1]
    compressed+= str(count)
    return compressed
print(string_compression("sssyy"))


"""
Defuse the bomb 

if K > 0, replace the ith number with the sum of next k numbers 
if K < 0, replace the ith number with the sum of previous k numbers 
if K == 0, replace teh ith number with 0. 
"""
def defuse_the_bomb(arr, k):
    results = [0] * len(arr)

    for i in range(len(arr)):

        if k == 0: 
            results[i] = 0 
        elif k > 0: 
            #arr[0] = arr[1] + arr[2] + arr[3]
            #arr[1] = arr[2] + arr[3] + arr[1]
            #arr[2] = arr[3] + arr[1] + arr[2]
            #arr[3] = arr[0] + arr[1] + arr[2]
            total = 0 
            for j in range(1, k+1):
                index = (i +j) % len(arr)
                print(f"Iteration: {i}. J is: {j}. Index is: {index}")
               
                total+=arr[index]
                print(f"Total is: {total}")
            results[i] = total 
        else: 
            #arr[0] = arr[3] + arr[2] + arr[1]
            #arr[1] = arr[0] + arr[3] + arr[2]
            #arr[2] = arr[1] + arr[0] + arr[3]
            #arr[3] = arr[2] + arr[1] + arr[0]
            total = 0
            for j in range(1, abs(k)+1):
                index = (i-j) % len(arr)
                total += arr[index]
            results[i] = total 



    return results  
  
    
print(defuse_the_bomb([1,2,3,4], 0))
print(defuse_the_bomb([5,7,1,4], 3))
print(defuse_the_bomb([2,4,9,3], -2))