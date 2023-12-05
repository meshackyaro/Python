student_scores = int(input("Enter score: "))
score = 0
failed = 0
passed = 0
passmark = 45

while score != -1:
	if score >= 45:
		passed += 1
	if score <= 45:
		failed += 1
print("The number of students who pass: ", passed)
print("The number of students who failed: ", failed)

