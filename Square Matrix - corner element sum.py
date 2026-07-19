Square Matrix - corner element sum

A square matrix of size NxN is passed as the input. The program must calculate and print the sum of the elements in the corners.


Input Format:

The first line will contain the value of N.

The next N lines will contain the N values separated by one or more spaces.

24th0236@mit

Output Format:

The first line will contain the integer value denoting the sum of the elements in the corners.

Save

Run

Boundary Conditions:

2 <= N <= 20

Example Input/Output 1:

Input:

3

Run with a custom test case (Input/Output)

10 90 1

4 22 5

32 8 66

Output:

109

Explanation:

The sum = 10+1+66+32= 109



n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

print(a[0][0] + a[0][-1] + a[-1][0] + a[-1][-1])




The program first reads the size of the square matrix n using n = int(input()). It then creates an empty list a to store the matrix. Using a for loop that runs n times, each row of the matrix is read with input().split(), which separates the values based on spaces. The map(int, ...) function converts these string values into integers, and list() stores them as a list. Each row is then added to the matrix using append(). After the complete matrix is stored, the program accesses the four corner elements using indexing: a[0][0] for the top-left corner, a[0][-1] for the top-right corner, a[-1][0] for the bottom-left corner, and a[-1][-1] for the bottom-right corner. Finally, it adds these four corner values together and prints the sum as the output.