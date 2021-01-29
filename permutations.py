import itertools as it


n = 8
r = [1,4,5,2,7,0,3,6]
p = it.permutations(range(n))
c = list(range(n))
#b = list(p)
#print(len(b))
#a=next(p)
#print(b)
s = [(i,j) for i,j in zip(c,r)]
print(s)
d=s[:]
for i in s:
	for j in d:
		if i==j:
			continue
		if abs(i[0]-i[1]) == abs(j[0]-j[1]):
			break
	print('hi')
	break
	
else:
	print('t')
	
	
	
	