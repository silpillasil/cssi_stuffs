from operator import xor
import fizzbuzz

counter = 1

def fizzbuzz_individual_modified(number):
    if xor(number % 3 == 0, number % 5 == 0):
        if number % 3 == 0:
            return "fizz"
        if number % 5 == 0:
            return "buzz"
    elif number % 3 == 0 and number % 5 == 0:
        return("fizzbuzz")
    else:
        return(str(number))

while True:
    inputt = input("")
    if str(inputt) != fizzbuzz_individual_modified(counter):
        "You lose!"
        break
    counter+=1
    print(fizzbuzz_individual_modified(counter))
    counter+=1
