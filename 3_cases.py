# 3.1
friends = ['John','Julia','Helen']
print(friends[0])
print(friends[1])
print(friends[2])
# 3.2
print(f'Hello, {friends[0]}!')
print(f'Hello, {friends[1]}!')
print(f'Hello, {friends[2]}!')
# 3.3
transportation = ['bike','plane','car']
print(f'I would like to have a {transportation[0]}')
# 3.4
guests = ['John','Julia','Helen']
print(f'你想来吃饭吗？{guests[0]}')
print(f'你想来吃饭吗？{guests[1]}')
print(f'你想来吃饭吗？{guests[2]}')
#3.5
print(guests.pop())
guests.insert(0,'Alian')
print(f'你想来吃饭吗？{guests[0]}')
print(f'你想来吃饭吗？{guests[1]}')
print(f'你想来吃饭吗？{guests[2]}')
print('---')
# 3.6
guests.insert(2,'Tom')
guests.insert(1,'Vivian')
guests.append('Peter')
print(f'你想来吃饭吗？{guests[0]}')
print(f'你想来吃饭吗？{guests[1]}')
print(f'你想来吃饭吗？{guests[2]}')
print(f'你想来吃饭吗？{guests[3]}')
print(f'你想来吃饭吗？{guests[4]}')
print(f'你想来吃饭吗？{guests[5]}')
print('---')
#3.6
print(f'sorry,{guests.pop()}')
print(f'sorry,{guests.pop()}')
print(f'sorry,{guests.pop()}')
print(f'sorry,{guests.pop()}')
print(guests)
print(f'你想来吃饭吗？{guests[0]}')
print(f'你想来吃饭吗？{guests[1]}')
del guests[0]
del guests[0]
print(guests)
print('---')

