# Hard code a list of random numbers with at least 15 numbers inside
# Have a function that takes in one number as an argument
#     print "Fizz" if the number is divisible by 3
#     print "Buzz" if the number is divisible by 5
#     print "FizzBuzz" if the number is divisible by both 3 and 5
#     The function should only ever print once per number!
# Run the function created for each number in your list.
# HINT: You will need to use the "Modulo" operator.
# +10% bonus - for a JavaScript FizzBuzz in addition to the Python FizzBuzz.

# Py
# declare array w/ 15 nrs
#     include nrs divisible by 3, 5, both and neither
# make loop; for each nr

numbers = [-4000, -18, 0, 2.718, 3, 5, 7, 10, 15, 60, 100, 909, 13455, 238463, 2982342837435]

for i in range(15):
    if((numbers[i] != 0) and (numbers[i] % 3 == 0) and (numbers[i] % 5 == 0)):
        print("FizzBuzz")
    elif((numbers[i] != 0) and numbers[i] % 3 == 0):
        print("Fizz")
    elif((numbers[i] != 0) and numbers[i] % 5 == 0):
        print("Buzz")
    elif(numbers[i] == 2.718):
        print("The exponential constant is not divisible by any number!")
    else:
        print("This number is not divisible by 3 or 5!")