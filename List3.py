"""Lista 3"""

__author__ = 'r.lukaszewski'

import math
def primes(n):
    return [x for x in range(2,n+1) if len([y for y in range(1,int(x**0.5)+1) if x % y == 0]) < 2 ]

def doskonale_skladana(n):
    return [x for x in range(1,n) if sum([y for y in range(1, int(x)/2+1) if x % y == 0]) == x]

def doskonale_funkcyjna(n):
    return filter(lambda x: sum(filter(lambda y: x % y == 0, range(1, int(x)/2+1))) == x, range(1,n))

def rozklad(n):
    pierwsze = primes(n/2+1)
    return[(x, [y for y in range(1,n/2+1) if n % x**y == 0][-1]) for x in pierwsze if n % x == 0 ]

