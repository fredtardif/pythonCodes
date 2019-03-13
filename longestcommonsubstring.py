# def longestCommonSubstring(a,b):


	### LookUp Table, O(mn) ###
	# lookUpTable = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
	# longest=0

	# for i in range(1,len(a)+1):
	# 	for j in range(1,len(b)+1):
	# 		if a[i-1]==b[j-1]:
	# 			lookUpTable[i][j]=lookUpTable[i-1][j-1]+1
	# 			# longest = max(longest,lookUpTable[i][j])
	# 			if lookUpTable[i][j]>longest:
	# 				longest=lookUpTable[i][j]
	# 				endIndex=i

	# string = a[endIndex-longest:endIndex]

	# return longest,string

# def longestCommonSubstring(a,b,longest):
# 	### Recursion, no memoization ###
# 	if len(a)==0 or len(b)==0:
# 		pass

# 	elif a[0]==b[0]:
# 		longest=longestCommonSubstring(a[1:],b[1:],longest+1)

# 	else:
# 		longest=max(longest,longestCommonSubstring(a[1:],b,0),longestCommonSubstring(a,b[1:],0))

# 	return longest


def longestCommonSubstring(a,b,length,lookup):

	key = a + '|' + b + str(length)

	if key not in lookup.keys():

		if len(a)==0 or len(b)==0:
			lookup[key]=length

		elif a[0]==b[0]:
			lookup[key]=max(longestCommonSubstring(a[1:],b[1:],length+1,lookup),longestCommonSubstring(a[1:],b,0,lookup),longestCommonSubstring(a,b[1:],0,lookup))

		else:
			lookup[key]=max(length,longestCommonSubstring(a[1:],b,0,lookup),longestCommonSubstring(a,b[1:],0,lookup))

	return lookup[key]




if __name__ == '__main__' :

	a = input()
	b = input()
	# longest = longestCommonSubstring(a,b,0)
	longest = longestCommonSubstring(a,b,0,dict())

	print(longest)