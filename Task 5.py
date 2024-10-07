from english_words import get_english_words_set
dictionary = get_english_words_set(['web2'], lower=True, alpha=True)
running = True

print("This only works if the first word of the encrypted sentence is in English and if there are spaces between words")

def ROT_NUMBER():
    ROT=""
    while ROT.isnumeric()==False:
        ROT=str(input("What ROT do you want to encrypt with?"))
        try:
            int(ROT)
        except:
            ROT=""
    return int(ROT)

def ENCRYPT_SENTENCE(ROT):
    encrypted_sentence=""
    sentence_to_encrypt = str(input("Enter a sentence to be put through a Ceaser cipher"))
    sentence_to_encrypt=sentence_to_encrypt.lower()
    for letter in sentence_to_encrypt:
        if ord(letter)>=97 and ord(letter)<=122:
            if ord(letter) + ROT >122:
                new_letter = (ord(letter)+ROT-26)
            else:
                new_letter = (ord(letter)+ROT)
        else:
            new_letter = ord(letter)
        encrypted_sentence += chr(new_letter)
    return str(encrypted_sentence)

def DECRYPT_SENTENCE(dictionary):
    first_word =""
    new_word = ""
    decrypted_sentence=""
    sentence_to_decrypt = str(input("Enter a sentence to be decrypted"))
    sentence_to_decrypt = sentence_to_decrypt.lower()
    attempts = 0
    i = ""
    count=0
    while i != " ":
        i = sentence_to_decrypt[int(count)]
        if i != " ":
            first_word += i
            count+=1
    match=False
    while match==False: 
        n_letter_words=[word for word in dictionary if len(word) == count]
        print("looking for match")
        if first_word in n_letter_words:
            match = True
            print("match found")
        if match == False:
            print("attempt "+str(attempts)+" failed")
            attempts+=1
            for letter in first_word:
                if ord(letter)>=97 and ord(letter)<=122:
                    if ord(letter) + 1 >122:
                        new_letter = (ord(letter)+1-26)
                    else:
                        new_letter = (ord(letter)+1)
                else:
                    new_letter = ord(letter)
                new_word += chr(new_letter)
        first_word = new_word
        new_word=""
    if match == True:
        for letter in sentence_to_decrypt:
            if ord(letter)>=97 and ord(letter)<=122:
                if ord(letter) + attempts >122:
                    new_letter = (ord(letter)+attempts-26)
                else:
                    new_letter = (ord(letter)+attempts)
            else:
                new_letter = ord(letter)
            decrypted_sentence += chr(new_letter)
    return str(decrypted_sentence)
        


while running == True:
    choice=""
    while choice != "d" and choice != "e":
        choice=str(input('To decrypt, input "d".\nTo encrypt, input "e"'))
    if choice =="e":
        rot=ROT_NUMBER()
        sentence = ENCRYPT_SENTENCE(rot)
        print("The encrypted sentence is "+ sentence)
    if choice == "d":
        sentence = DECRYPT_SENTENCE(dictionary)
        print("The decrypted sentence is "+ sentence)
    repeat = str(input('Input "y" to repeat, input anything else to quit'))
    if repeat != "y":
        running = False
quit()
        
