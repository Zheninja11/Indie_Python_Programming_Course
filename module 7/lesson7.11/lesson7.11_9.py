product_dict = {}

while True:
    product = input()
    if product == 'конец':
        break
    else:
        name_product, price = product.split(': ')
        product_dict[name_product] = int(price)

product_dict = sorted(product_dict.items(), key= lambda x: x[1], reverse=True)

for item in product_dict:
    print(item[0])
