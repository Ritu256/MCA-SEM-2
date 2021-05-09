s = input("Enter any string to remove all vowels from it:")
vowels = ('aeiouAEIOU')
#s = s.lower()
for x in s:
    if x in vowels:
        s=s.replace(x," ")
print(s)
