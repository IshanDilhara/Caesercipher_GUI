import tkinter as tk

class CaesarCipherGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Caesar Cipher")

        # Create labels
        self.message_label = tk.Label(self.root, text="Message:")
        self.key_label = tk.Label(self.root, text="Key:")
        self.encrypted_message_label = tk.Label(self.root, text="Encrypted message:")
        self.decrypted_message_label = tk.Label(self.root, text="Decrypted message:")

        # Create entry widgets
        self.message_entry = tk.Entry(self.root)
        self.key_entry = tk.Entry(self.root)
        self.encrypted_message_entry = tk.Entry(self.root)
        self.decrypted_message_entry = tk.Entry(self.root)

        # Create buttons
        self.encrypt_button = tk.Button(self.root, text="Encrypt", command=self.encrypt)
        self.decrypt_button = tk.Button(self.root, text="Decrypt", command=self.decrypt)

        # Place widgets on the grid
        self.message_label.grid(row=0, column=0)
        self.message_entry.grid(row=0, column=1)
        self.key_label.grid(row=1, column=0)
        self.key_entry.grid(row=1, column=1)
        self.encrypted_message_label.grid(row=2, column=0)
        self.encrypted_message_entry.grid(row=2, column=1)
        self.decrypted_message_label.grid(row=3, column=0)
        self.decrypted_message_entry.grid(row=3, column=1)
        self.encrypt_button.grid(row=4, column=0)
        self.decrypt_button.grid(row=4, column=1)

        # Start the mainloop
        self.root.mainloop()

    def encrypt(self):
        message = self.message_entry.get()
        key = int(self.key_entry.get())

        # Encrypt the message
        encrypted_message = ""
        for char in message:
            encrypted_message += chr(ord(char) + key)

        # Display the encrypted message
        self.encrypted_message_entry.delete(0, "end")
        self.encrypted_message_entry.insert(0, encrypted_message)

    def decrypt(self):
        encrypted_message = self.encrypted_message_entry.get()
        key = int(self.key_entry.get())

        # Decrypt the message
        decrypted_message = ""
        for char in encrypted_message:
            decrypted_message += chr(ord(char) - key)

        # Display the decrypted message
        self.decrypted_message_entry.delete(0, "end")
        self.decrypted_message_entry.insert(0, decrypted_message)

if __name__ == "__main__":
    gui = CaesarCipherGUI()
