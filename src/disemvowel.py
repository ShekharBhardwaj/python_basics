def disemvowel(word):
    print("The Word is {}".format(word))
    list_word = list(word)
    print("The List Word is {}".format(list_word))
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    for vowel in vowels:
        while vowel in list_word:
            list_word.remove(vowel)
    
    word = ''.join(list_word)
    return word



def print_the_word():
    print(disemvowel(raw_input(">")))
    
    
    
print_the_word()
    