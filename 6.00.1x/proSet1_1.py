# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

s = raw_input("input your num:")

tip1 = s.count('a')
tip2 = s.count('e')
tip3 = s.count('i')
tip4 = s.count('o')
tip5 = s.count('u')

sum = tip1+tip2+tip3+tip4+tip5
print (sum)

