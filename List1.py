"""Lista 1, Zad 4"""
__author__ = 'r.lukaszewski'
import math
from itertools import takewhile, ifilter

def erat(n):

    primes = range(1,n,2)
    primes[0] = 0
    zeros = [0]*(len(primes))
    limit = int(math.sqrt(n))

    for p in takewhile(lambda x: x <= limit, ifilter(None,primes)):
        start = (p*p - 1) / 2
        primes[start::p] = zeros[start::p]

    primes[0] = 2

    return filter(None,primes)

def primePower(p,n):
    """
    Oblicz potege czynnika p w liczbie n
    """
    #int(math.log(n, p))+1
    return filter(lambda x: n % math.pow(p,x) == 0, range(1, int(math.log(n, 2))+1))[-1]

def rozklad(n):
    """
    Napisz jednoargumentowa funkcje rozklad(n) ktora oblicza rozklad liczby n na czynniki pierwsze i zwraca jako wynik liste par
    """
    if n <= 2:
        return []
    else:
        return [ (x, primePower(x,n)) for x in erat(n) if n % x == 0]