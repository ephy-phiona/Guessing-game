import random
 
name = input("What is your name? ")
 
print("Good Luck ! ", name)
 
words = ['Nairobi', 'Kajiado', 'Kakamega', 'Nakuru',
         'Naivasha', 'Limuru', 'Kiambu', 'Mombasa',
         'Taita', 'Busia', 'Migori', 'Kisumu','Kitui'
         'Nyali','Lamu','Kisii','Siaya']

word = random.choice(words)
 
 
print("Guess the characters")
 
guesses = ''
 
turns = 12
 
 
while turns > 0:
     
    failed = 0
     
    for char in word:
         
        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end=" ")
             
        else:
            print("_")
            print(char, end=" ")
             
        
            failed += 1
             
 
    if failed == 0:
        
        print("You Win")
         
        print("The word is: ", word)
        break
     
    print()
    guess = input("guess a character:")
     
    guesses += guess
     
    if guess not in word:
         
        turns -= 1
         
        print("Wrong")
         
        print("You have", + turns, 'more guesses')
         
        if turns == 0:
            print("You Loose")
