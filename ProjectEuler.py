__author__ = 'Byron'

import sys

def problem1():

    nums = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
    print(nums)
    print(sum(nums))
    pass

def problem2():

    def func(current, last, evenSum):

        even = current + evenSum if current % 2 == 0 else evenSum

        if current <= 4000000:
            return func(last+current, current, even)
        else:
            return even
        pass

    print(func(2,1,0))
    pass

def problem3():
    #find the largest prime factors of a given number.

    # Step 1. get the number from the user.
    test_num = int(input("Enter test number:"))

    # Step 2. figure out all the multiples of that number.
    # create a function to test if number is divisible
    def find_divisible(num):
        for n in range(2, num-1):
            # check if number is divisible.
            if num % n == 0:
                return n
        else:
            #if we didn't find any number that was divisible and it's a prime number
            return num
        pass
    
    # create some variables to test the divisibility
    divisibles = []
    test_divisible = test_num
    result_divisible = find_divisible(test_divisible)
    divisibles.append(result_divisible)

    # test the rest of the values for divisibility
    while result_divisible != test_divisible:
        test_divisible = int(test_divisible / result_divisible)
        result_divisible = find_divisible(test_divisible)
        divisibles.append(result_divisible)
    
    #step 3. find the max prime factor and print it.
    max = 0
    for d in divisibles:
        if d > max:
            max = d
    print("max is {}".format(max))

    pass



def problem4():
    
    # The problem...
    # find the largest number from the product of two 3-digit numbers that is also a palindrome  
    
    palindromes = [] 

    # Step1. loop through all the combinations of 3 digit numbers
    for num1 in range(100,999):
        for num2 in range(num1+1,999):

            # step 2. calculate the product
            test_num = num1 * num2

            # step 3. check for palindrom-i-ness
            if str(test_num) == str(test_num)[::-1]:
                # save off that value.
                palindromes.append(test_num)

    #print the result.
    print("Max number is {}".format(max(palindromes)))
            

    pass

def main(args):
    
    
    problem4()
    input("Press enter to exit.")

    pass


if __name__ == '__main__':
    main(sys.argv)
