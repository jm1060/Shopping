import random
def shopping(amount):
    clothes_items={'jackets':25.99, 'sweater':15.50, 't-shirts':13.69, 'jeans': 16.49, 'sweatpants':20.99,'sneakers':14.79, 'glasses':25.25,
    'long-sleeve-shirts':14.69, 'vests':19.49, 'short-sleeve-jackets':20.79}
    school_supplies={'pencils':0.99, 'pens': 1.99, 'eraser':1.59, 'notebooks':2.99, 'binders':5.99, 'folders': 2.59, 'markers':2.00}
    sale_items={'jackets':0.1, 'sweater':0.15, 't-shirts': 0.1, 'jeans':0.20, 'sweatpants': 0.1, 'sneakers':0.25, 'glasses':0.1, 
    'long-sleeve-shirts':0.1, 'vests':0.16, 'short-sleeve-jackets':0.225}
    cart=dict()
    total = 0
    section = input("What section would you like to buy from? Enter item (or type 'Done' to finish):").lower()
    while True: 
        
        if section == 'done': 
            break 
        else:
            if(section == 'clothes'):
                shop_clothes(total, clothes_items, sale_items, cart)
 
        section = input("Is there anything section else you would like to buy from? (type 'Done' to finish): ").lower()
    print("Seems like you are ready to check out. Let's check the total")
    if(total > amount):
        drop(amount, total, items, sale_items, cart)
    checkout(amount, items, cart, sale_items)

def shop_clothes(total, clothes_items, sale_items, cart):
    cloth_item = input("What clothes would you like to buy from? Enter item (or type 'Done' to finish):").lower()
    while True:
        while cloth_item not in clothes_items: 
            cloth_item = input("This item is not in the store. Try again: ").lower() 
        quantity = input("How many would you like to buy? ") 
        try: 
            quantity = float(quantity) # Convert quantity to float 
        except ValueError: 
            print("Please enter a valid number for quantity.") 
            continue 
        if cloth_item in cart: 
            cart[cloth_item] += quantity 
        else: 
            cart[cloth_item] = quantity 
        if(cloth_item in sale_items):
            print("You have a sale item")
            add_off_sale_cart(total, quantity, clothes_items, sale_items, cloth_item)
        else:
            total += clothes_items[cloth_item] * float(quantity) 
        cloth_item = input("Is there anything section else you would like to buy from? (type 'Done' to finish): ").lower()


def drop(amount, total, items, sale_items, cart):
    print("Seems like you need to drop an item")
    
    drop_item=input("Which item would like to drop?")
    while drop_item != "Done" or total > amount:
        while not drop_item in cart.keys():
            drop_item = input("That item is not in your cart. You need drop an item from your cart.")
        drop_quantity = input("How many would like to drop?")
        while(drop_quantity > cart[drop_item]):
            drop_quantity = input("You don't have that much "+ str(drop_item) + " in your cart. Try again.")
        cart[drop_item] -= drop_quantity
        if(drop_item in sale_items):
            drop_off_sale(total, drop_quantity, items, sale_items, drop_item)
        else:
            total -= items[drop_item] * float(drop_quantity) 
        drop_item = input("Is there anything else you would like to drop?")
    
  
def add_off_sale_cart(total, quantity, items, sale_items, store_item):
    total+=(items[store_item] - (sale_items[store_item] * items[store_item])) * quantity

def drop_off_sale(total, drop_quantity,items, sales_items, store_item):
    total-=(items[store_item] - (sales_items[store_item] * items[store_item])) * drop_quantity

def checkout(amount, items, cart, sale_items):
    print("Time for you checkout your items. Time to print out your receipt")
    item_total = 0
    total = 0
    for cart_key in cart.keys():
        if(cart_key in sale_items):
            item_total += (cart[cart_key] * (items[cart_key] - (items[cart_key] * sale_items[cart_key])))
        else:    
            item_total += cart[cart_key] * items[cart_key]
        print(str(cart[cart_key]) + " " + str(cart_key) + " "+ str(round(item_total, 2)))
        total += item_total
        item_total = 0
    
    amount -= total
    print("Your total for purchase: "+str(round(total, 2)))
    print("You are left with "+str(round(amount, 2))+ " Thank you for shopping")


def main():
    print("Hello, welcome to the shop.")
    amount = random.uniform(100.0, 5000.0) 
    amount = round(amount, 2)
    print("You have "+str(amount)+" with you")
    shopping(amount)

main()
