ai_elective = {
    "192311001", "192311004",
    "192311007", "192311009"
}

iot_elective = {
    "192311002", "192311004",
    "192311009", "192311010"
}

all_students = {
    f"192311{i:03d}" for i in range(1, 11)
}

# Students in both electives
both = ai_elective & iot_elective

# Students in exactly one elective
exactly_one = ai_elective ^ iot_elective

# Students in neither elective
neither = all_students - (ai_elective | iot_elective)

print("Clash:", sorted(both))
print("Exactly One:", sorted(exactly_one))
print("Neither:", sorted(neither))
