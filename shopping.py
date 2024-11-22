import random
def shopping(amount):
    items={'jackets':25.99, 'sweater':15.50, 't-shirts':13.69, 'jeans': '16.49', 'sweatpants':'20.99','sneakers':14.79, 
    'pencils':0.99, 'pens': 1.99, 'eraser':1.59, 'notebooks':2.99, 'binders':5.99, 'folders': 2.59}

def main():
    print("Hello, welcome to the shop.")
    amount = random.uniform(1.0, 1000.0) 
    amount = round(amount, 2)
