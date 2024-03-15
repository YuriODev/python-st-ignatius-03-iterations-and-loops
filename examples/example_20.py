# Prompt the user to enter the number of participants
n = int(input("Enter the number of participants: "))

# Initialize the maximum score to 0
max_score = 0

# Flag to indicate if any participant failed the quiz
failed_quiz = False

# Iterate over the range of participants
for _ in range(n):
    # Prompt the user to enter the score for each participant
    score = int(input("Enter the score: "))

    # Check if the current score is greater than the maximum score
    if score > max_score:
        max_score = score

    # Check if the current score is 0, indicating a failed quiz
    elif score == 0:
        failed_quiz = True

# Print the maximum score achieved
print(max_score)

# Print "Yes" if any participant failed the quiz, otherwise print "No"
print("Yes" if failed_quiz else "No")
