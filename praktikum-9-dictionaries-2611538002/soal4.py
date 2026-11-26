class_list = input().split()
submissions = input().split()

submitted_set = set(submissions)
submitted_count = len(submitted_set)

not_submitted_set = set(class_list) - submitted_set
not_submitted_count = len(not_submitted_set)

print(f"Submitted: {submitted_count} students")
print(f"Not submitted: {not_submitted_count} students")

for student in class_list:
    if student not in submitted_set:
        print(student)