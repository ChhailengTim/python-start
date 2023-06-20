try:
    age = int(input("Age: "))
    print(age)
    income = 2000
    risk = income / age

except ZeroDivisionError:
    print("Division by zero NO")
except ValueError:
    print("Accept only number")