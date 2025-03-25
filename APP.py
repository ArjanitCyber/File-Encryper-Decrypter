import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Generate or load encryption key       
KEY_FILE = "secret.key"
def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

encryption_key = load_key()
cipher = Fernet(encryption_key)

class FileEncryptorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("File Encryptor & Decryptor")
        self.geometry("500x450")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.filepath = ""

        self.label = ctk.CTkLabel(self, text="Zgjidh një fajll", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.btn_select = ctk.CTkButton(self, text="Zgjidh Fajll", command=self.select_file)
        self.btn_select.pack(pady=5)

        self.btn_encrypt = ctk.CTkButton(self, text="Enkripto Fajllin", command=self.encrypt_file)
        self.btn_encrypt.pack(pady=5)

        self.btn_decrypt = ctk.CTkButton(self, text="Dekripto Fajllin", command=self.decrypt_file)
        self.btn_decrypt.pack(pady=5)

        self.label_key = ctk.CTkLabel(self, text=f"Çelësi aktual: {encryption_key.decode()[:45]}", font=("Arial", 12))
        self.label_key.pack(pady=10)

        self.entry_key = ctk.CTkEntry(self, width=350)
        self.entry_key.insert(0, encryption_key.decode())
        self.entry_key.pack(pady=5)

        self.btn_set_key = ctk.CTkButton(self, text="Vendos Çelësin", command=self.set_manual_key)
        self.btn_set_key.pack(pady=5)

    def select_file(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath:
            self.label.configure(text=f"Fajlli: {os.path.basename(self.filepath)}")

    def encrypt_file(self):
        if not self.filepath:
            messagebox.showerror("Gabim", "Zgjidh një fajll!")
            return
        with open(self.filepath, "rb") as file:
            file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(self.filepath, "wb") as file:
            file.write(encrypted_data)
        messagebox.showinfo("Sukses", "Fajlli u enkriptua me sukses!")

    def decrypt_file(self):
        if not self.filepath:
            messagebox.showerror("Gabim", "Zgjidh një fajll të enkriptuar!")
            return
        with open(self.filepath, "rb") as file:
            encrypted_data = file.read()
        try:
            decrypted_data = cipher.decrypt(encrypted_data)
        except:
            messagebox.showerror("Gabim", "Fajlli nuk mund të dekriptohet!")
            return
        with open(self.filepath, "wb") as file:
            file.write(decrypted_data)
        messagebox.showinfo("Sukses", "Fajlli u dekriptua me sukses!")

    def set_manual_key(self):
        global encryption_key, cipher
        new_key = self.entry_key.get().strip()
        if len(new_key) == 44:
            encryption_key = new_key.encode()
            cipher = Fernet(encryption_key)
            with open(KEY_FILE, "wb") as key_file:
                key_file.write(encryption_key)
            messagebox.showinfo("Sukses", "Çelësi u përditësua me sukses!")
        else:
            messagebox.showerror("Gabim", "Çelësi duhet të jetë 44 karaktere i gjatë!")

if __name__ == "__main__":
    app = FileEncryptorApp()
    app.mainloop()