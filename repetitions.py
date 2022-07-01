'''
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.
Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3

'''


DNA = list(input())
cont = 0
listNumber =[]
N = DNA[0]
p = 0

for i in DNA:
    if i == N:
        cont += 1
        N = i
    else:        
        cont = 1
        N = i
    listNumber.append(cont)

for i in listNumber:
    if i>p:
        p=i

print(p)
