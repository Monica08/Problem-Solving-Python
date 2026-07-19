
Difference between the length of the rectangles 


Alen and Tim both own a tennis grass court and they decide to mow the lawn in and around the court which will cost them Rs.5 per square feet. Given the amount they spent to mow the lawn and the width of the court, find the difference between the length of the courts.

24th0236@mit

Save

Run

Input Format:

First line will contain the amount spent (in Rs) by Alen and Tim separated by space. Second line will contain the width (in feet) of the courts of Alen and Tim separated by space.

Output Format:

The value (in feet) which is the difference between the length of the courts rounded off upto two decimal points.

Example Input/Output 1:

Input:

100 80

Output: 0.00

Explanation:

Area of Alen's court = 100000/5 = 20000 sq.ft. Length = 20000/100 - 200 Area of Tim's court = 80000/5 16000 sq.ft. Length - 16000/80-200

Hence the difference 200-200 = 0 which when rounded off to decimal places is 0.00

Example Input/Output 2:

Input:

17500 40000 50 80

Output: 30.00

Explanation:

Area of Alen's court 17500/5 3500 sq.ft. Length = 3500/50 - 70 Area of Tim's court = 40000/5 8000 sq.ft. Length = 8000/80 - 100

Hence the difference 100-70-30.00



output:

a_amt, t_amt = map(float, input().split())
a_width, t_width = map(float, input().split())

a_length = (a_amt / 5) / a_width
t_length = (t_amt / 5) / t_width

print(f"{abs(a_length - t_length):.2f}")


explanation:

The program reads the amounts spent and widths of both courts. Since mowing costs Rs. 5 per square foot, it calculates the area = amount ÷ 5. Then it finds the length = area ÷ width for each court. Finally, it prints the absolute difference between the two lengths rounded to 2 decimal places.