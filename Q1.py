str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
len1 = len(str1)
len2 = len(str2)
count = 0
max_count = 0
i = i1 = i2 = 0
subseq = []
while i < len1:
    i1 = i
    i2 = 0
    while i1 < len1 and i2 < len2:
        if str1[i1] == str2[i2]:
            count += 1
            i1 += 1
            i2 += 1
            if count > max_count:
                max_count = count
                t = 0
                while t < max_count:
                    if t >= len(subseq):
                        subseq.insert(t, str2[i2 - max_count + t])
                    elif t < len(subseq):
                        subseq[t] = str2[i2 - max_count + t]
                    t += 1
        else:
            count = 0
            i1 = i
            i2 += 1
    i += 1
print("The longest common subsequence of the two given strings is: ")
print(*subseq, sep = '')
