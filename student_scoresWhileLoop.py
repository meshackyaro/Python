student_score = int(input("Enter score enter -1 stop: "))
student_score = 0
failed = 0
passed = 0
passmark = 45

while student_score != -1:

	if student_score >= 45:
		passed += 1
		student_score += 1
	if student_score <= 45:
		failed += 1
	student_score = int(input("Enter score enter -1 stop: "))		

print("The number of students who pass: ", passed)
print("The number of students who failed: ", failed)

