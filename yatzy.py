
def small_straight(dice):
    """
    from yatzy import small_straight
    python -m doctest yatzy.py
    python -m doctest yatzy.py -v
    python -m pytest --doctest-modules
    It doesnot handles sets or unsorted lists.
        
    >>> small_straight({1,2,3,4,5})
    0
    >>> small_straight([1,2,3,5,4])
    0
    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,5,5])
    0
    
    """
    
    if dice == [1,2,3,4,5]:
        return sum(dice)
    return 0

  