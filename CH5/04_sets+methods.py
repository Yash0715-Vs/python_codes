#add
s = {1, 2, 3}
s.add(4)
print(s)

#update
s.update([5, 6, 7])
print(s)

#remove
s.remove(3)
print(s)

#discard
s.discard(2)    

#pop
s.pop() #removes a random element from the set

#clear
s.clear() #removes all elements from the set

#copy
s1 = s.copy() #creates a shallow copy of the set
print(s1)

#union
s2 = {8, 9, 10}
s3 = s.union(s2)
print(s3)

#intersection
s4 = s.intersection(s2) 
print(s4)

#difference
s5 = s.difference(s2)
print(s5)

#symmetric_difference
s6 = s.symmetric_difference(s2)
print(s6)

#issubset
s7 = {1, 2}
print(s7.issubset(s)) #returns True if s7 is a subset of s

#issuperset
s8 = {1, 2, 3, 4, 5}    
print(s8.issuperset(s)) #returns True if s8 is a superset of s

#isdisjoint
s9 = {6, 7, 8}
print(s.isdisjoint(s9)) #returns True if s and s9 have no elements in common

#intersection_update
s.intersection_update(s2) #updates s to keep only elements found in both sets
print(s)

#symmetric_difference_update
s.symmetric_difference_update(s2) #updates s to keep only elements found in either set,
# but not in both
print(s)
