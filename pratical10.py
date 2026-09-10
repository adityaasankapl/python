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
            new_price = input("enter new price :")
            price[index] = new_price
            print("price updated successfull !!")

        else:
            print("price not found !!")

    elif choice == 4:
        product3 = input("Enter the product to delete :")

        if product3 in product:
            product.index(product3)
            index = product.index(product3)
            product.pop(index)
            price.pop(index)
            print("product deleted Successfully !!!") 

        else:
            print("product not found !!!")        

    elif choice == 5:    
        product4 = input("Enter the product to search :")

        if product4 in product:
            product.index(product4)
            index = product.index(product4)
            print("Search product !!")
            print("product\tprice")
            print(product[index],"\t",price[index])

        else:
            print("product not found !!!")

    elif choice == 6:
        for i in range(len(product)):
            for j in range(i+1 , len(product)):

                if price[i]>price[j]:
                    price[i],price[j] = price[j],price[i]
                    product[i],product[j] = product[j],product[i]
                    print("sorted successfuly !!!")
                print(product)
                print(price)

    elif choice == 7:
        print("Thank you for buying Product !!!")
        break

    else:
        print("Invalid choice !!!")
