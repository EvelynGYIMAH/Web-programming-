# Ask for user's name
user_name = input('What is your name? ')
print("Hello, " + user_name + ", welcome to the class.")

# If/else conditional statement
try:
    age = int(input("How old are you? "))
except ValueError:
    print("Please enter a valid number for age.")
    age = 0
if age < 18:
    print(user_name + ", you are a minor.")
else:
    print(user_name + ", you are allowed.")
    print("Let's go!")

# Student score grading
try:
    student_score = int(input("What is your score? "))
except ValueError:
    print("Please enter a valid number for score.")
    student_score = 0
if student_score >= 70:
    print("You got an A!")
elif student_score >= 68:
    print("You got a B!")
elif student_score >= 58:
    print("You got a C!")
elif student_score >= 48:
    print("You got a D!")
elif student_score >= 40:
    print("You have failed! Sorry!!")
else:
    print("Score too low to be graded.")

# List of student scores
student_scores = [12, 40, 58, 68, 70]
print("Student scores:", student_scores)

# Function to grade a score
def grade_score(score):
    if score >= 70:
        return "A"
    elif score >= 68:
        return "B"
    elif score >= 58:
        return "C"
    elif score >= 48:
        return "D"
    elif score >= 40:
        return "Fail"
    else:
        return "Too low to be graded"

# Loop through the list and print grades
for score in student_scores:
    print(f"Score: {score} - Grade: {grade_score(score)}")

password =234
correct_password = 189
while password != "correct_password":
    password = input("invalid password,please try again: ")
print("password accepted,welcome to the system")