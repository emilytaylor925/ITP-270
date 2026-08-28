student_name = input("Enter the student's name: ")

def get_grade(assignment_name):
	while True:
		try:
			grade = int(input(f"Enter {assignment_name} grade: "))
			if 0 <= grade <= 100:
				return grade
			print("Grade must be between 0 and 100.")
		except ValueError:
			print("Please enter a number between 0 and 100.")


grade_one = get_grade("assignment 1")
grade_two = get_grade("assignment 2")
grade_three = get_grade("assignment 3")

average = (grade_one + grade_two + grade_three) / 3

print("\nStudent Grade Summary")
print("---------------------")
print(f"Student: {student_name}")
print(f"Assignment Grades: {grade_one}, {grade_two}, {grade_three}")
print(f"Average: {average:.2f}")

if average >= 90:
	message = "Excellent work!"
elif average >= 80:
	message = "Good job!"
elif average >= 70:
	message = "You are passing, but keep working hard."
else:
	message = "You need to improve."

print(f"{message}")


# AI DEVELOPMENT NOTES
#
# One prompt I gave Copilot: Help me create a Python program that asks for a 
# student's name and three assignment grades, calculates the average, 
# and displays a formatted summary. Explain the code you suggest.
#
# One useful suggestion Copilot gave me: Copilot suggested to classify the grades into 
# categories based off the number (ex: 90/80/70 cut off)
#
# One thing I changed or rejected: Copilot started by putting decimals everywhere and i made
# the change to only include decimals in the average. I made it look neater by removing 
# multiple prints of each assignment grade in the summary. I also made copilot adjust so that no one
# could type any numbers other than 0 through 100. for grades.
#
# Why I made that decision: The decimals on every number looked messy.
# I made the change for only allowing some numbers that way a correct grade average would come out.
#
# How I tested the finished program: I used my own name and typed in failing grades, and grades that were 
# outside the range to see if the program would accept them.
# I also tested what the bottom message would say to me each time.