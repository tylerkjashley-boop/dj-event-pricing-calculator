PACKAGES = {
    "1": {"name": "Party", "rate": 60},
    "2": {"name": "Club", "rate": 75},
    "3": {"name": "Wedding", "rate": 100},
    "4": {"name": "Corporate", "rate": 120},
    "5": {"name": "Game", "rate": 65},
    "6": {"name": "Festival", "rate": 150},
}

def get_float(prompt, min_value=None):
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
            if min_value is not None and value < min_value:
                print(f"❌ Please enter a number greater than or equal to {min_value}.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number (e.g., 2 or 3.5).")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "no"):
            return answer
        print("❌ Please type 'yes' or 'no'.")

def save_quote_to_file(client_name, event_date, event_location, event_type, hours, base_rate, travel_fee, subtotal, discount, total):
    # Make a safe filename
    safe_name = "".join(c for c in client_name if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
    safe_date = event_date.strip().replace("/", "-").replace(" ", "_")
    filename = f"quote_{safe_name}_{safe_date}.txt"

    quote_text = f"""
DJ 2Tuff LLC - Event Quote
--------------------------
Client: {client_name}
Event Date: {event_date}
Location: {event_location}

Event Type: {event_type.capitalize()}
Duration: {hours:.1f} hour(s)
Hourly Rate: ${base_rate:.2f}/hr
Travel Fee: ${travel_fee:.2f}
Subtotal: ${subtotal:.2f}
Discount: -${discount:.2f}

TOTAL QUOTE: ${total:.2f}

Thank you,
Tyler Ashley
DJ 2Tuff LLC
""".strip()

    with open(filename, "w", encoding="utf-8") as f:
        f.write(quote_text)

    return filename









print("🎧 Welcome to the DJ 2TUFF Event Pricing Calculator 🎧")

print("\nSelect an event package:")
for key, pkg in PACKAGES.items():
    print(f"{key}. {pkg['name']} (${pkg['rate']}/hr)")

while True:
    package_key = input("Enter package number (1-6): ").strip()
    if package_key in PACKAGES:
        break
    print("❌ Invalid selection. Please enter a number from 1 to 6.")

event_type = PACKAGES[package_key]["name"].lower()
base_rate = PACKAGES[package_key]["rate"]





hours = get_float("How many hours will you DJ? ", min_value=1)
distance = get_float("How far is the event? (miles): ", min_value=0)





if distance <= 10:
    travel_fee = 0
elif distance <= 25:
    travel_fee = 20
else:
    travel_fee = 40

subtotal = base_rate * hours + travel_fee

apply_discount = get_yes_no("Is this for Sigma / FSU / a friend? (yes/no): ")
if apply_discount == "yes":
    discount = subtotal * 0.20
else:
    discount = 0

total = subtotal - discount

print("\n===== FINAL QUOTE =====")
print(f"Event Type: {event_type.capitalize()}")
print(f"Hours: {hours:.1f}")
print(f"Hourly Rate: ${base_rate:.2f}/hr")
print(f"Travel Fee: ${travel_fee:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: -${discount:.2f}")
print(f"TOTAL: ${total:.2f}")
print("========================")

make_file = get_yes_no("\nGenerate a quote file? (yes/no): ")

if make_file == "yes":
    client_name = input("Client name: ").strip()
    event_date = input("Event date (MM/DD/YYYY): ").strip()
    event_location = input("Event location: ").strip()

    filename = save_quote_to_file(
        client_name, event_date, event_location,
        event_type, hours, base_rate, travel_fee,
        subtotal, discount, total
    )

    print(f"✅ Saved: {filename}")

