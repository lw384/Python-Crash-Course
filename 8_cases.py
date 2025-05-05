# 8.3
def make_shirt(size = 'L',text = 'I love python'):
    """desciibe a shit"""
    print(f'The shirt is {size} size,and {text} on it')

make_shirt('M','GOOD')
make_shirt(size = 'M',text ='GOOD')

# 8.4
make_shirt()
make_shirt('S','I LOVE YOU')

# 8.5
def describe_city(city,country = 'China'):
    """describe city and country"""
    print(f'{city} is in {country}')
describe_city('Beijing')
describe_city('Coventry','UK')
describe_city('NewYork','US')

# 8.6
def city_coutry(city,country):
    """return city and country"""
    city =  f"{city.title()}, {country.title()}"
    return city
print(city_coutry('Beijng','China'))

#8.7
def make_album(artist_name,album_title):
    """return dict"""
    dict = {'artist': artist_name,'album': album_title}
    return dict
print(make_album('Lily','album one'))
print(make_album('Bob','album two'))

# 8.8
# while True:
#     print('8.8 Please input message, enter "q" at any time to quit')
#     artist = input("Artist name: ")
#     if artist == 'q':
#         break
#     album = input('Album title: ')
#     if album == 'q':
#         break
#     if album and artist:
#         print( make_album(artist,album))
#         break
# 8.9
def show_message(messages):
    """show message from list"""
    for value in messages:
        print(value)

list1 = {'a','aa','aaa'}
show_message(list1)

#8.10

def send_message(messages,sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
list2 = ['1','2','3']
sent_mesaages = []
send_message(list2,sent_mesaages)
print(list2,sent_mesaages)

#8.11
list3 = ['1','2','3']
send_message(list3[:],sent_mesaages)
print(list3,sent_mesaages)

# 8.12
def order_sandwish(*toppings):
    for value in toppings:
        print(value)

order_sandwish('apple','organe','blue')

# 8.14
def make_car(manufaturer, model, **info):
    info['manufaturer'] = manufaturer
    info['model'] = model
    return info

car = make_car('subaru','outback',color = 'blue',two_package = True)
print(car)