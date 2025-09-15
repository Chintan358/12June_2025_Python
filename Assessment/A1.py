
stock = {}
sales = {}
flag = 'Y'
while flag.upper() != 'N':
    choice = int(input("""Enter choice for operations : 
        1 : Sales
        2 : Manager
        """))

   
    if choice == 1 :
        s_flag = 'Y'
        while s_flag.upper() !='N':
            s_choice = int(input("""
            1 : Create order
            2 : View Order
            """))
            if s_choice==1:
                cname = input("enter custome rname : ")
                pname = input("Enter product name :")
                qty = int(input("Enter Qty : "))
                
                product =  stock.get(pname)
                if qty > product['qty']:
                    print("Product not avalible")
                else : 
                    sales.update({cname:{"pname":pname,"price":product['price'],"qty":qty}})
                    stock[pname]={"price":product['price'],"qty":product['qty']-qty}
                    print("success")

            elif s_choice==2:
                print(sales)
            else : 
                print("Invalid choice")
            
            s_flag = input("Do u want to continue as a Sales ? y or n")  



    elif choice == 2:
        m_flag = 'Y'
        while m_flag.upper() !='N':
            m_choice = int(input("""
            1 : Add Stock
            2 : View Stock
            """))
            if m_choice==1:
                name = input("Enter product name :")
                price = float(input("Enter price :"))
                qty = int(input("Enter Qty : "))
                stock.update({name.lower() : {"price":price,"qty":qty}})
            elif m_choice==2:
                print(stock)
            else : 
                print("Invalid choice")
            
            m_flag = input("Do u want to continue as a manager ? y or n")

    else :
        print("Invalid choice")

    flag = input("Do u want to Continue ? y or n")