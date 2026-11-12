rainfall = [10, 20, 0, 15, 25, 5, 0,
            12, 18, 10, 0, 20, 15, 5]

# Weekly totals
for i in range(0, len(rainfall), 7):
    week = rainfall[i:i+7]
    print("Weekly Total:", sum(week))

# Maximum and minimum
print("Maximum:", max(rainfall))
print("Minimum:", min(rainfall))

# 7-day moving average
for i in range(len(rainfall)-6):
    avg = sum(rainfall[i:i+7]) / 7
    print("Moving Average:", round(avg, 2))

# Dry days
dry_days = [i+1 for i in range(len(rainfall))
            if rainfall[i] == 0]
print("Dry Days:", dry_days)
