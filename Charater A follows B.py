Charater A follows B

Given a string S and two characters A, B the program must print the number of occurrences where A is followed by B.

Boundary Conditions:

Length of the string S is between 2 and 200.

24th0236@mlt

Save

Run

Input Format:

First line will contain the string value S.

Second line will contain the value of A.

Third line will contain the value of B.

Output Format:

First line will contain the integer which represents the number of occurrences in sring S where A is followed by B

Run with a custom test case (Input/Output)

Sample Input/Output:

Example 1:

Input:

malayalam

a

i

Output:

2

Explanation:

The two occurrences where a is followed by I is as highlighted below. malayalam

Example 2:

Input:

engine

e

n



output:

s = input()
a = input().strip()
b = input().strip()

count = 0

for i in range(len(s) - 1):
    if s[i] == a and s[i + 1] == b:
        count += 1

print(count)



strip() removes extra spaces and newline characters from the beginning and end of a string.