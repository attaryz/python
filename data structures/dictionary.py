# dictionaries can be used to store key value pairs
elements = {'hydrogen': {'number': 1},
                        'weight': 1.00794,
                        'symbol': 'H',
            'helium': {'number': 2,
                        'weight': 4.002602,
                        'symbol': 'He'}}
# to access a key you use [] with the name of the key
# keys are case sensitive
print(elements['helium']['weight'])

customer = {
    'name': 'John Doe',
    'age': 50,
    'is_verified': True
}
print(customer['name'])
# modify an existing value
customer['name'] = 'John John'
print(customer['name'])
# add a new key value pair to dictionary 
customer['job_title'] = 'Doctor'
print(customer)
