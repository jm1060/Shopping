import random
def shopping(amount):
    # Data initialization
    clothes_items = {
        'jackets': 25.99, 'sweater': 15.50, 't-shirts': 13.69, 'jeans': 16.49, 
        'sweatpants': 20.99, 'sneakers': 14.79, 'glasses': 25.25,
        'long-sleeve-shirts': 14.69, 'vests': 19.49, 'short-sleeve-jackets': 20.79
    }
    school_supplies = {
        'pencils': 0.99, 'pens': 1.99, 'eraser': 1.59, 'notebooks': 2.99, 
        'binders': 5.99, 'folders': 2.59, 'markers': 2.00
    }
    appliances = {
        'refrigerator': 599.99, 'air-conditioning': 479.99, 'microwave': 84.99,
        'dishwasher': 349.79, 'fan': 51.99, 'tv': 1089.99
    }
    furniture = {
        'chairs': 25.89, 'sofa': 301.99, 'tables': 40.79, 'bed:': 539.98, 'drawers': 55.69, 
        'cabinets': 61.99, 'shelves': 115.68, 'closet': 150.59
    }
    electronics = {
        'computer': 309.99, 'phone':151.98, 'headphones': 78.79, 'game-console':230.59
    }
    sports = {'basketball': 13.42, 'soccer-ball':22.97, 'baseball': 24.95, 'bat': 39.99, 'bowling-ball': 46.99, 
                'tennis-ball': 3.38, 'tennis-racket': 29.08, 'boxing-gloves':29.98, 'hockey-stick': 41.97, 'hockey-puck':2.50,
                'lacrosse-stick':42.05, 'volleyball':27.15, 'dodgeball': 10.99, 'badminton-racket':30.91, 'football': 18.99}
    sale_items = {
        'jackets': 0.1, 'sweater': 0.15, 't-shirts': 0.1, 'jeans': 0.20, 
        'sweatpants': 0.1, 'sneakers': 0.25, 'glasses': 0.1,
        'long-sleeve-shirts': 0.1, 'vests': 0.16, 'short-sleeve-jackets': 0.225,
        'binders': 0.10, 'refrigerator': 0.25, 'air-conditioning': 0.15,
        'microwave': 0.05, 'dishwasher': 0.15, 'fan': 0.075, 'tv': 0.30,
        'chairs':0.025, 'sofa':0.15, 'tables':0.075, 'bed':0.15, 'drawers':0.075, 'cabinets':0.05,
        'shelves': 0.1, 'closet':0.125, 'computer': 0.1, 'game-console':0.1 
    }
    cart = {}
    total = 0

    # Shopping process
    section = input("What section would you like to buy from? (clothes, supplies, appliances, furniture, electronics) or type 'done' to finish: ").lower()
    while section != 'done': 
        if section == 'clothes':
            total = shop_clothes(total, clothes_items, sale_items, cart)
        elif section == 'supplies':
            total = shop_school_supplies(total, school_supplies, sale_items, cart)
        elif section == 'appliances':
            total = shop_appliances(total, appliances, sale_items, cart)
        elif section  == 'furniture':
            total = shop_furniture(total, furniture, sale_items, cart)
        elif section == 'electronics':
            total = shop_electronics(total, electronics, sale_items, cart)
        else:
            print("Invalid section. Please choose from clothes, supplies, or appliances.")
        section = input("Is there anything else you would like to buy? (clothes, supplies, appliances) or type 'done' to finish: ").lower()
    print(f"Total after shopping is {round(total, 2)}, Budget is {amount}")

    # Check if total exceeds budget
    if total > amount:
        print(f"Your total is {round(total, 2)}, which exceeds your budget of {round(amount, 2)}.")
        drop_section = None  # Initialize drop_section outside the loop
        while total > amount:
            drop_section = input("Which section would you like to remove items from (clothes, supplies, appliances)? Or type 'done' to stop: ").lower()
            if drop_section == 'done':
                print("You decided to stop dropping items.")
                break
            elif drop_section == 'clothes':
                total = drop(amount, total, clothes_items, sale_items, cart)
            elif drop_section == 'supplies':
                total = drop(amount, total, school_supplies, sale_items, cart)
            elif drop_section == 'appliances':
                total = drop(amount, total, appliances, sale_items, cart)
            elif drop_section == 'furniture':
                total = drop(amount, total, furniture, sale_items, cart)
            elif drop_section == 'electronics':
                total = drop(amount, total, electronics, sale_items, cart)
            else:
                print("Invalid section. Please choose from clothes, supplies, or appliances.")

# Checkout
    checkout(amount, clothes_items, school_supplies, appliances, furniture, electronics, cart, sale_items)

# Shopping section functions
def shop_clothes(total, clothes_items, sale_items, cart):
    return shop_generic(total, clothes_items, sale_items, cart, "clothes")

def shop_school_supplies(total, school_supplies, sale_items, cart):
    return shop_generic(total, school_supplies, sale_items, cart, "school supplies")

def shop_appliances(total, appliances, sale_items, cart):
    return shop_generic(total, appliances, sale_items, cart, "appliances")

def shop_furniture(total, furniture, sale_items, cart):
    return shop_generic(total, furniture, sale_items, cart, "furniture")

def shop_electronics(total, electronics, sale_items, cart):
    return shop_generic(total, electronics, sale_items, cart, "electronics")

def shop_generic(total, items, sale_items, cart, section_name):
    item = input(f"What {section_name} would you like to buy? Enter item (or type 'done' to finish): ").lower()
    while item != 'done':
        if item not in items:
            item = input("This item is not in the store. Try again: ").lower()
            continue
        try:
            quantity = float(input("How many would you like to buy? "))
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
        cart[item] = cart.get(item, 0) + quantity
        if item in sale_items:
            print("This item is on sale!")
            total += (items[item] - (items[item] * sale_items[item])) * quantity
        else:
            total += items[item] * quantity
        item = input(f"Is there anything else you would like to buy? (type 'done' to finish): ").lower()
    return total

# Drop function
def drop(amount, total, items, sale_items, cart):
    drop_item = None
    while total > amount:
        print(f"Current total: {round(total, 2)} | Budget: {round(amount, 2)}")
        drop_item = input("Which item would you like to remove? ").lower()
        if drop_item not in cart or cart[drop_item] <= 0:
            print("This item is not in your cart or you have none left to drop. Try again.")
            continue

        try:
            drop_quantity = float(input(f"How many {drop_item}'s would you like to remove? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if drop_quantity > cart[drop_item]:
            print(f"You don't have that many {drop_item}s in your cart. Try again.")
            continue

        cart[drop_item] -= drop_quantity
        if cart[drop_item] <= 0:
            del cart[drop_item]
        if drop_item in sale_items:
            total -= (items[drop_item] - (items[drop_item] * sale_items[drop_item])) * drop_quantity
        else:
            total -= items[drop_item] * drop_quantity

        print(f"Updated total: {round(total, 2)}")
        if total <= amount:
            print("Your total is now within budget.")
            break
    return total
# Checkout function
def checkout(amount, clothes_items, school_supplies, appliances, furniture, electronics, cart, sale_items):
    print("Time for you to checkout. Printing receipt...")
    total = 0
    for item, quantity in cart.items():
        if item in clothes_items:
            price = clothes_items[item]
        elif item in school_supplies:
            price = school_supplies[item]
        elif item in appliances:
            price = appliances[item]
        elif item in furniture:
            price = furniture[item]
        elif item in electronics:
            price = electronics[item]
        else:
            continue
        if item in sale_items:
            price -= price * sale_items[item]

        item_total = price * quantity
        total += item_total
        print(f"{quantity} {item} {round(price, 2)} each: {round(item_total, 2)}")

    print(f"Total: {round(total, 2)}")
    print(f"Remaining budget: {round(amount - total, 2)}")
    print("Thank you for shopping!")

# Main function
def main():
    print("Hello, welcome to the shop.")
    amount = round(random.uniform(0, 500.0), 2)
    print(f"You have ${amount} with you.")
    shopping(amount)

main()
