# function of discount 10%
def discount(t):
    if t >= 100:
        finalprice = t - t * 0.1  
        return finalprice
    return t

# Ask about Name of product
NameProdcut = input("what product do u have ? ")
# Ask about Price of product
PriceProduct = int(input("how much do u buy it ? ") )
# Ask about Quantity of product
QuantityProduct = int(input("how much quantity of product do u have ? ") )

Total = PriceProduct * QuantityProduct
# call the function
Finalprice = discount(Total)

print("Product:", NameProdcut)
print("Total =", Total)
print("Discount (10%)=", Total * 0.1)
print("Final price =", Finalprice)
