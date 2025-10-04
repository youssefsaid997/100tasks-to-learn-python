alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(encrypt_word,shift_amount):
    lower_case_word = str.lower(encrypt_word)
    word_list = []
    print(lower_case_word)
    for char in lower_case_word:
        char_index = alphabets.index(char)
        shifted_position = char_index + shift_amount
        print(f"char {char} , shifted position {shifted_position}")
        word_list.append(alphabets[shifted_position])
    encrypted_word = ''.join(word_list)
    print(f"word-before: {encrypt_word} , word after shifting: {encrypted_word}")


# we need to swap letters
# alphabets from a to z 
# the shift position means if a -> 1 then you add 3 so a will become 1+3 = 4-> d
# [a,h,m,e,d] 
# how we can do so 
# first we need to list 

encrypt(shift_amount=3 , encrypt_word="Ahmed")