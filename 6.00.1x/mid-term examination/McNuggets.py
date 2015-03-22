def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    # recursion 
    # if n == 0:
    #     return True
    # for i in (6,9,20):
    #     if n >=i and McNuggets(n-1):
    #         return True
    # return False
    for a in range(0,n/6+1):
        for b in range(0,n/9+1):
            for c in range(0,n/20+1):
                if (a*6 + b*9 +c*20)==n:
                    return True

    return False
    
