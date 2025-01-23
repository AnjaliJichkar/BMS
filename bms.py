import streamlit as st
import pickle
import os
import pathlib

# Account class
class Account:
    def __init__(self, accNo, name, acc_type, deposit):
        self.accNo = accNo
        self.name = name
        self.type = acc_type
        self.deposit = deposit

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        if amount <= self.deposit:
            self.deposit -= amount
            return True
        else:
            return False

# File handling functions
def loadAccounts():
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            return pickle.load(infile)
    return []

def saveAccounts(accounts):
    with open('accounts.data', 'wb') as outfile:
        pickle.dump(accounts, outfile)

# Streamlit UI
def main():
    st.title("🏦 Bank Management System")

    menu = ["Home", "New Account", "Deposit", "Withdraw", "Balance Enquiry", "Account List", "Close Account", "Modify Account", "Exit"]
    choice = st.sidebar.selectbox("Menu", menu)

    accounts = loadAccounts()

    if choice == "Home":
        st.write("Welcome to the Bank Management System!")
        st.image("https://images.unsplash.com/photo-1501167786227-4cba60f6d58f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGJhbmt8ZW58MHx8MHx8fDA%3D", width=400)

    elif choice == "New Account":
        st.subheader("Create a New Account")
        accNo = st.number_input("Enter Account Number", min_value=1, step=1)
        name = st.text_input("Enter Account Holder Name")
        acc_type = st.radio("Select Account Type", ["Saving", "Current"])
        deposit = st.number_input("Enter Initial Deposit (>=500 for Saving, >=1000 for Current)", min_value=0)

        if st.button("Create Account"):
            if (acc_type == "Saving" and deposit >= 500) or (acc_type == "Current" and deposit >= 1000):
                new_account = Account(accNo, name, acc_type, deposit)
                accounts.append(new_account)
                saveAccounts(accounts)
                st.success(f"Account {accNo} created successfully!")
            else:
                st.error("Insufficient initial deposit amount!")

    elif choice == "Deposit":
        st.subheader("Deposit Amount")
        accNo = st.number_input("Enter Account Number", min_value=1, step=1)
        amount = st.number_input("Enter Deposit Amount", min_value=0)
        
        if st.button("Deposit"):
            for account in accounts:
                if account.accNo == accNo:
                    account.depositAmount(amount)
                    saveAccounts(accounts)
                    st.success(f"Deposited ${amount} to account {accNo}")
                    break
            else:
                st.error("Account not found!")

    elif choice == "Withdraw":
        st.subheader("Withdraw Amount")
        accNo = st.number_input("Enter Account Number", min_value=1, step=1)
        amount = st.number_input("Enter Withdrawal Amount", min_value=0)
        
        if st.button("Withdraw"):
            for account in accounts:
                if account.accNo == accNo:
                    if account.withdrawAmount(amount):
                        saveAccounts(accounts)
                        st.success(f"Withdrawn ${amount} from account {accNo}")
                    else:
                        st.error("Insufficient balance!")
                    break
            else:
                st.error("Account not found!")

    elif choice == "Balance Enquiry":
        st.subheader("Check Account Balance")
        accNo = st.number_input("Enter Account Number", min_value=1, step=1)
        
        if st.button("Check Balance"):
            for account in accounts:
                if account.accNo == accNo:
                    st.info(f"Account Balance: ${account.deposit}")
                    break
            else:
                st.error("Account not found!")

    elif choice == "Account List":
        st.subheader("All Account Holders")
        if accounts:
            for account in accounts:
                st.write(f"**Account No:** {account.accNo}, **Name:** {account.name}, **Type:** {account.type}, **Balance:** ${account.deposit}")
        else:
            st.warning("No accounts available.")

    elif choice == "Close Account":
        st.subheader("Close an Account")
        accNo = st.number_input("Enter Account Number to Close", min_value=1, step=1)
        
        if st.button("Close Account"):
            updated_accounts = [acc for acc in accounts if acc.accNo != accNo]
            if len(updated_accounts) < len(accounts):
                saveAccounts(updated_accounts)
                st.success(f"Account {accNo} has been closed.")
            else:
                st.error("Account not found!")

    elif choice == "Modify Account":
        st.subheader("Modify Account Details")
        accNo = st.number_input("Enter Account Number to Modify", min_value=1, step=1)
        
        for account in accounts:
            if account.accNo == accNo:
                new_name = st.text_input("Enter New Account Holder Name", account.name)
                new_type = st.radio("Select New Account Type", ["Saving", "Current"], index=0 if account.type == "Saving" else 1)
                new_deposit = st.number_input("Enter New Balance", min_value=0, value=account.deposit)
                
                if st.button("Update Account"):
                    account.name = new_name
                    account.type = new_type
                    account.deposit = new_deposit
                    saveAccounts(accounts)
                    st.success("Account updated successfully!")
                break
        else:
            st.error("Account not found!")

    elif choice == "Exit":
        st.success("Thanks for using the Bank Management System!")
        st.stop()

if __name__ == "__main__":
    main()