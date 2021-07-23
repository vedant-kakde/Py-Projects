import random

words=['facebook', 'amazon', 'apple', 'microsoft', 'netflix', 'google']

#choose random words from the list
guessed_word = random.choice(words)
guessed_word

hint=guessed_word[0]+guessed_word[-1]
hint

store_g_l=[]
try_p=6
a=input('Enter Your Name')
print('Welcome to the Game world', a)
print('You have 6 attempts to guess the word.')

for guess in range(try_p):
 while True:
  letter = input('Guess the letter')

  if len(letter) == 1:
   break
  else:
   print("Oops! Please guess a letter")

 if letter in guessed_word:
  print('yes!')
  store_g_l.append(letter)
 else:
  print('no!')

 if guess == 3:
  print()
  clue_request = input('Would you like a clue?')
  if clue_request.lower().startswith('y'):
   print()
   print('CLUE: The first and last letter of the word is: ', hint)
   
