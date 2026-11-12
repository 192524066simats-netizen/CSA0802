readings = [-3, -1, 0, 2, 9, 55, -60]

# Clean readings using a loop
valid = []
for t in readings:
    if -50 <= t <= 50:
        valid.append(t)
print("Valid:", valid)

# List comprehension
clean = [t for t in readings if -50 <= t <= 50]
print("Clean:", clean)

# Celsius to Fahrenheit using map
fahrenheit = list(map(lambda c: c * 9/5 + 32, clean))
print("Fahrenheit:", fahrenheit)

# Find alarm readings using filter
alarm = list(filter(lambda t: t < -2 or t > 8, clean))
print("Alarm:", alarm)

# Find alarm minutes using enumerate
for minute, temp in enumerate(clean, start=1):
    if temp < -2 or temp > 8:
        print("Alarm Minute:", minute)
