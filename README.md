# File Encryptor & Decryptor

## Description
This Python application provides an easy-to-use graphical interface for encrypting and decrypting files. It uses **CustomTkinter** for the UI and **Fernet** encryption from the **cryptography** library to ensure secure file encryption.

## Features
- **File Encryption**: Encrypt any file securely.
- **File Decryption**: Decrypt previously encrypted files.
- **Custom Encryption Key**: Generate or manually set an encryption key.
- **Graphical Interface**: A user-friendly dark-mode UI.

## Encryption & Decryption Method
This application uses **Fernet encryption**, which is part of the **cryptography** library. Fernet is a symmetric encryption method, meaning the same key is used for both **encryption** and **decryption**.

### **How Fernet Encryption Works**  
1. **Key Generation**  
   - The script generates a **256-bit secret key** (Base64 encoded) if it does not exist.  
   - This key is stored in a file named **`secret.key`**.  
   
2. **Encryption Process**  
   - The selected file is read as **binary data**.  
   - The **Fernet cipher** encrypts the data using the secret key.  
   - The **AES-128 in CBC mode** is used internally with **HMAC authentication** to ensure data integrity.  
   - The encrypted content **overwrites the original file**.  

3. **Decryption Process**  
   - The script reads the encrypted file as **binary data**.  
   - Using the same **secret key**, it decrypts the data.  
   - The decrypted content **replaces the encrypted file**.  

### **Security Features of Fernet**  
✔ **AES-128 encryption** in **CBC mode** (Cipher Block Chaining)  
✔ **HMAC (SHA256) authentication** to prevent tampering  
✔ **Time-sensitive encryption tokens** (optional, not used in your script)  

## Requirements
Make sure you have Python installed. Then, install the required dependencies using:

```sh
pip install customtkinter cryptography
```

## Usage
Run the application with:

```sh
python APP.py
```

## Converting to an Executable (.exe)
To convert the script into an executable file, use **PyInstaller**:

1. Install PyInstaller if not already installed:

   ```sh
   pip install pyinstaller
   ```

2. Create an executable with the following command:

   ```sh
   pyinstaller --onefile --windowed APP.py
   ```

3. The executable will be available in the `dist` folder.



