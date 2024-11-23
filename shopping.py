import random
def shopping(amount):
    items={'jackets':25.99, 'sweater':15.50, 't-shirts':13.69, 'jeans': 16.49, 'sweatpants':20.99,'sneakers':14.79, 
    'pencils':0.99, 'pens': 1.99, 'eraser':1.59, 'notebooks':2.99, 'binders':5.99, 'folders': 2.59, 'markers':2.00}
    cart=dict()
    total = 0
    store_item = input("What would you like to buy? Enter item (or type 'Done' to finish):").lower()
    while True: 
        
        if store_item == 'done': 
            break 
        while store_item not in items: 
            store_item = input("This item is not in the store. Try again: ").lower() 
        quantity = input("How many would you like to buy? ") 
        try: 
            quantity = float(quantity) # Convert quantity to float 
        except ValueError: 
            print("Please enter a valid number for quantity.") 
            continue 
        if store_item in cart: 
            cart[store_item] += quantity 
        else: 
            cart[store_item] = quantity 
        total += items[store_item] * float(quantity) 
        store_item = input("Is there anything else you would like to buy? (type 'Done' to finish): ").lower()
    print("Seems like you are ready to check out. Let's check the total")
    if(total > amount):
        drop(amount, total, items, cart)
    checkout(amount, total, items, cart)
        
def drop(amount, total, items, cart):
    print("Seems like you need to drop an item")
    
    drop_item=input("Which item would like to drop?")
    while drop_item != "Done" or total > amount:
        while not drop_item in cart.keys():
            drop_item = input("That item is not in your cart. You need drop an item from your cart.")
        drop_quantity = input("How many would like to drop?")
        while(drop_quantity > cart[drop_item]):
            drop_quantity = input("You don't have that much "+ str(drop_item) + " in your cart. Try again.")
        cart[drop_item] -= drop_quantity
        for j in range(drop_quantity):
            total -= items[drop_item]
        drop_item = input("Is there anything else you would like to drop?")
    
    
def checkout(amount, total, items, cart):
    print("Time for you checkout your items.")
    item_total = 0
    for cart_key in cart.keys():
        item_total += cart[cart_key] * items[cart_key]
        print(str(cart[cart_key]) + " " + str(cart_key) + " "+ str(item_total))
        item_total = 0
    
    amount -= total
    print("You are left with "+str(amount)+ " Thank you for shopping")





def main():
    print("Hello, welcome to the shop.")
    amount = random.uniform(100.0, 5000.0) 
    amount = round(amount, 2)
    print("You have "+str(amount)+" with you")
    shopping(amount)

main()
