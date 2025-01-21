''' Lab 02 Exercise'''
# Attribution Statement will be added later
# -----------------
# User Instructions
#
# Write a function best_hand(hand) that takes a seven
# card hand as input and returns the best possible 5
# card hand. The itertools library has some functions
# that may help you solve this problem.
#
# -----------------
# Solution Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools

# Input: 7-card hand        Output: the best 5-card hand
def best_hand(hand):
    # "From a 7-card hand, return the best 5 card hand."

    # use python itertools to get all possible combinations from the hand (stores them all in the list allFiveHands)
    allFiveHands = list(itertools.combinations(hand, 5))
    bestHand = allFiveHands[0]
    # Iterate through allFiveHands checking if any hand is better than the last "best" we set
    for testHand in allFiveHands:
        if hand_rank(testHand) > hand_rank(bestHand):
            bestHand = testHand

    # (a test statement)
    # print(f"Best hand: {bestHand}, rank: {hand_rank(bestHand)}")

    return bestHand
    

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# are already defined in the unit to write 
# your best_hand function.

# Input: a hand 5-card hand     Output: a value indicating the ranking of a hand.
def hand_rank(hand):
    
    ranks = card_ranks(hand) 
    
    # Check if a straight flush is possible
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    # Check if 4-of-a-kind is possible
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    # Check if full house is possible
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    # Check if flush (all cards of same suit) is possible
    elif flush(hand):
        return (5, ranks)
    # Check if straight (cards can be arranged in sequential order) is possible
    elif straight(ranks):
        return (4, max(ranks))
    # Check if 3-of-a-kind is possilbe
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    # Check if 2 pair is possible
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    # Check if 1 pair is possible
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    # Otherwise return the highest rank
    else:
        return (0, ranks)

# Input: 7-card hand        Output: "list of the ranks, sorted with higher first"
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."

    # Makes array "ranks", puts a card in that array based on its "ranking"
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    # Deal with the Ace
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 
    
def best_hand_try():
    # Assert statements for testing (test if a condition is true, throws AssertionError if it's not)

    # This first one checks if the best hand of "6C 7C 8C 9C TC 5C JS", if sorted, is the hand "6C 7C 8C 9C TC"
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

if __name__ == '__main__':
  print(best_hand_try())