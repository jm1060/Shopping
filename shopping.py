import random
def shopping(amount):
    items={'jackets':25.99, 'sweater':15.50, 't-shirts':13.69, 'jeans': '16.49', 'sweatpants':'20.99','sneakers':14.79, 
    'pencils':0.99, 'pens': 1.99, 'eraser':1.59, 'notebooks':2.99, 'binders':5.99, 'folders': 2.59, 'markers':'2.00'}
    cart=dict()
    store_item = input("What would you like to buy?")
    while not store_item in items.keys():
        print("This item is not in the store. Try again")
    quantity = input("How many would you like to buy?")
    if(store_item in cart):
        cart[store_item]+=quantity
    else:
        cart[store_item]=quantity
    
    



def main():
    print("Hello, welcome to the shop.")
    amount = random.uniform(100.0, 5000.0) 
    amount = round(amount, 2)
    print("You have "+str(amount)+" with you")
    shopping(amount)
