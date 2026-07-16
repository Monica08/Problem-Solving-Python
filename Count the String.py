Count the String

The program must accept a string S and print the count of words in S.

Ambiance

Boundary Condition(s):

1 <= Length of S <= 1000

Input Format:

The first line contains S.

Output Format:

The first line contains the integer value representing the word count.

Save

Run

Example Input/Output 1:

Input: like tea

Output: 3

Example Input/Output 2:

Input:

I like coffee very much

Output:

5


output:

s = input()
print(len(s.split()))


Explantion:
Yes. We use split() because it separates the sentence into words based on spaces.

s = "I like tea"
print(s.split())

['I', 'like', 'tea']