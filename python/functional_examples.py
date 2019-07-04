import functools
import timeit

# multiples of 3 and 5 lambda predicate
mult_3_5= lambda x: x % 3==0 or x % 5==0 # returns bool

if __name__ == '__main__':
    print(mult_3_5(5)) # returns true

    # The following returns the sum of all multiples of 3 and 5
    # Uses list comprehension for n in n if predicate
    # n is not bound as a is the case for a variable in the OOP for loop.
    # this is a hybrid approach as the sum function results in an object
    print(sum(n for n in range(1,10) if mult_3_5(n)))

    print(timeit.timeit(str(sum(list(x for x in range(1,5)))))) #=0.009s
    timeit.timeit("[]+([1]+([2]+([3]+[4])))") #=0.4s
