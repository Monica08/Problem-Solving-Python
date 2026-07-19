calendar month

A date in DD-MM-YYYY format is passed as the input. The program must print the calendar month.

01-January, 02 - February and so on till 12 - December.

24th0236@mit

Input Format:

First line will contain the date in DD-MM-YYYY format.

Output Format:

The string value denoting the month.

Save

Run

Example Input/Output 1:

Input:

23-12-2016

Output:

December

Run with a custor

ion Time Limit: 5000 millisecs



output:

date = input()

month = date.split("-")[1]

months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

print(months[month])






The program reads the date in DD-MM-YYYY format and uses split("-") to separate the day, month, and year. It extracts the month (MM) and looks up the corresponding month name from a dictionary, then prints the month name.