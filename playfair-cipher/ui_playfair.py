import tkinter as tk
from tkinter import messagebox
from playfair import PlayfairCipher

class PlayfairUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Playfair Cipher - Mã hóa & Giải mã")
        self.root.geometry("700x600")
        
        # Title
        title_frame = tk.Frame(root)
        title_frame.pack(fill='x', padx=10, pady=10)
        title_label = tk.Label(title_frame, text="PLAYFAIR CIPHER", 
                              font=('Arial', 24, 'bold'))
        title_label.pack(pady=15)
        
        # Key input
        key_frame = tk.Frame(root)
        key_frame.pack(pady=10, padx=20)
        tk.Label(key_frame, text="Khóa (Key):", font=('Arial', 12)).grid(row=0, column=0, padx=5)
        self.key_entry = tk.Entry(key_frame, width=40, font=('Arial', 12))
        self.key_entry.grid(row=0, column=1, padx=5)
        
        # Text input
        text_frame = tk.Frame(root)
        text_frame.pack(pady=10, padx=20)
        tk.Label(text_frame, text="Văn bản:", font=('Arial', 12)).grid(row=0, column=0, padx=5, sticky='n')
        self.text_input = tk.Text(text_frame, width=50, height=5, font=('Arial', 11))
        self.text_input.grid(row=0, column=1, padx=5)
        
        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)
        
        self.encrypt_btn = tk.Button(btn_frame, text="Mã hóa", 
                                    command=self.encrypt_text, 
                                    font=('Arial', 11, 'bold'),
                                    width=15, height=2)
        self.encrypt_btn.grid(row=0, column=0, padx=10)
        
        self.decrypt_btn = tk.Button(btn_frame, text="Giải mã", 
                                    command=self.decrypt_text, 
                                    font=('Arial', 11, 'bold'),
                                    width=15, height=2)
        self.decrypt_btn.grid(row=0, column=1, padx=10)
        
        self.clear_btn = tk.Button(btn_frame, text="Xóa", 
                                  command=self.clear_all, 
                                  font=('Arial', 11),
                                  width=10)
        self.clear_btn.grid(row=0, column=2, padx=10)
        
        # Result
        result_frame = tk.Frame(root)
        result_frame.pack(pady=10, padx=20, fill='both', expand=True)
        tk.Label(result_frame, text="Kết quả:", font=('Arial', 12)).grid(row=0, column=0, padx=5, sticky='n')
        self.result_output = tk.Text(result_frame, width=50, height=8, font=('Arial', 11))
        self.result_output.grid(row=0, column=1, padx=5)
        
        # Matrix display
        matrix_frame = tk.Frame(root)
        matrix_frame.pack(pady=10, padx=20)
        tk.Label(matrix_frame, text="Ma trận khóa:", font=('Arial', 12, 'bold')).pack()
        self.matrix_display = tk.Text(matrix_frame, width=30, height=6, font=('Courier', 12))
        self.matrix_display.pack(pady=5)
    
    def encrypt_text(self):
        key = self.key_entry.get().strip()
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not key or not text:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập khóa và văn bản!")
            return
        
        try:
            cipher = PlayfairCipher(key)
            result = cipher.encrypt(text)
            self.result_output.delete("1.0", tk.END)
            self.result_output.insert(tk.END, result)
            self.display_matrix(cipher)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
    
    def decrypt_text(self):
        key = self.key_entry.get().strip()
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not key or not text:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập khóa và văn bản!")
            return
        
        try:
            cipher = PlayfairCipher(key)
            result = cipher.decrypt(text)
            self.result_output.delete("1.0", tk.END)
            self.result_output.insert(tk.END, result)
            self.display_matrix(cipher)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
    
    def display_matrix(self, cipher):
        self.matrix_display.delete("1.0", tk.END)
        matrix_str = ""
        for row in cipher.matrix:
            matrix_str += " ".join(row) + "\n"
        self.matrix_display.insert(tk.END, matrix_str)
    
    def clear_all(self):
        self.key_entry.delete(0, tk.END)
        self.text_input.delete("1.0", tk.END)
        self.result_output.delete("1.0", tk.END)
        self.matrix_display.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayfairUI(root)
    root.mainloop()