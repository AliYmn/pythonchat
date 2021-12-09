class Ceaser:
    def __init__(self,pw1,pw2):
        self.key_val = pw1+pw2

    def Encryption(self,plaintext):
        ciphertext = ''
        for i in range(len(plaintext)):
            special = plaintext[i]
            new_special = special.lower()
            if new_special == " ":
                ciphertext += ' '
            elif special.isalpha():
                ciphertext += chr((ord(new_special) + self.key_val - 97) % 26 + 97)

        return ciphertext


    def Decryption(self, ciphertext):
        plaintext = ''
        for i in range(len(ciphertext)):
            special = ciphertext[i]
            new_special = special.lower()
            if new_special == " ":
                plaintext += ' '
            elif special.isalpha():
                plaintext += chr((ord(new_special) - self.key_val - 97) % 26 + 97)
        return plaintext
