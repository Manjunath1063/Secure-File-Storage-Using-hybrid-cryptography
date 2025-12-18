# Secure File Storage Using Hybrid Cryptography

## 📌 Project Overview

The **Secure File Storage Using Hybrid Cryptography** project is a Python-based desktop application designed to securely store and manage user files. The system focuses on data confidentiality and controlled access by combining authentication mechanisms with encryption techniques. The application provides a graphical user interface (GUI) for ease of use and ensures that files are encrypted before being stored locally.

This project is suitable for understanding **file security concepts**, **encryption**, and **Python desktop application development**.

---

## 🎯 Objectives

* To provide secure storage for user files
* To prevent unauthorized access using authentication mechanisms
* To encrypt files before storage to maintain confidentiality
* To build a simple and user-friendly desktop application

---

## 🛠️ Technology Stack

* **Programming Language:** Python
* **GUI Framework:** Tkinter
* **Cryptography:** Cryptography library (Fernet – symmetric encryption)
* **Data Storage:** Local file system
* **Data Serialization:** Pickle
* **Other Libraries:** PIL (Image handling)

---

## 🔐 Key Features

* User registration and login
* Graphical password authentication
* OTP-based verification
* Secure file upload and download
* File encryption and decryption using hybrid cryptography approach
* Encrypted local file storage
* Exception handling and validation

---

## 🧩 System Architecture

1. User registers and logs in through the Tkinter GUI
2. Authentication is validated using stored credentials
3. OTP verification adds an extra layer of security
4. Files selected by the user are encrypted before storage
5. Encrypted files are stored securely in the local system
6. Authorized users can decrypt and access stored files

---

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.x installed on the system
* Basic understanding of Python and Tkinter

### Steps to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Manjunath1063/Secure-File-Storage-Using-hybrid-cryptography.git
   ```
2. Navigate to the project directory:

   ```bash
   cd Secure-File-Storage-Using-hybrid-cryptography
   ```
3. Install required dependencies:

   ```bash
   pip install cryptography pillow
   ```
4. Run the application:

   ```bash
   python main.py
   ```

---

## 📂 Project Structure

```
Secure-File-Storage-Using-hybrid-cryptography/
│── main.py
│── script.py
│── finalscript.py
│── server_storage/
│── images/
│── *.pickle
│── README.md
```

---

## 🔎 Security Implementation

* **Encryption:** Files are encrypted using Fernet symmetric encryption
* **Authentication:** User credentials and graphical passwords are validated
* **OTP Verification:** Provides an additional security layer
* **Data Protection:** Sensitive information is not stored in plain text

---

## 🧪 Testing

* Tested user registration and login flows
* Verified file encryption and decryption
* Checked unauthorized access prevention
* Validated exception handling scenarios

---

## 🚀 Future Enhancements

* Integration with a database (MySQL/PostgreSQL)
* Cloud-based secure storage
* Role-based access control
* Improved UI and user experience

---

## 👤 Author

**Manjunath**
Python Developer | Java Backend Enthusiast

---

## 📄 License

This project is developed for academic and learning purposes.
