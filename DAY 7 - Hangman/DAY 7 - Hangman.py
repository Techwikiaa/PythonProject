# step1
word_list = ["hangman", "apple", "programming", "peoaple","beea","amississippi"]

import random

choosen_word = random.choice(word_list)
word_length = len(choosen_word)
ending = False
display = []
lives = 6
for _ in range(word_length):
  display += "_"
  
while not ending:
  user_guess = input("Enter a letter to guess: ").lower()
  
  for position in range(word_length):
    letter = choosen_word[position]
    if letter == user_guess:
      display[position] += user_guess
      
  print (display)
  if user_guess not in choosen_word:
    lives -= 1
    if lives == 0:
      ending = True
      print(f"Game Over! \n Word is {choosen_word}")

  if "_" not in display:
    ending = True
    print(f"You Win!\nWord is {choosen_word}")
