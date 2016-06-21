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

def problem5():
    # what is the smallest positive number that is evently divisible by the numbers from 1-20
    is_divisible = False
    test_num = 20
    
    while not is_divisible:
        test_num += 1
        for num in range(2,20):
            if test_num % num != 0:
                is_divisible = False
                break
        else:
            is_divisible = True

    print(test_num)
    pass

def problem6():
    
    #find the difference between the sum of squares and the square of the sum for the first one hundred natural numbers
    sum_of_square = 0
    sum = 0
    for x in range(1, 101):
        sum_of_square += x**2
        sum += x
    
    square_of_sum = sum**2
    print(square_of_sum - sum_of_square )
    pass

def problem7():
    #find the 10,001st prime number

    def is_prime(num):

        for n in range(2, num-1):
            #check if it is divisible.
            if num % n == 0:
                return False
        else:
            #otherwise nothing is divisible and that proves this num is a prime
            return True
        pass

    count = 0
    test_num = 2
    while count < 10001: 
        test_num += 1
        if is_prime(test_num):
            count += 1 
    
    print(test_num)

    pass

def problem8():
    
    max_num = 0
    count = 0
    str_num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    nums = list(str_num)
    
    
    def product(list):
        p = 1
        for i in list:
            p *= int(i)
        return p
    
    for n in nums:
        count += 1
        index_n = nums.index(n)
        check_lst = nums[index_n:index_n + 13]
        x = product(check_lst)
        if x > max_num:
            max_num = x
        if count ==1000:
            stop = "now"
    print(max_num)

    
    pass

def main(args):
    
    problem8()
    input("Press enter to exit.")

    pass


if __name__ == '__main__':
    main(sys.argv)
