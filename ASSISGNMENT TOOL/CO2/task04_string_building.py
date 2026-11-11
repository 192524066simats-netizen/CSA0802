# Q4 - String Building: + vs join()

import time

items = ["Customer " + str(i) for i in range(10000)]

start = time.time()
text = ""
for item in items:
    text += item + "\\n"
plus_time = time.time() - start

start = time.time()
result = "\\n".join(items) + "\\n"
join_time = time.time() - start

print("Plus Time:", plus_time)
print("Join Time:", join_time)
print("Same Output:", text == result)
