Average speed

A single line L with a set of space separated values indicating distance travelled and time taken is passed as the input. The program must calculate the average speed S (with precision up to 2 decimal places) and print S as the output.

Note:
The distance and time taken will follow the format DISTANCE@TIMETAKEN. DISTANCE will be in kilometers and TIMETAKEN will be in hours.

Input Format:
The first line contains L.

Output Format:
The first line contains the average speed S.

Boundary Conditions:
Length of L will be from 3 to 100.

Example Input:
60@2 120@3

Example Output:
36.00 kmph

Explanation:
Total distance = 60 + 120 = 180 km
Total time taken = 2 + 3 = 5 hours
Average speed = 180 / 5 = 36.00 kmph
"""
outfile="/mnt/data/Average_Speed_Question.txt"
pypandoc.convert_text(text,"plain",format="md",outputfile=outfile,extra_args=['--standalone'])
print("done")


s = input().split()

d = 0
t = 0

for i in s:
    a = i.split("@")
    d += int(a[0])
    t += int(a[1])

print(f"{d/t:.2f} kmph")


Explantaion:
split() → separates each DISTANCE@TIME
split("@") → separates distance and time
f"{d/t:.2f}" → prints the average speed with 2 decimal places.