# 4.1
pizzas = ['bacon','cheese','fruit']
for pizza in pizzas:
    print(f'I like {pizza} pizza')
print('that is all')

# 4.2
# list= [value for value in range(1,1_000_000)]
# print(list)
# print(min(list))
# print(max(list))
# print(sum(list))

list = [value for value in range(1,21,2)]
print(list)
list2 = [value for value in range(3,30,3)]
print(list2)

list3 = [value**3 for value in range(1,11)]
print(list3)

# 4.10 slice array
alpha = ['a','b','c','d','e','f']
print(alpha[0:3])
print(alpha[1:4])
print(alpha[-3:])