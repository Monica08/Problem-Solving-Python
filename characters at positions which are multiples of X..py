
characters at positions which are multiples of X.


A string S is passed as the input. A positive Integer X is also passed as the input. The program must print the characters at positions which are multiples of X.

Input Format:

The first line contains S.

The second line contains X.

24th0236@mit

Output Format:

The first line contains the characters at positions which are multiples of X.

Boundary Conditions:

Length of S will be from 3 to 100.

Example Input/Output 1:

Input: abcdexyzwqpoolj 5

Output: eqj

Explanation:

The multiples of 5 are like 5, 10, 15,... So the characters in these positions are e,


output:

s = input()
x = int(input())

for i in range(x - 1, len(s), x):
    print(s[i], end="")



explanation :
The program reads the string S and integer X. It starts from the Xth position (index X-1) and prints every Xth character using range(x-1, len(s), x). Since Python uses 0-based indexing, the Xth position is accessed using X-1.