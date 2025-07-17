import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Constants
SERVER_FOLDER = "server_storage"

# Ensure the server folder exists
os.makedirs(SERVER_FOLDER, exist_ok=True)

class CloudFileStorageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Local File Storage with Cryptography")
        self.root.geometry("500x400")

        # UI Elements
        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file, width=20, height=2)
        self.upload_button.pack(pady=20)

        self.restore_button = tk.Button(root, text="Restore File", command=self.restore_file, width=20, height=2)
        self.restore_button.pack(pady=20)

        self.key_file_label = tk.Label(root, text="Key File (optional):")
        self.key_file_label.pack(pady=10)

        self.key_file_entry = tk.Entry(root, width=50)
        self.key_file_entry.pack(pady=5)

        self.browse_key_button = tk.Button(root, text="Browse Key File", command=self.browse_key_file)
        self.browse_key_button.pack(pady=5)

    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Select a File")
        if not file_path:
            messagebox.showwarning("No File", "Please select a file to upload.")
            return

        # Generate encryption key
        key = Fernet.generate_key()
        cipher = Fernet(key)

        # Encrypt the file
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted_data = cipher.encrypt(data)

        # Save the encrypted file to the server folder
        encrypted_file_name = os.path.basename(file_path) + ".enc"
        encrypted_file_path = os.path.join(SERVER_FOLDER, encrypted_file_name)
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        # Save key to a file
        key_file_path = filedialog.asksaveasfilename(
            defaultextension=".key",
            filetypes=[("Key Files", "*.key")],
            title="Save Encryption Key"
        )
        if key_file_path:
            with open(key_file_path, "wb") as key_file:
                key_file.write(key)
            messagebox.showinfo("Success", f"File uploaded and key saved at:\n{key_file_path}")
        else:
            messagebox.showwarning("Key Not Saved", "File uploaded, but the key was not saved.")

    def restore_file(self):
        encrypted_file_name = filedialog.askopenfilename(
            title="Select Encrypted File to Restore",
            filetypes=[("Encrypted Files", "*.enc")],
            initialdir=SERVER_FOLDER
        )
        if not encrypted_file_name:
            messagebox.showwarning("No File", "Please select an encrypted file to restore.")
            return

        key_file_path = self.key_file_entry.get() or filedialog.askopenfilename(
            title="Select Encryption Key File",
            filetypes=[("Key Files", "*.key")]
        )
        if not key_file_path:
            messagebox.showerror("No Key", "Encryption key is required to restore the file.")
            return

        # Load the encryption key
        try:
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read the key file: {e}")
            return

        cipher = Fernet(key)

        # Read the encrypted file
        try:
            with open(encrypted_file_name, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read the encrypted file: {e}")
            return

        # Decrypt the file
        try:
            decrypted_data = cipher.decrypt(encrypted_data)
        except Exception as e:
            messagebox.showerror("Decryption Error", "Invalid key or corrupted file.")
            return

        # Save the decrypted file
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("All Files", "*.*")],
            title="Save Decrypted File"
        )
        if save_path:
            with open(save_path, "wb") as file:
                file.write(decrypted_data)
            messagebox.showinfo("Success", f"File restored and saved at:\n{save_path}")
        else:
            messagebox.showwarning("Save Canceled", "Restoration canceled by the user.")

    def browse_key_file(self):
        key_file_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
        if key_file_path:
            self.key_file_entry.delete(0, tk.END)
            self.key_file_entry.insert(0, key_file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = CloudFileStorageApp(root)
    root.mainloop()