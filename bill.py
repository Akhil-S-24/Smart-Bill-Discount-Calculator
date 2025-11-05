from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.CYAN + "=== Welcome to SuperShop ===\n")


name = input("Enter your name: ")
phone = input("Enter your phone number: ")


n = int(input("\nHow many items are you buying? "))
total = 0
items = []

for i in range(n):
    item_name = input(f"\nEnter name of item {i+1}: ")
    price = float(input(f"Enter price of {item_name} (₹): "))
    total += price
    items.append((item_name, price))


if total >= 5000:
    discount = total * 0.20
    message = "🎉 Congratulations! You got a 20% discount!"
elif total >= 3000:
    discount = total * 0.15
    message = "✨ You got a 15% discount!"
elif total >= 1000:
    discount = total * 0.10
    message = "😊 You got a 10% discount!"
else:
    discount = 0
    message = "No discount available for amounts below ₹1000."


gst = (total - discount) * 0.05
final_amount = total - discount + gst

print(Fore.YELLOW + "\n--- BILL RECEIPT ---")
print(f"Customer Name : {name}")
print(f"Phone Number  : {phone}")
print(f"Date & Time   : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
print("-----------------------------")
print("Items Purchased:")
for item, price in items:
    print(f" - {item} : ₹{price:.2f}")
print("-----------------------------")
print(f"Total Amount  : ₹{total:.2f}")
print(f"Discount      : ₹{discount:.2f}")
print(f"GST (5%)      : ₹{gst:.2f}")
print(Fore.GREEN + f"Final Amount  : ₹{final_amount:.2f}")
print("-----------------------------")
print(Fore.CYAN + message)
print(Fore.MAGENTA + "Thank you for shopping with us! Visit again! 🛍️")
print(Fore.CYAN + "=============================\n")

save = input("Do you want to save this bill as a text file? (yes/no): ").lower()
if save == "yes":
    filename = f"bill_{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== SuperShop Bill Receipt ===\n")
        f.write(f"Customer Name : {name}\n")
        f.write(f"Phone Number  : {phone}\n")
        f.write(f"Date & Time   : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("-----------------------------\n")
        for item, price in items:
            f.write(f"{item} : ₹{price:.2f}\n")
        f.write("-----------------------------\n")
        f.write(f"Total Amount  : ₹{total:.2f}\n")
        f.write(f"Discount      : ₹{discount:.2f}\n")
        f.write(f"GST (5%)      : ₹{gst:.2f}\n")
        f.write(f"Final Amount  : ₹{final_amount:.2f}\n")
        f.write("-----------------------------\n")
        f.write(message + "\n")
        f.write("Thank you for shopping with us! 🛍️\n")
    print(Fore.GREEN + f"Bill saved successfully as '{filename}'")
else:
    print(Fore.RED + "Bill not saved.")
