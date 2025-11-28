print("🎧 Welcome to the DJ 2TUFF Event Pricing Calculator 🎧")

event_type = input("Enter event type (party / club / wedding / corporate / game / festival): ").lower()
hours = float(input("How many hours will you DJ? "))

if hours < 1:
    print("⚠️ Minimum booking is 1 hour. Updated to 1 hour.")
    hours = 1

distance = float(input("How far is the event? (miles): "))

base_rate = 0

if event_type == "party":
    base_rate = 60
elif event_type == "club":
    base_rate = 75
elif event_type == "wedding":
    base_rate = 100
elif event_type == "corporate":
    base_rate = 120
elif event_type == "game":
    base_rate = 65
elif event_type == "festival":
    base_rate = 150
else:
    print("Invalid event type. Default rate applied.")
    base_rate = 70

if distance <= 10:
    travel_fee = 0
elif distance <= 25:
    travel_fee = 20
else:
    travel_fee = 40

subtotal = base_rate * hours + travel_fee

apply_discount = input("Is this for Sigma / FSU / a friend? (yes/no): ").lower()

if apply_discount == "yes":
    discount = subtotal * 0.20
else:
    discount = 0

total = subtotal - discount

print("\n===== FINAL QUOTE =====")
print(f"Event Type: {event_type.capitalize()}")
print(f"Hours: {hours}")
print(f"Hourly Rate: ${base_rate}")
print(f"Travel Fee: ${travel_fee}")
print(f"Discount: -${discount:.2f}")
print(f"TOTAL: ${total:.2f}")
print("========================")

