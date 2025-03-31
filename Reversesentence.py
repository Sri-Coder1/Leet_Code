def reverseString(s):
    word = s.split()
    word.reverse()
    return ' '.join(word)
s = input("enter the sentence")
print(reverseString(s))