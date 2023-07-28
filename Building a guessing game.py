#we will specify a secret word stored inside our program, user will interact with program and will try to guess the secret word

secret_word = "cat"
guess = ""
guess_count =0
#we need to be able to prompt the user to input the secret
guess_limit =3
out_of_guesses = False

while guess !=secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guessses , You LOSE!")
else:
    print("You WIN!!!")