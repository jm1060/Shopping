import random
def shopping(amount):
    items={'jackets':25.99, 'sweater':15.50, 't-shirts':13.69, 'jeans': '16.49', 'sweatpants':'20.99','sneakers':14.79, 
    'pencils':0.99, 'pens': 1.99, 'eraser':1.59, 'notebooks':2.99, 'binders':5.99, 'folders': 2.59, 'markers':'2.00'}
    cart=dict()
    total = 0
    store_item = input("What would you like to buy?")
    while(store_item != 'Done'):

        while not store_item in items.keys():
            store_item=input("This item is not in the store. Try again")
        quantity = input("How many would you like to buy?")
        if(store_item in cart):
            cart[store_item]+=quantity
        else:
            cart[store_item]=quantity
        for i in range(quantity):
            total+=items[store_item]
        store_item = input("Is there anything else you would like to buy?")
    print("Seems like you are ready to check out. Let's check the total")
    if(total > amount):
        print("Seems like you need to drop an item")
        drop_item=input("Which item would like to drop?")
        while not drop_item in cart.key():
            drop_item   = input("That item is not in your cart. You need drop an item from your cart.")

    
    



def main():
    print("Hello, welcome to the shop.")
    amount = random.uniform(100.0, 5000.0) 
    amount = round(amount, 2)
    print("You have "+str(amount)+" with you")
    shopping(amount)
