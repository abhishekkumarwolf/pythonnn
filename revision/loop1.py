''' print multiplication table'''
'''
print("Give the number:\n")
number = int(input())

i =1
while ( i < 11 ):
    
    print(number*i)
    i = i +1
'''
'''
n = 4
for i in range(n):
    print(i)


li = ["ram", "mohan", "sita", 6]
for i  in li:
    print(i)

tup = ("binod", 54, True, "ok")
for i in tup:
    print(i)

d = dict({'x':123, 'y': 34})
for i in d:
    print(i)

set = { 1, 3 ,"fdre"}
for i in set:
    print(i)
'''
'''
#loop control 
for letter in 'iamabhishekthegreat':
    if letter == 'e' or letter == 'g':
        continue
    print('Current letter: ', letter)

print('\n')


for letter in 'iamabhishekthegreat':
    if letter == 'e' or letter == 'g':
        break
    print('Current letter: ', letter)
'''

for letter in 'iamabhishekthegreat':
    if letter == 'e' or letter == 'g':
        pass
    print('Current letter: ', letter)

print('\n')