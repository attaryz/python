# iterate over items in a list
cities = ['new york', 'mountain view', 'chicago', 'los angeles']

for city in cities:
    print(city.title())

# iterate over characters in a string 
for item in 'Python':
# output is p y t h o n
    print(item)

# iterate over numbers in (range) function
# (range) stars from 0 index
for number in range(10):
# output is from 0 to 9
    print(number)

# iterate numbers in (range) between 10 to 15 
for num in range(10, 15):
    print(num)

# (range) can take an optional parameter 
for step in range(1, 10, 2):
# output is 1 3 5 7 9
    print(step)


# calculate the sum of items in a list
prices = [10, 29, 35, 12]
total = 0
for price in prices:
    total += price
# output is 86
print(f'Total: {total}')

