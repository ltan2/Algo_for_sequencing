# construct a suffix array
# time complexity = O(N log N)

def suffix_array_brute_force(search_str):
    suffixes = []
    old_rank = []
    for i in range(len(search_str)):
        suffixes.append(search_str[i:])
    
    old_rank = suffixes.copy()
    suffixes.sort()

    SA = []

    for suffix in suffixes:
        SA.append(old_rank.index(suffix))

    return SA
    
    

# Example
S = "banana$"
# suffixes = $, a$,na$,ana$,nana$,anana$,banana$
# after_sort = $,a$,ana$,anana$,banana$,na$,nana$
print(suffix_array_brute_force(S))
