def total_t(arr):
    """
    Returns the total of nodes with value "TRUE" in a given array
    """
    count = 0
    for x in arr:
        if x == True:
            count += 1
    return count

def g_fam(arr):
    """
    Returns the next array
    """
    aux = 0
    hol = []
    while(aux +1 < arr.__len__()):
        if arr[aux] or arr[aux + 1]:
            hol.append(True)
        else:
            hol.append(False)
        aux += 1
    return hol
    
def solution(P):
    """
    Returns the total nodes with value "TRUE" in a given OR-Pascal-triangle
    """
    total = 0
    if P.__len__() <= 1:
        return 
    for x in range(P.__len__()):
        total += total_t(P)
        P = g_fam(P)
    return total