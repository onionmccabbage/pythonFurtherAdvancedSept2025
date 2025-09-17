# generators and comprehension

r = range(0,12,3) # start, stop-before, step
g = (i*i for i in (0,3,6,9)) # a generator
print(g, type(g)) # the values of a generator do not all exist in memory
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# the generator is now exhausted
# print(g.__next__()) # throws StopIteration

# comprehension is when we comprehensively deal with every member of a collection
r = [i*i for i in (0,3,6,9)] # use a generator to populate a list
print(r, type(r)) # this time all the results exist in memory
