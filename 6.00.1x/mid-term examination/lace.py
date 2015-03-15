
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    ls1 = len(s1)
    ls2 = len(s2)
    if ls1>ls2:
        n = ls1
    else:
        n = ls2
    newString = []
    for i in range(n):
        if i<ls1 and i<ls2:
            newString.append(s1[i])
            newString.append(s2[i])
        elif i>=ls1 and i<ls2:
            newString.append(s2[i])
        elif i<ls1 and i>=ls2:
            newString.append(s1[i])
    newString = str(newString)
    newString = newString.translate(None, "[',] ")
    return newString
    
#     for i in range(len(s1)):
#         newString[i+j] = s1[i]
#         if i in range(len(s2)):
#             j = len(newString)
#             newString[i+j] = s2[i]
#         if len(s2) - len(s1)>0:
#             # for x in s2[i:]:
#             #     newString+=x
#             for x in range(len(s2)):
#                 if x>i:
#                     newString[x+j] = s2[x]
#     return newString

# nstr = laceStrings(s1,s2)
# print (nstr)

print (laceStrings('dsadsa','dasda'))








       
