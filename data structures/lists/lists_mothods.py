# append adds items to the end of list
numbers = [1, 5, 3, 8, 20, 5]
numbers.append(30)
print(numbers)

cities = ['Tokyo', 'New york', 'Berlin', 'Paris']
# insert function adds items to the chosen index 
cities.insert(1, 'Dubai')
print(cities)

teams = ['Juventus', 'Chelsea', 'Barcelona', 'Real Madrid']
# remove function removes item from the list
# case sensitive  
teams.remove('Chelsea')
print(teams)

countries = ['Japan', 'China', 'USA', 'France']
# clear function removes all items in list
countries.clear()
print(countries)

currencies = ['Euro', 'Dollar', 'Dollar', 'Pound', 'Riyal']
# pop removes the last item
currencies.pop()
print(currencies)
#index function used to get the index of an item or to check the if the item exists in the list
print(currencies.index('Dollar'))
# check if the item exists in a list
# return a boolean value
print('Yen' in currencies)
# count the number of an item in a list
print(currencies.count('Dollar'))


num = [1, 3, 9, 20, 36, 94, 220]
# sort items in list
num.sort()
# reverse the order of items after using sort function 
num.reverse()
print(num)
names = ['John', 'Sally', 'Leyla', 'Omar']
# sort strings alphabetically
names.sort()
print(names)

ages = [11, 25, 56, 44, 36]
# copy the list
# changes in the original list don't effect the copied list
ages2 = ages.copy()
ages.append(20)
print(ages2)
print(ages)