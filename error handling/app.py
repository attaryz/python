try:
    age = int(input('Age:'))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid Input')
except ZeroDivisionError:
    print('Age cannot be 0')