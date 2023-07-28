def translate(phrase):
    translation = " " #an empty string
    for letter in phrase: #checking each letter the user will pass as a phrase
        if letter.lower() in "aeiou":
            if letter.isupper():
             translation = translation + "G"#converting the letter into the "g"

            else:
             translation = translation + "g"

        else:
            translation = translation + letter
    return translation


print(translate(input("Input a phrase:")))
