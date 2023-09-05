# step1

import random
from hangman_word import word_list
from hangman_art import logo, stages

print(f"\nInstructions:\nYou have 10 Lives to guess correct word! \nHope You will Enjoy Playing. ")

# word_list = ["hangman", "apple", "programming", "peoaple","beea","amississippi"]
# word_list = ['hangman', 'apple', 'programming', 'people', 'bee', 'mississippi']

# choosen_word = random.choice(hangman_word.word_list)
choosen_word = random.choice(word_list)
word_length = len(choosen_word)
ending = False
display = []
lives = 9

print(logo)
for _ in range(word_length):
  display += "_"
print(f"Pssst, the solution is {choosen_word}")

while not ending:
  user_guess = input("Enter a letter to guess: ").lower()

  if user_guess in display:
    print(f"Awww! you have already enter {user_guess}")

  # watch FOR IN loop and String working with for loop:

  for position in range(word_length):
    letter = choosen_word[position]
    if letter == user_guess:
      display[position] = user_guess

  # print(display)
  # converting following into string's
  print(f"{' '.join(display)}")
  
  
  

  if user_guess not in choosen_word:
    print(f"\nOop! You loose a point, {user_guess} letter isn't in a word ")
    
    lives -= 1
    if lives == 0:
      ending = True
      print("Game Over!")

  if "_" not in display:
    ending = True
    print(f"You Win!\nword is {choosen_word}")

  pic = stages[lives]
  print(pic)
