# By >| Mohammed Alaa Mohammed
# تستخدم الأداة لأغراض الأمان فقط
import os
import tqdm
from tqdm import tqdm
from tqdm import *
import time
BANNED_ACCOUNTS_FILE = "banned_accounts.txt"

# التحقق من وجود ملف الحظر أو إنشائه
if not os.path.exists(BANNED_ACCOUNTS_FILE):
    open(BANNED_ACCOUNTS_FILE, "w").close()

# وظيفة لإضافة حساب إلى قائمة الحظر
def ban_account(account):
    with open(BANNED_ACCOUNTS_FILE, "r") as file:
        banned_accounts = file.read().splitlines()
    if account in banned_accounts:
        print(f"\n\33[91;2mAccouny ❌ '{account}'Already Banned. ⚠︎\33[39;0m")
    else:
        with open(BANNED_ACCOUNTS_FILE, "a") as file:
            file.write(account + "\n")
        print(f"\n\33[32;2mThe Account has Been Banned. ✅ '{account}' Successfully.\33[39;0m")

# وظيفة لإزالة حساب من قائمة الحظر
def unban_account(account):
    with open(BANNED_ACCOUNTS_FILE, "r") as file:
        banned_accounts = file.read().splitlines()
    if account in banned_accounts:
        banned_accounts.remove(account)
        with open(BANNED_ACCOUNTS_FILE, "w") as file:
            file.write("\n".join(banned_accounts) + "\n")
        print(f"\n\33[92;2mThe Account has Been Unblocked. ✅ '{account}'.\33[39;0m")
    else:
        print(f"\n\33[91;2mAccount ❌ '{account}' Not on The Block List. ⚠︎\33[39;0m")

# وظيفة لعرض قائمة الحسابات المحظورة
def list_banned_accounts():
    with open(BANNED_ACCOUNTS_FILE, "r") as file:
        banned_accounts = file.read().splitlines()
    if banned_accounts:
        print("List of Banned Accounts:📋")
        for account in banned_accounts:
            print(f"- {account}")
    else:
        print("\33[91;1mThere are no Banned Accounts Currently.!\33[39;0m")

# القائمة الرئيسية
def main_menu():
    for _ in tqdm (range(0,500),desc="\33[96;1m Processing\33[39;0m",total=500,mininterval=1,colour='blue',postfix='Wait'):
        time.sleep(.00699)

    print("\n👨🏻‍💻 By Developer : Mohammed Alaa Mohammed ⭐⭐⭐⭐⭐\n")
    while True:
        print("\33[92;1m\n</> Simulate Blocking and Unblocking of Accounts.\n\33[39;0m")
        print("+"+"-"*50+"+")
        print("\33[36;2m🔐1 - Account Ban Now")
        print("\33[36;2m🔓2 - Unblock Anaccount")
        print("\33[36;2m🔎3 - View List of Blocked Accounts")
        print("\33[36;2m🤝4 - Can You Help Me Of This")
        print("\33[91;1m👋🏻0 - Exit an Tool\33[39;0m")
        print("+" + "-" * 50 + "+")
        choice = input("\33[34;1m⟦→⟧ Choose a Number From List ====>| \33[39;0m").strip()
        print("+" + "-" * 50 + "+")
        if choice == "1":
            account = input("\33[33;2m⟦→⟧ Enter The Account Name to Block --->: \33[39;0m").strip()
            ban_account(account)
        elif choice == "2":
            account = input("\33[35;1mEnter The Account Name to Unblock --->: \33[39;0m").strip()
            unban_account(account)
        elif choice == "3":
            list_banned_accounts()

        elif choice == "4":
            print("\n\r\33[33;1mSet a Account Name of Set it Block List\33[39;0m",end='\r')
        elif choice == "0":
            print("Farewell! 👋")
            break
        else:
            print("\33[91;1m🔴 Invalid Selection. Try Again. ❌ ⁴⁰⁴ \33[39;0m")

if __name__ == "__main__":
    main_menu()
