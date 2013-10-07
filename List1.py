"""Lista 1, Zad 4"""
__author__ = 'solar_plexus'
import math

def erat14(n):
    primes = range(1,n,2)
    primes[0] = 0
    zeros = [0]*(len(primes))
    limit = int(math.sqrt(n))

    for p in takewhile(lambda x: x <= limit, ifilter(None,primes)):
        start = (p*p-1)/2
        primes[start::p] = zeros[start::p]

    primes[0] = 2
    return filter(None,primes)

erat14(456)
