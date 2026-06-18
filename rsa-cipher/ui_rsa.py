import tkinter as tk
from tkinter import messagebox
from rsa import generate_keys, encrypt_rsa, decrypt_rsa

class RSAUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Cipher - Mã hóa & Giải mã")
        self.root.geometry("750x650")
        
        # Title
        title_frame = tk.Frame(root)
        title_frame.pack(fill='x', padx=10, pady=10)
        title_label = tk.Label(title_frame, text="RSA CIPHER", 
                              font=('Arial', 24, 'bold'))
        title_label.pack(pady=15)
        
        # Keys Frame
        keys_frame = tk.Frame(root)
        keys_frame.pack(pady=10, padx=20)
        
        tk.Label(keys_frame, text="Public Key (e, n):", font=('Arial', 11)).grid(row=0, column=0, padx=5, sticky='w')
        self.public_key_display = tk.Entry(keys_frame, width=40, font=('Arial', 11))
        self.public_key_display.grid(row=0, column=1, padx=5)
        
        tk.Label(keys_frame, text="Private Key (d, n):", font=('Arial', 11)).grid(row=1, column=0, padx=5, sticky='w')
        self.private_key_display = tk.Entry(keys_frame, width=40, font=('Arial', 11))
        self.private_key_display.grid(row=1, column=1, padx=5)
        
        # Generate Keys Button
        self.gen_keys_btn = tk.Button(root, text="🔑 Tạo khóa mới", 
                                     command=self.generate_new_keys,
                                     font=('Arial', 11, 'bold'),
                                     bg='#4CAF50', fg='white',
                                     width=20, height=2)
        self.gen_keys_btn.pack(pady=10)
        
        # Text input
        text_frame = tk.Frame(root)
        text_frame.pack(pady=10, padx=20)
        
        tk.Label(text_frame, text="Văn bản:", font=('Arial', 12)).grid(row=0, column=0, padx=5, sticky='n')
        self.text_input = tk.Text(text_frame, width=50, height=4, font=('Arial', 11))
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
        self.result_output = tk.Text(result_frame, width=50, height=6, font=('Arial', 11))
        self.result_output.grid(row=0, column=1, padx=5)
        
        # Generate keys on startup
        self.generate_new_keys()
    
    def generate_new_keys(self):
        try:
            self.public_key, self.private_key = generate_keys()
            self.public_key_display.delete(0, tk.END)
            self.public_key_display.insert(0, f"e={self.public_key[0]}, n={self.public_key[1]}")
            self.private_key_display.delete(0, tk.END)
            self.private_key_display.insert(0, f"d={self.private_key[0]}, n={self.private_key[1]}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo khóa: {str(e)}")
    
    def encrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản!")
            return
        
        try:
            cipher = encrypt_rsa(text, self.public_key)
            self.result_output.delete("1.0", tk.END)
            self.result_output.insert(tk.END, " ".join(map(str, cipher)))
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
    
    def decrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản mã hóa!")
            return
        
        try:
            cipher_numbers = [int(x) for x in text.split()]
            plain = decrypt_rsa(cipher_numbers, self.private_key)
            self.result_output.delete("1.0", tk.END)
            self.result_output.insert(tk.END, plain)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
    
    def clear_all(self):
        self.text_input.delete("1.0", tk.END)
        self.result_output.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RSAUI(root)
    root.mainloop()