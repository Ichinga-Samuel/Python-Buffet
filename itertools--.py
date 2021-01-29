import itertools as it
import operator as op


a = list(range(1, 8))
b = it.accumulate(a, op.mul, initial=10)
b = list(b)

c = it.chain(a, b)
c = list(c)

# Infinite Iterators
d = it.cycle(c)

e = it.repeat(4, 5)
e = list(e)
f = [4 for _ in range(4)]  # Does the same thing as repeat

g = it.count(start=0.1, step=0.01)

# Iterators terminating on the shortest input sequence:
h = it.compress(a, [0, 0, 1, 0, 0, 1, 2])
h = list(h)

i = it.filterfalse(lambda i: i > 3, a)
i = list(i)

a.extend([8, 9, 0, 6, 2, 3, 1])
aa = a[3:]
k = it.dropwhile(lambda i:  i <= 3, aa)
k = list(k)

j = it.takewhile(lambda i:  i <= 3, aa)
j = list(j)

args = list(it.zip_longest(range(1, 13), range(12, 0, -1)))
s = it.starmap(op.mul, args)
sli = it.islice(args, 2, 5)

pro = it.product('A, B, C, D', '1, 2, 3, 4')
pro1 = it.product('A, B, C, D', '1, 2, 3, 4', repeat=2)
pro2 = it.product('A, B, C, D', repeat=2)
