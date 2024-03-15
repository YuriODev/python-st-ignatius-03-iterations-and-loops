# Prompt the user to enter the number of subjects
n = int(input("Enter the number of subjects: "))

# Initialize a variable to store the total grade
total = 0

# Iterate 'n' times to get the grades for each subject
for _ in range(n):
    # Prompt the user to enter the grade for each subject
    grade = int(input("Enter the grade: "))
    
    # Add the grade to the total
    total += grade

# Calculate the average grade by dividing the total by the number of subjects
average = total / n

# Print the average grade with two decimal places
print(f"The average grade is: {average:.2f}")
