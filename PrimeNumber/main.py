# Write your code below this line 👇
def prime_checker(number):
    its_Prime = True
    for i in range(2, number):
        if number % i == 0:
            its_Prime = False
    if its_Prime:
        print('It\'s a prime')
    else:
         print('It\'s not a prime')

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



