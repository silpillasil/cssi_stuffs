from operator import xor

def fizzbuzz_individual(number):
    if xor(number % 3 == 0, number % 5 == 0):
        if number % 3 == 0:
            print "fizz"
        if number % 5 == 0:
            print "buzz"
    elif number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    else:
        print(str(number))

fb = fizzbuzz_individual

def fizzbuzz_ultimate(number):
    for num in range(number):
        fb(num+1)

def fizzbuzz_interactive():
    num = input("Enter a number to fizzbuzz: ")
    fizzbuzz_ultimate(num)
