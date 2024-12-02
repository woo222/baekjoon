# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from itertools import permutations

number = list(map(str, input().split()))

for n in number:
	if(len(number) <= 9 and len(n) <= 2):
		continue
	elif(len(number) <= 6 and len(n) <= 3):
		continue
	else:
		print(-1)
		exit()

def num_permutation(num):
	tmp_list = permutations(num)
	num_list = []
	for i in tmp_list:
		num_list.append(int(''.join(i)))

	
	min = num_list[0]
	max = num_list[0]
	
	for element in num_list:
		
		if min >= element:
			min = element
			
		elif max <= element:
			max = element
	return min + max

result = num_permutation(number)
print(result)
	