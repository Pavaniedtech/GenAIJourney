list1 = [3,4,5]
list2 = [6,7,8]
list3 = [9,10,"ii"]
list4 = ["red","orange","yellow"]

print(list1)
list1.append(100)
print(list1)
print(list1 + list2)

#tuple

t1=(1,2,3)
print(t1)

#create a list with 6 numbers and reverse the list and print it

list5 = [10,20,30,40,50,60]

# Using for loop
print("Reversed list using for loop:",end=" ")
for x in reversed(list5):
    print(x,end=" ")
print()

# Using reverse() method (in-place)
list5.reverse()
print("Reversed list using reverse() function:",list5)

# Using list(reversed())
list(reversed(list5))
print("Reversed list using list(reversed()) function:",list5)

# Using extended slicing
list5[::-1]
print("Reversed list using extended slicing:",list5)

# Using for loop
list5 = [10,20,30,40,50,60]

print("Reversed list using for loop but re-initializing:",end=" ")
for x in reversed(list5):
    print(x,end=" ")
print()


#create a list with 6 number print alternative numbers
#create a list with 6 number and print the sum of all numbers