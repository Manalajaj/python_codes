def add_product(name,quantity):
    for product in products:
        if product['name'] == name:
            product['quantity'] += quantity
            break
    else:
        price = float(input('enter price :'))
        product = {'name': name, 'quantity': quantity, 'price': price}
        products.append(product)
def remove_product(name,quantity):
    if not products:
        print('Not found ayy product to remove')
        return
    for product in products:
        if product['name'] == name:
            if product['quantity'] < quantity:
                print(f'Quantity of product is :{product["quantity"]}')
            else:
                product['quantity'] -= quantity
                if product['quantity'] == 0:
                    products.remove(product)
                print('Remove is done')
        else:
            print('Not found product')
def display_product():
    if len(products) == 0:
        print('Not found products')
    else:
        for product in products:
            print(f'product name : {product["name"]} ,'
                  f'Quantity : {product["quantity"]}, '
                  f'price : {product["price"]}')
products=[]
while True:
    print('''
    Enter one of the following choices:
    For add product enter : 1
    For remove product enter : 2
    For display product enter : 3
    For exit enter :4
    ''')
    choice = input('enter number :')
    if choice == '1':
        product_name = input('enter name of product :')
        product_quantity = int(input('enter quantity :'))
        add_product(product_name, product_quantity)
        print('Add is successful')
    elif choice == '2':
        product_name = input('enter name of product :')
        product_quantity = int(input('enter quantity :'))
        remove_product(product_name, product_quantity)
    elif choice == '3':
        display_product()
    elif choice == '4':
        break
    else:
        print('Invalid number')