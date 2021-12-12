class Caesar:
    def __init__(self,pw1,pw2):
        self.key_val = pw1+pw2

    def Encryption(self,plaintext):
        ciphertext = '' # define string for strings
        numbers = '' # define string for numbers
        for i in range(len(plaintext)): # loop text count
            special = plaintext[i] # each character
            new_special = special.lower() # to lower
            if new_special == " ": # space check
                ciphertext += ' '
            if special.isdigit(): # if is numeric
                numbers += str(special)
            elif special.isalpha(): # if is alpha
                # x+n mod 26
                ciphertext += chr((ord(new_special) + self.key_val - 97) % 26 + 97)
        return ciphertext+numbers


    def Decryption(self, ciphertext):
        plaintext = '' # define string
        numbers = '' # define string for numbers
        for i in range(len(ciphertext)): # loop text count
            special = ciphertext[i] # each character
            new_special = special.lower() # to lower
            if new_special == " ": # space check
                plaintext += ' '
            if special.isdigit(): # if is numeric
                numbers += str(special)
            elif special.isalpha():# if is alpha
                # x-n mod 26
                plaintext += chr((ord(new_special) - self.key_val - 97) % 26 + 97)
        return plaintext+numbers

if __name__ == '__main__':
    user1 = 25 # pw1
    user2 = 35 # pw2
    cs = Caesar(user1, user2) # call class
    text = "End to end Encrypted Secure Python Chat 2021 2020" # define text
    print(cs.Encryption(text)) # encryt
    print(cs.Decryption(cs.Encryption(text))) # decryt