Next Prime Number

A number N is passed as the input. The program must print the next immediate prime number.

A

Input Format:

The first line will contain N.

24th0236@mit

Output Format:

The first line will contain the integer value of next immediate prime number.

Boundary Conditions:

1 <= N <= 999999

Save

Run

Example Input/Output 1:

Input: 11

Run with a custom test case (Inpu

Output: 13

Example Input/Output 2:

Input: 2

Output: 3

n = int(input())

num = n + 1

while True:
    prime = True
    if num < 2:
        prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break

    if prime:
        print(num)
        break

    num += 1


The program first reads the input number `N` and starts checking from `N + 1`. It uses a `while` loop to test each number until a prime number is found. For each number, it assumes it is prime and checks if it is divisible by any value from `2` to the square root of the number. If it is divisible, it is not a prime, so the program checks the next number. When a number has no divisors, it is the next immediate prime number, which is printed as the output.

