def fizz_buzz(n):
    #Algorithm will handle modulo of any value n to generate a fizz buzz
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"   #will give the fizz buzz combination
    elif n % 3 == 0:
        return "Fizz"   #modulo 3 number will be handled here
    elif n % 5 == 0:
        return "Buzz"   #modulo 5 number will be handled here
    else:
        return (n)
