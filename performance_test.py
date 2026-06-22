import time

numbers = list(range(1000000))

start = time.time()

result = []

for i in numbers:
    if i % 2 == 0:
        result.append(i * i)

original_time = time.time() - start

start = time.time()

result = [
    i * i
    for i in numbers
    if i % 2 == 0
]

refactored_time = time.time() - start

print("Original Time:", original_time)
print("Refactored Time:", refactored_time)
