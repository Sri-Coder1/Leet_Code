#Merging alternate characters in 2 words.
def MergeAlternateString(str1,str2):
    str3 = ""
    mi = min(len(str1),len(str2))
    
    for i in range(mi):
        str3 += str1[i] + str2[i]
    
    if len(str1) > mi:
        str3 += str1[mi:]
    elif len(str2) > mi:
        str3 += str2[mi:]
    
    return str3

str1 = input("Enter the first word ")
str2 = input("Enter the second word ")

print(MergeAlternateString(str1,str2))
print("thank you")