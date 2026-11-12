calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

stop = {"not", "high"}
frequency = {}
group = {}
districts = ["Chennai", "Madurai", "Chennai"]

# Count word frequency
for complaint in calls:
    for word in complaint.split():
        if word not in stop:
            frequency[word] = frequency.get(word, 0) + 1

# Group complaints by district
for i in range(len(calls)):
    group.setdefault(districts[i], []).append(calls[i])

# Find top three words
top = sorted(frequency.items(),
             key=lambda x: (-x[1], x[0]))[:3]

print("Frequency:", frequency)
print("District:", group)
print("Top Words:", top)
