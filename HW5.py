# -*- coding: utf-8 -*-
"""
@author: Blopa Sauma
"""

import itertools
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
    res = sum(random.sample(votes,sample_size))
    return 1 if res > 0 else (-1 if res < 0 else 0)

def test(repeats, t, *args, **kwargs):
    r = []
    for i in range(repeats):
        res = t
        for fn in args:
            res = fn(res,**kwargs)
        r.append(res)
    print(f'repeats={repeats}, t={t}: {sum(r)/repeats} with {kwargs}')

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
    
    REPEATS = 100
    print("Problem 3a-c)")
    test(REPEATS, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=20)
    test(REPEATS, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=100)
    test(REPEATS, 1e6, binary_vote, sample_votes, positive_voters=0.52, sample_size=400)
    
    