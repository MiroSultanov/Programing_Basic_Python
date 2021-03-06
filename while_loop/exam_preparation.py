# Write a program in which Marin solves exam tasks until he receives an "Enough" message from his lecturer. 
# For each task solved, he receives a grade. The program must end reading data with the "Enough" command or if Marin receives the specified number of unsatisfactory
# grades. Any grade less than or equal to 4 is unsatisfactory.

# Input
# ⦁ In the first row - number of unsatisfactory grades - integer;
# ⦁ Then two lines are read repeatedly:
# ⦁ Task name - text;
# ⦁ Score - an integer in the range [2… 6]

# Output
# ⦁ If Marin reaches the "Enough" command, print in 3 lines:
# ⦁ "Average score:"
# ⦁ "Number of problems: {number of all tasks}"
# ⦁ "Last problem: {name of last task}"
# ⦁ If he receives the specified number of unsatisfactory grades:
# } "You need a break, {number of unsatisfactory grades} poor grades."
# The average score should be formatted to the second decimal place.

max_bad_grades = int(input())
bad_grades = 0
is_expelled = False
total_problems = 0
average_grades = 0
last_problem = " "
current_problem = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades += 1
        if bad_grades == max_bad_grades:
            is_expelled = True
            break
    average_grades += current_grade
    total_problems += 1
    last_problem = current_problem
    current_problem = input()
if is_expelled:
    print(f"You need a break, {max_bad_grades} poor grades.")
else:
    average_grades /= total_problems
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {total_problems}")
    print(f"Last problem: {last_problem}")
