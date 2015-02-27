# from string import lowercase
s = raw_input("Please input a String:")

from itertools import count
def find_substring(input_string):
	maxsubstr = input_string[0:0]
	for start in range(len(input_string)):
		for end in count(start+len(maxsubstr)+1):
			substr = input_string[start:end]
			if len(substr)!=(end - start):
				break
			if sorted(substr) == list(substr):
				maxsubstr = substr
	return maxsubstr

log_substr = find_substring(s)
print ("Longest substring in alphabetical order is:"+log_substr)
#lowe = 'abcdefghijklmnopqrstuvwxyz'  
# cont = []
# sub = []
# for i in s:
#     if len(sub) >= 1 and lowe.index(sub[-1]) + 1 != lowe.index(i):
#             cont.append(''.join(sub))
#             sub = []
#     sub.append(i)
 
# cont = sorted(cont, key = len, reverse=True)
# print cont[0]


# cont = []
# sub = []
# for i in s:
#     if len(sub) >= 1 and lowercase.index(sub[-1]) + 1 != lowercase.index(i):
#             cont.append(''.join(sub))
#             sub = []
#     sub.append(i)
 
# cont = sorted(cont, key = len, reverse=True)
# print cont[0]
# counter = 0
# i = 0
# length = len(s)
# temp = s[0]
# substr = s[0]

# while (i<=length-1):
#     if s[i]<s[i+1]:
#         temp += s[i+1]
#         counter += 1
#     elif s[i]>s[i+1]:
#         if len(substr)<len(temp):
#             substr = temp
#         temp = s[i+1]
#     i = i + 1
# if len(temp)>len(substr):
#     substr = temp
# print 'Longest substring in alphabetical order is:',substr


#s = 'cyqfjhcclkbxpbojgkar'




# def long_alphabet(input_string):
#     maxsubstr = input_string[0:0] # empty slice (to accept subclasses of str)
#     for start in range(len(input_string)): # O(n)
#         for end in count(start + len(maxsubstr) + 1): # O(m)
#             substr = input_string[start:end] # O(m)

#             if len(substr) != (end - start): # found duplicates or EOS
#                 break
#             if sorted(substr) == list(substr):
#                 maxsubstr = substr
#     return maxsubstr

# bla = (long_alphabet(s))
# print "Longest substring in alphabetical order is: %s" %bla
