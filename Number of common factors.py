Given a set of numbers where all other numbers are multiple of the smallest number, the program must find the count of the common factors C excluding 1.

Input Format:

First line will contain the integer value N representing how many numbers are passed as input.

Next N lines will have the numbers.

Output Format:

First line will contain the count of common factors C.

Constraints:

N will be from 2 to 20.

Sample Input/Output:

Example 1:

Input:

2

100

75

Output:

2

Explanation:

The common factors excluding 1 are 5,25. Hence output is 2



output:

n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

m = min(a)
c = 0

for i in range(2, m + 1):
    ok = True
    for x in a:
        if x % i != 0:
            ok = False
            break
    if ok:
        c += 1

print(c)



This program finds the number of common factors (excluding 1) among all the given numbers.

First, the program reads the number of integers n from the user. It then creates an empty list a and reads n integers one by one, storing each value in the list using append(). After all the numbers are stored, the program finds the smallest number in the list using the min() function and stores it in the variable m. The smallest number is used because a common factor cannot be greater than the smallest number in the list.

Next, the variable c is initialized to 0 to count the number of common factors. The program checks every integer from 2 to m using a for loop. The value 2 is used because the question specifies that the factor 1 should not be counted.

For each value i, the variable ok is initially set to True, assuming that i is a common factor. Another for loop then checks whether every number in the list is divisible by i. The condition x % i != 0 checks if the remainder is not zero. If any number is not divisible by i, ok is changed to False, and the break statement immediately exits the inner loop because there is no need to check the remaining numbers.

After checking all the numbers, if ok is still True, it means that i divides every number in the list and is therefore a common factor. The counter c is increased by one.

Finally, after checking all possible factors, the program prints the value of c, which represents the total number of common factors excluding 1.

