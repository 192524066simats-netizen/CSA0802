# Q7 - Diagnose, Redesign and Validate

import time

items = ["Customer " + str(i) + "\\n" for i in range(10000)]

# Original method
start = time.time()
text = ""
for item in items:
    text += item
old_time = time.time() - start

# Improved method
start = time.time()
result = "".join(items)
new_time = time.time() - start

print("Original Time:", old_time)
print("Redesigned Time:", new_time)
print("Same Output:", text == result)

if old_time > new_time:
    improvement = ((old_time - new_time) / old_time) * 100
    print("Improvement:", round(improvement, 2), "%")
else:
    print("No improvement in this run")
