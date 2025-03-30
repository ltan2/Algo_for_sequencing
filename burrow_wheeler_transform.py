# time complexity = O(N log N)
# space complexity = O(n)
from suffix_array import suffix_array_brute_force

def bwt(search_str):
    cp_str = search_str + "$"
    SA = suffix_array_brute_force(cp_str)

    bwt = ""
    # return preceding char
    for idx in SA:
        if idx == 0:
            bwt += "$"
        else:
            bwt += cp_str[idx-1]
    
    return bwt

bwt_str = bwt("banana")
print(bwt_str)

