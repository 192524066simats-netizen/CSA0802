import copy

rows = 3
cols = 3

# Aliasing problem
bad = [[0] * cols] * rows
bad[0][1] = 7
print("Bad:", bad)

# Correct grid
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7
print("Good:", good)

# Shallow and deep copy
a = [[1, 2], [3, 4]]
shallow = a.copy()
deep = copy.deepcopy(a)
a[0][0] = 9

print("Original:", a)
print("Shallow:", shallow)
print("Deep:", deep)

# Tuple as dictionary key
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}
print(stops[(13.0418, 80.2341)])
