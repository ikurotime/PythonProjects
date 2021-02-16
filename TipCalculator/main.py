print('Welcome to the tip calculator')
bill = float(input('What was the total bill? '))
people = float(input('How many people to split the bill? '))
percentage = float(input('What percentage tip would you like to give? 10, 12, or 15? '))
calculation = (bill / people) + ((bill / people) * (percentage / 100))
totalBill = round(calculation, 2)
print('Each person should pay: ' + str(totalBill) + "€")

