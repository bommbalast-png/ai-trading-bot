# bot_auto.py
import time
import random

balance = 1000
print("🚀 Raju Auto Trading Bot Started (Demo Mode)")
print(f"Starting balance: ₹{balance}\n")

while True:
    trade = random.choice(["win", "loss"])
    if trade == "win":
        balance *= 1.02  # 2% profit
        print(f"✅ Trade WIN! New balance: ₹{round(balance,2)}")
    else:
        balance *= 0.98  # 2% loss
        print(f"❌ Trade LOSS! New balance: ₹{round(balance,2)}")

    time.sleep(2)  # wait 2 seconds between trades
