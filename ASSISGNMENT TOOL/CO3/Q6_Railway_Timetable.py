trains = {
    101: {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Salem", "11:00", "11:05"),
            ("Coimbatore", "13:00", "13:10")
        ],
        "days": {"Monday", "Tuesday", "Wednesday"}
    },
    102: {
        "name": "Pandian Express",
        "stops": [
            ("Chennai", "09:00", "09:15"),
            ("Salem", "12:00", "12:05"),
            ("Madurai", "15:00", "15:10")
        ],
        "days": {"Monday", "Friday", "Sunday"}
    },
    103: {
        "name": "Kovai Express",
        "stops": [
            ("Chennai", "10:00", "10:10"),
            ("Salem", "12:30", "12:35"),
            ("Coimbatore", "15:00", "15:10")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    }
}

station = "Salem"
day = "Monday"
result = []

# Find trains stopping at the selected station on the selected day
for number, details in trains.items():
    if day in details["days"]:
        for stop in details["stops"]:
            if stop[0] == station:
                result.append(
                    (number, details["name"], stop[1], stop[2])
                )

# Sort by departure time
result.sort(key=lambda x: x[3])

print("Station:", station)
print("Day:", day)
for train in result:
    print(train)
