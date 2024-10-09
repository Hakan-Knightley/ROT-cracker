from english_words import get_english_words_set
dictionary = get_english_words_set(['web2'], lower=True, alpha=True)
running = True




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
    temp_word=""
    encrypted_sentence=""
    sentence_to_encrypt = str(input("Enter a sentence to be put through a Ceaser cipher"))
    sentence_to_encrypt=sentence_to_encrypt.lower()
    for letter in sentence_to_encrypt:
        if ord(letter)>=97 and ord(letter)<=122:
            temp_word = temp_word+letter
    sentence_to_encrypt=temp_word
    temp_word=""

    for letter in sentence_to_encrypt:
        
        if ord(letter) + ROT >122:
            new_letter = (ord(letter)+ROT-26)
        else:
            new_letter = (ord(letter)+ROT)
        encrypted_sentence += chr(new_letter)
    return str(encrypted_sentence)

def DECRYPT_SENTENCE(dictionary):
    decrypted_sentence = ""
    match = False
    count = 0
    word_to_test = ""
    temp_word=""
    
    encrypted_sentence = str(input("Enter the encrypted sentence"))
    encrypted_sentence = encrypted_sentence.lower()
    for letter in encrypted_sentence:
        if ord(letter)>=97 and ord(letter)<=122:
            temp_word = temp_word+letter
    encrypted_sentence=temp_word
    temp_word = ""
    characters = len(encrypted_sentence)
    while match == False:

        attempts = 0
    
        for i in range(0,characters):
            temp_word += encrypted_sentence[i]
        word_to_test = temp_word
        temp_word = ""




        
        if word_to_test in dictionary:
            match = True
            print("match found")
        elif word_to_test == "" or word_to_test == " ":
            print("No match found")
            quit()
            
        else:
            
            count=0
            while count <= 25:
                for letter in word_to_test:
                    if ord(letter)>=97 and ord(letter)<=122:
                        if ord(letter) + 1 >122:
                            new_letter = (ord(letter)+1-26)
                        else:
                            new_letter = (ord(letter)+1)
                    else:
                        new_letter = ord(letter)
                        
                    temp_word += chr(new_letter)
                word_to_test = temp_word
                temp_word=""
                #print(word_to_test)
                attempts=attempts+1
                #print(str(attempts))
                if word_to_test in dictionary:
                    match = True
                    count=25
                    
                count +=1
            characters = characters - 1
            
    for letter in encrypted_sentence:
        if ord(letter) + attempts >122:
            new_letter = ord(letter)+attempts-26
        else:
            new_letter = ord(letter)+attempts
        
        decrypted_sentence = decrypted_sentence + chr(new_letter)
    print("The ROT used is "+str(26-attempts))




    
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
        print("This only works if the first combination of letters in the unencrypted sentence makes an English word")
        sentence = DECRYPT_SENTENCE(dictionary)
        print("The decrypted sentence is "+ sentence)
    repeat = str(input('Input "y" to repeat, input anything else to quit'))
    if repeat != "y":
        running = False
quit()
        
