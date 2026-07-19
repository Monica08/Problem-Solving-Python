
Odd length string - Middle Three letters

An odd length string S is passed as the input. The middle three letters of S must be printed as the output.

Input Format:

First line will contain the string value S

24th0236@mit

Output Format:

First line will contain the middle three letters of S.

Boundary Conditions: Length of S is from 5 to 100

Save

Run

Example Input/Output 1:

Input:

level

Run with a custom test case (Input/Output)

Output:

eve

Example Input/Output 2:

Input:

manager

Output:

nag

Max


output:

s = input()

mid = len(s) // 2

print(s[mid-1:mid+2])


explanation:

The program finds the middle index of the odd-length string using len(s)//2. Then it prints the three middle characters by slicing from mid-1 to mid+2.
