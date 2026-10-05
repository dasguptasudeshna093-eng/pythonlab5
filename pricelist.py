product={'apple':120, "banana":80, "orange":100, "grapes":150, "grape":150}
x=input("Enter the product name: ")
if x in product:
    print(f"The price of {x} is {product[x]}")
else:
    price=int(input("Product not found.Enter price-"))
    product[x]=price
    print(f"Product added with price {price}")
print(product)