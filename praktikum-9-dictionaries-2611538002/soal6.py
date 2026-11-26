schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a: Find the day with the most courses
busiest_day = max(schedule, key=lambda day: len(schedule[day]))
max_courses = len(schedule[busiest_day])
print(f"Busiest day: {busiest_day} ({max_courses} courses)")

# 6b: Count how many days a given course appears
course_name = input().strip()
day_count = sum(1 for courses in schedule.values() if course_name in courses)
print(f"{course_name}: {day_count} days")