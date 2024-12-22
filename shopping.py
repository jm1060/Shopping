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
    tools = {'screwdriver':10.85, 'nails': 5.97, 'hammer':12.91, 'wrench':19.86, 'saw':31.67, 'drill':33.85, 'tape-measure':7.96,
        'gloves':4.93}
    canned_food = {'canned-vegetables':3.99, 'canned-tomatoes':3.59, 'canned-fruit':3.89, 'canned-beans':3.92, 'canned-salmon':4.05,
    'canned-tuna':4.05, 'canned-crab':3.99, 'canned-chicken': 4.49, 'canned-spam':5.99, 'canned-beets':3.49, 'canned-olives':3.39, 
    'tomato-sauce':3.59, 'spaghetti-sauce':3.69}
    fruits = {'apple':1.25, 'bananas':3.39, 'orange':1.29, 'pears':1.19, 'grapes':5.79, 'plums': 1.29, 'lemon':0.99, 'blueberries':4.49,
    'peach':1.59, 'kiwi':1.29, 'mango':2.05, 'watermelon':15.89, 'tangerine':0.79}
    vegetables = {'brocoli':5.99, 'carrots':7.99, 'corn':1.59, 'eggplant':2.49, 'cabbage':6.09, 'mushrooms':4.49, 'potato':0.99, 
    'onion':1.29, 'bok-choy':8.99, 'spinach':7.79, 'cucumber':2.59, 'zucchini':2.59, 'sweet potato':0.99}
    bakery = {'bagel':1.09, 'buns':1.29, 'cinnamon-rolls':2.49, 'biscuits':1.19, 'muffin':1.59, 'cupcake':1.79, 'donut': 1.69, 
    'pie': 20.99, 'cake':41.99, 'banana-bread':2.39, 'cookie':0.99, 'tortilla':1.89, 'croissant':2.39, 'cornbread':1.99
    }
    meat = {'eggs':2.99, 'filet-mignon':32.28, 'new-york-strip':17.32, 'ribeye':17.39, 'chicken':12.99, 'pork-chop':10.67, 'pork-tenderloin':39.95,
     'lamb':19.99, 'veal':18.52, 'sausage':3.29, 'ground-beef':5.63,'turkey':26.20}
    fish = {'snapper': 30.00, 'salmon':32.50, 'cod':18.44, 'tuna':199.99, 'flounder':25.99, 'haddock':14.95, 'catfish':6.99, 'halibut':295.95,
            'swordfish':34.50, 'trout':21.98}
    sale_items = {
        'jackets': 0.1, 'sweater': 0.15, 't-shirts': 0.1, 'jeans': 0.20, 
        'sweatpants': 0.1, 'sneakers': 0.25, 'glasses': 0.1,
        'long-sleeve-shirts': 0.1, 'vests': 0.16, 'short-sleeve-jackets': 0.225,
        'binders': 0.10, 'refrigerator': 0.25, 'air-conditioning': 0.15,
        'microwave': 0.05, 'dishwasher': 0.15, 'fan': 0.075, 'tv': 0.30,
        'chairs':0.025, 'sofa':0.15, 'tables':0.075, 'bed':0.15, 'drawers':0.075, 'cabinets':0.05,
        'shelves': 0.1, 'closet':0.125, 'computer': 0.1, 'game-console':0.1, 'basketball': 0.045,
        'hockey-stick':.10, 'lacrosse-stick':0.1, 'drill':0.15, 'saw':0.1, 'canned-spam':0.05,
        'brocoli':0.05, 'bok-choy':0.10, 'cake': 0.15, 'pie':0.05, 'filet-mignon':0.05, 'NY-Strip':0.05,
        'pork-tenderloin':0.10, 'salmon':0.05, 'tuna':0.1, 'halibut':0.075
    }
    cart = {}
    total = 0

    # Shopping process
    section = input("What section would you like to buy from? (clothes, supplies, appliances, furniture, electronics, sports, tools, \ncanned-food, fruits, vegetables, bakery, meat, fish) or type 'done' to finish: ").lower()
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
        elif section == 'sports':
            total = shop_sports_equip(total, sports, sale_items, cart)
        elif section == 'tools':
            total = shop_tools(total, tools, sale_items, cart)
        elif section == 'canned-food':
            total = shop_canned_food(total, canned_food, sale_items, cart)
        elif section == 'fruits':
            total = shop_fruits(total, fruits, sale_items, cart)
        elif section == 'vegetables':
            total = shop_veggies(total, vegetables, sale_items, cart)
        elif section == 'bakery':
            total = shop_bakery_goods(total, bakery, sale_items, cart)
        elif section == 'meat':
            total = shop_meat(total, meat, sale_items, cart)
        elif section == 'fish':
            total = shop_fish(total, fish, sale_items, cart)
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
            elif drop_section == 'sports':
                total = drop(amount, total, sports, sale_items, cart)
            elif drop_section == 'tools':
                total = drop(amount, total, tools, sale_items, cart)
            elif drop_section == 'canned-food':
                total = drop(amount, total, canned_food, sale_items, cart)
            elif drop_section == 'fruits':
                total = drop(amount, total, fruits, sale_items, cart)
            elif drop_section == 'vegetables':
                total = drop(amount, total, vegetables, sale_items, cart)
            elif drop_section == 'bakery':
                total = drop(amount, total, bakery, sale_items, cart)
            elif drop_section == 'meat':
                total = drop(amount, total, meat, sale_items, cart)
            elif drop_section == 'fish':
                total = drop(amount, total, fish, sale_items, cart)
            else:
                print("Invalid section. Please choose from clothes, supplies, or appliances.")

# Checkout
    checkout(amount, clothes_items, school_supplies, appliances, furniture, electronics, sports, tools, canned_food, fruits, vegetables, bakery, meat, fish, cart, sale_items)

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

def shop_sports_equip(total, sports, sale_items, cart):
    return shop_generic(total, sports, sale_items, cart, "sports")

def shop_fruits(total, fruits, sale_items, cart):
    return shop_generic(total, fruits, sale_items, cart, "fruits")

def shop_veggies(total, vegetables, sale_items, cart):
    return shop_generic(total, vegetables, sale_items, cart, 'vegetables')

def shop_bakery_goods(total, bakery, sale_items, cart):
    return shop_generic(total, bakery, sale_items, cart, 'bakery goods')

def shop_canned_food(total, canned_food, sale_items, cart):
    return shop_generic(total, canned_food, sale_items, cart, "canned-food")

def shop_tools(total, tools, sale_items, cart):
    return shop_generic(total, tools, sale_items, cart, "tools")

def shop_meat(total, meat, sale_items, cart):
    return shop_generic(total, meat, sale_items, cart, "meat" )

def shop_fish(total, fish, sale_items, cart):
    return shop_generic(total, fish, sale_items, cart, "fish")

def shop_generic(total, items, sale_items, cart, section_name):
    item = input(f"What {section_name} item would you like to buy? Enter item (or type 'done' to finish): ").lower()
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
def checkout(amount, clothes_items, school_supplies, appliances, furniture, electronics, sports, tools, canned_food, fruits, vegetables, bakery, meat, fish, cart, sale_items):
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
        elif item in sports:
            price = sports[item]
        elif item in tools:
            price = tools[item]
        elif item in canned_food:
            price = canned_food[item]
        elif item in fruits:
            price = fruits[item]
        elif item in vegetables:
            price = vegetables[item]
        elif item in bakery:
            price = bakery[item]
        elif item in meat:
            price = meat[item]
        elif item in fish:
            price = fish[item]
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
