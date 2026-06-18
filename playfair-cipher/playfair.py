class PlayfairCipher:
    def __init__(self, key):
        self.key = key.upper().replace('J', 'I')
        self.matrix = self.create_matrix()
    
    def create_matrix(self):
        key_letters = ""
        for char in self.key:
            if char not in key_letters and char.isalpha():
                key_letters += char
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in key_letters:
                key_letters += char
        
        matrix = []
        for i in range(5):
            row = list(key_letters[i*5:(i+1)*5])
            matrix.append(row)
        return matrix
    
    def find_position(self, char):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j
        return None, None
    
    def prepare_text(self, text):
        text = text.upper().replace('J', 'I').replace(" ", "")
        prepared = ""
        i = 0
        while i < len(text):
            if not text[i].isalpha():
                i += 1
                continue
            prepared += text[i]
            if i + 1 < len(text) and text[i] != text[i + 1] and text[i + 1].isalpha():
                prepared += text[i + 1]
                i += 2
            else:
                prepared += 'X'
                i += 1
        if len(prepared) % 2 != 0:
            prepared += 'X'
        return prepared
    
    def encrypt(self, plaintext):
        text = self.prepare_text(plaintext)
        cipher = ""
        for i in range(0, len(text), 2):
            row1, col1 = self.find_position(text[i])
            row2, col2 = self.find_position(text[i + 1])
            
            if row1 == row2:
                cipher += self.matrix[row1][(col1 + 1) % 5]
                cipher += self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                cipher += self.matrix[(row1 + 1) % 5][col1]
                cipher += self.matrix[(row2 + 1) % 5][col2]
            else:
                cipher += self.matrix[row1][col2]
                cipher += self.matrix[row2][col1]
        return cipher
    
    def decrypt(self, ciphertext):
        text = ciphertext.upper().replace(" ", "")
        plain = ""
        for i in range(0, len(text), 2):
            row1, col1 = self.find_position(text[i])
            row2, col2 = self.find_position(text[i + 1])
            
            if row1 == row2:
                plain += self.matrix[row1][(col1 - 1) % 5]
                plain += self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plain += self.matrix[(row1 - 1) % 5][col1]
                plain += self.matrix[(row2 - 1) % 5][col2]
            else:
                plain += self.matrix[row1][col2]
                plain += self.matrix[row2][col1]
        return plain