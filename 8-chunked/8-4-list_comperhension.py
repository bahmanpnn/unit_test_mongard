
"""
[output for v in sequence / list(lists) condition[optional]]
"""

squere=[]

for i in range(1,11):
    if i%2==0:
        s=i**2
        squere.append(s)

# print(squere)


#changing top loop to list comperhension

squere_2=[ i**2 for i in range(1,11)]
squere_3=[ i**2 for i in range(1,11) if i%2==0 ]
squere_4=[ i**2 for i in range(1,11) if i%2==0 if i>=5 ]

print(squere_2,'\n',squere_3,'\n',squere_4)


print('--------------------------')

#example2
v=[(i,'Even' if i%2==0 else 'Odd') for i in range(1,11)]
# v=[(i**2,'Even' if i%2==0 else 'Odd') for i in range(1,11) if i>=3]
print(v)



print('--------------------------')

#example3 ***

l2d=[[1,2],[3,4],[5,6]]

# l=[number for item in l2d for number in item ]
l=[number for item in l2d for number in item if number%2==0]

print(l)