__author__ = 'Byron'

import sys
def problem1():

    nums = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
    print(nums)
    print(sum(nums))
    pass

def problem2():

    even1 = 0
    even2 = even1
    even1 += 5 if True else 0

    def func(current, last):

        #even1 +=  current if current % 2 == 0 else 0

        if current <= 4000000:
            return func(last+current, current)
        else:
            return current
        pass
    print("x")
    print(func(2,1))
    pass

def main(args):
    problem2()

    pass


if __name__ == '__main__':
    main(sys.argv)
