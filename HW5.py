# -*- coding: utf-8 -*-
"""
@author: Blopa Sauma
"""

import itertools
import math
import random

def random_walk(t,x0=0):
    steps = [1 if random.randint(0, 1) else -1 for i in range(int(t))]
    steps[0] += x0
    return list(itertools.accumulate(steps)) 

def count_cross_origin(xs,x0=0):
    count = 0
    for i in range(len(xs)-1):
        if xs[i]==x0 and xs[i-1]!=xs[i+1]:
            count += 1
    return count

def binary_vote(n, positive_voters,**kwargs):
    return [1]*int(n*positive_voters) + [-1]*int(n*(1-positive_voters))

def sample_votes(votes, sample_size,**kwargs):
    # If replacement use random.choices
    res = sum(random.sample(votes,k=sample_size))
    return 1 if res > 0 else 0

def pr_xn_eq_i(n,i,N=1000000,k=520000):
    return math.comb(k,i)*math.comb(N-k,n-i)/math.comb(N,n)

def pr_majority(n):
    p = 0
    for i in range((n//2)+1, n+1):
        p += pr_xn_eq_i(n, i)
    return p

def test(repeats, t, *args, **kwargs):
    r = []
    for i in range(repeats):
        res = t
        for fn in args:
            res = fn(res,**kwargs)
        r.append(res)
    mean = sum(r)/repeats
    std = math.sqrt(sum((i-mean)**2 for i in r)/repeats)
    print(f'repeats={repeats}, t={t}: {mean:.2f} & {std:.2f} with {kwargs}')
    

### MAIN
if __name__ == '__main__':
    random.seed(21)
    
    REPEATS = 50
    
    print("Problem 2c)")
    test(REPEATS, 4e4, random_walk, count_cross_origin, x0=0)
    test(REPEATS, 9e4, random_walk, count_cross_origin, x0=0)
    test(REPEATS, 16e4, random_walk, count_cross_origin, x0=0)
    test(REPEATS*10, 4e4, random_walk, count_cross_origin, x0=0)
    test(REPEATS*10, 9e4, random_walk, count_cross_origin, x0=0)
    test(REPEATS*10, 16e4, random_walk, count_cross_origin, x0=0)
    test(REPEATS*100, 4e4, random_walk, count_cross_origin, x0=0)
    test(REPEATS*100, 9e4, random_walk, count_cross_origin, x0=0)
    test(REPEATS*100, 16e4, random_walk, count_cross_origin, x0=0)
    
    
    REPEATS = 100
    print("Problem 3a-c)")
    test(REPEATS, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=20)
    test(REPEATS, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=100)
    test(REPEATS, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=400)
    test(REPEATS*10, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=20)
    test(REPEATS*10, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=100)
    test(REPEATS*10, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=400)
    
    print("Testing for majority:")
    sample_size = 1
    while True:
        p = pr_majority(sample_size)
        if sample_size%100==1 or p>=0.9:
            print(f'Sample size: {sample_size}, Pr Majority: {p}')
        if p>=0.9:
            break
        sample_size += 1
        
    print("Experimental test:")
    test(REPEATS*10, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=sample_size)
    