import random

# choices = [rock, paper, scissors]
user_choice = int(input('Think at the possible number combination using the fingers of two hands.\nCould be between 0 and 10. You virtually use one hand and the computer the other\n'))
if user_choice >= 11:
  print("You type and invalid numer, you loose!")
user_bid = int(input("Choose a number between 1 and 5\n"))
if user_bid >= 6:
  print("You type and invalid numer, you loose!")

computer_choice = random.randint(0,10)
print(f'Total guessed by the computer...\n{computer_choice}')
computer_bid = random.randint(0, 5)
print(f'Computer choose...\n{computer_bid}')

total = user_bid + computer_bid
print(f"Total is {total}")
# print(choices[computer_choice])


if total == user_choice:
  print("You win!")
elif total == computer_choice:
  print("Computer win!")
else:
  print("No one win. Try again!")
