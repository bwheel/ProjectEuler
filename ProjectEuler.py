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

    pass

def main(args):
    problem2()

    pass


if __name__ == '__main__':
    main(sys.argv)
