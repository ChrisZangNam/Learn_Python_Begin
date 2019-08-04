#Link : https://viblo.asia/p/su-dung-comprehensions-trong-python-pVYRPjJEG4ng?fbclid=IwAR0tPZi6sThuVLnZaCJ-sqWO22dblo9KyRjOBxbP0aKBVl0cL7pzb2V7aSk

#1. Introducto to Comprehensions:

#Cu phap:
#       <.......> f(x) for x in <iterable> if <condition>

#to create a List
#       <.......> [f(x) for x in <iterable> if <condition>]

#to creata a Set or Dictionary
#       <.......> {f(x) for x in <iterable> if <condition>}

lst = []
for i in range(1, 11):
    lst.append(i)
print(lst)

lst1 = [i for i in range(1, 11)]
print(lst1)

s = set()
for i in range(1, 21):
    if i % 3 == 0:
        s.add(i)

print(s)
s1 = {i for i in range(1, 21) if i % 3 == 0}
print(s1)

d = {}
for k in range(1, 21):
   if k % 3 == 0:
      d[k] = k ** 2

print(d)

d1 = {k: k ** 2 for k in range(1, 21) if k % 3 == 0}
print(d1)
