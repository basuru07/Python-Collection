list = ['ph', 'ch', 1997, 2000, 2009]
#index    0     1     2     3     4


#update the index[2] value
list[2] = 2001

#remove the 2000
list.remove(2000)

#add value in last part of the list
list.append(2015)

#print the list in index = 2 
print(list[2:])


#membership
print (2001 in list)

#length
print (len(list))


numlist = [2,4,6,8,3,4,2,1]
print(numlist[:4])
