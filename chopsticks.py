# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:11:39 2019

@author: DSU
"""

import copy
from collections import defaultdict

dp = defaultdict(set)   # state space memoization
victories = [0, 0]      # a_victories, b_victories

def state(turn: bool, hands: list):    
    # a victory, b victory - don't memoize, count winner victory
    for looser, hand in enumerate(hands):
        if all(x is 0 for x in hand):
            victories[1 - looser] += 1
            return 'victory'
    
    # check dp state table otherwise add
    key = (turn, *(tuple(x) for x in hands))
    if key in dp: return key
    
    next_turn = 1 - turn
    
    # simmulate split
    if hands[turn][0] is 0 and hands[turn][1] % 2 is 0:
        next_hands = copy.deepcopy(hands)
        next_hands[turn][0], next_hands[turn][1] = [hands[turn][1] // 2] * 2
        dp[key].add(state(next_turn, next_hands))
    
    # tap each opponent hands with each attacker hand
    for tapper_val in hands[turn]:
        if tapper_val is 0: continue
        for tapped_key, tapped_val in enumerate(hands[next_turn]):
            if tapped_val is 0: continue
            next_hands = copy.deepcopy(hands)
            # attack and roll over
            next_hands[next_turn][tapped_key] = (tapped_val + tapper_val) % 5
            # sort for state hash uniqueness
            
            next_hands[next_turn].sort()
            
            dp[key].add(state(next_turn, next_hands))
    
    return key


            
            
            
state(0, [[1,1], [1,1]])
            
            
            
            
            
            
            
            
            
            
            
            
            
            