# 🏦 Bank Management System (BMS)

A simple **Bank Management System** built using Python that allows users to create, modify, delete accounts, deposit and withdraw money, and view account details. The system uses file handling with `pickle` for data storage and retrieval.

---

## 🚀 Features

- 📂 **Account Management:**  
  - Create new accounts (Savings/Current).  
  - Modify existing account details.  
  - Delete accounts.  

- 💰 **Transaction Management:**  
  - Deposit money into an account.  
  - Withdraw funds with balance validation.  
  - View account balance.  

- 📜 **Report Generation:**  
  - Display details of all account holders.  
  - View specific account details.  

---

## 🛠️ Technologies Used

- **Programming Language:** Python 🐍  
- **File Handling:** `pickle` for data persistence  
- **CLI Tool:** Streamlit (for UI enhancements in the future)  

---

## 📥 Installation Guide

1. **Clone the repository**  
   ```bash
   git clone https://github.com/AnjaliJichkar/BMS.git
   ```

2. **Navigate to the project directory**  
   ```bash
   cd BMS
   ```

3. **Create a virtual environment (optional)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

4. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**  
   ```bash
   python bank.py
   ```
   
 6. **Install Streamlit**  
   ```bash
   pip install streamlit
   ```
   
6. **Run the Streamlit application**  
   ```bash
   streamlit run bms.py
   ```

---

## 📖 Usage

1. **Run the program**, and you will see the following options:

   ```
   1. NEW ACCOUNT
   2. DEPOSIT AMOUNT
   3. WITHDRAW AMOUNT
   4. BALANCE ENQUIRY
   5. ALL ACCOUNT HOLDER LIST
   6. CLOSE AN ACCOUNT
   7. MODIFY AN ACCOUNT
   8. EXIT
   ```

2. **Choose the desired option and follow the instructions.**

---

## 📁 Project Structure

```
BMS/
│-- accounts.data          # Serialized account data file
│-- bank.py     # Main script for CLI operations
│-- bms.py     # Streamlit script for CLI operations
│-- README.md              # Project documentation
│-- requirements.txt       # Required dependencies
│-- .gitignore             # Ignored files and folders
└─── tests/                 # Unit tests
```

---

## 🧪 Testing

To run unit tests, execute:

```bash
python -m unittest discover tests
```

---

## 🛡️ Security Measures

- Account balance checks before withdrawals.  
- Input validation for account creation and transactions.  
- Serialization with `pickle` for secure data storage.  

---

## 🌟 Future Enhancements

- [ ] Build a GUI using **Streamlit** for a more user-friendly interface.  
- [ ] Add user authentication for secure access.  
- [ ] Improve data storage using **SQLite** or **MongoDB**.  
- [ ] Implement transaction history tracking.  
- [ ] Create web-based access using Flask/Django.  

---

## 🏗️ Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.  
2. Create a feature branch: `git checkout -b feature-name`.  
3. Commit your changes: `git commit -m "Add new feature"`.  
4. Push to the branch: `git push origin feature-name`.  
5. Open a pull request.  

**Anjali Jichkar**  
🔗 [GitHub Profile](https://github.com/AnjaliJichkar)

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

