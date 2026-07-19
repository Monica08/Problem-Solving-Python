Alterante letters in uppercase 

A string S (only alphabets) is passed as input. The printed output should contain alphabets in odd positions in each word in uppercase and alphabets in even positions in each word in lowercase.

24th0236@mit

Input Format:

The first line will contain S.

Output Format:

The first line will contain the resultant string value based on the conditions provided.

Save

Run

Boundary Conditions: Length of S is from 3 to 100.

Example Input/Output 1:

Input:

TREE GIVES us fruiTS

Output:

TrEe GiVeS Us FrUiTs

Example Input/Output 2:

Input:

Flower is beauTIFUL

Output:

FIOwEr Is BeAuTiFuL




output:

s = input().split()

result = []

for word in s:
    new = ""
    for i in range(len(word)):
        if i % 2 == 0:
            new += word[i].upper()
        else:
            new += word[i].lower()

    result.append(new)

print(" ".join(result))


The program splits the input sentence into words using `split()`. It then processes each word separately. For every word, characters in **odd positions (1st, 3rd, 5th...)** are converted to **uppercase**, and characters in **even positions (2nd, 4th, 6th...)** are converted to **lowercase**. The modified words are stored in a list and finally joined together with spaces using `" ".join()` and printed as the output.
