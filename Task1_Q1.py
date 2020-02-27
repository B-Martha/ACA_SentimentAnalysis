str1 = input("Enter first string: ")         
str2 = input("Enter second string: ")        
len1 = len(str1)
len2 = len(str2)
count = 0
max_count = 0
i = i1 = i2 = 0
lcs_array = []

def lcs(str1, str2, len1, len2): 
    lcs_len = [[0 for x in range(len2+1)] for x in range(len1+1)] 
  
    #DP Method to find length of lcs, given by lcs_len[len1][len2]
    for i in range(len1+1): 
        for j in range(len2+1): 
            if i == 0 or j == 0: 
                lcs_len[i][j] = 0
            elif str1[i-1] == str2[j-1]: 
                lcs_len[i][j] = lcs_len[i-1][j-1] + 1
            else: 
                lcs_len[i][j] = max(lcs_len[i-1][j], lcs_len[i][j-1]) 
   
    index = lcs_len[len1][len2] 
   
    lcs = [""] * (index+1) 
  
    # Start from lcs_len[len1][len2] and move towards topright.
    # This is simply the reverse of the method to find length of lcs 
    i = len1 
    j = len2 
    while i > 0 and j > 0: 
         
        if str1[i-1] == str2[j-1]: 
            lcs[index-1] = str1[i-1] 
            i-=1
            j-=1
            index-=1
  
        # If not same, then find the larger of two and go in the direction of larger value 
        elif lcs_len[i-1][j] > lcs_len[i][j-1]: 
            i-=1
        else: 
            j-=1
    return lcs        

  
lcs_array = lcs(str1, str2, len1, len2)
print("The longest common subsequence of " + str1 + " and " + str2 + " is:") 
print(*lcs_array, sep = '')


