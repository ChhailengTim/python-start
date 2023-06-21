import random

for i in range(3):
    print(random.randint(10, 20))

numbers = ["Leng", "Hong", "Long", "Heng"]
leader = random.choice(numbers)
print(leader)