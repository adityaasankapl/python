product =[]
price=[]

while True:

    print("\n----------product list---------")
    print("1.Add the product: ")
    print("2.Display the product: ")
    print("3.update the product: ")
    print("4.delete the product: ")
    print("5.search the product: ")
    print("6.sort the product: ")
    print("7.exit:")

    choice =int(input("Enter the choice :"))

    if choice ==1:
        product1 = input("Enter the product :")
        price1 = input("Enter the price : ")
        product.append(product1)
        price.append(price1)
        print("Product enter successfully !!!")

    elif choice == 2:
        if  len(product)==0:
            print("product is not avilable :")

        else:
            print("product\tprice")
            for i in range(len(product)):
                print(product[i],"\t",price[i])

    elif choice == 3: 
        product2 = input("Enter the product name to update there price :")

        if product2 in product:
            product.index(product2)
            index =  product.index(product2)
            