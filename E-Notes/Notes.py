
choice=0
enotes = {}
while(choice!=4) :
    
    print("""
        Welcome to python E-note
        Press 1 for generate note
        Press 2 for view note
        Press 4 for exit
    """)
    choice = int(input("enter choice : "))
    if choice==1:
        print("*****generate notes*****")
        name = input("enter name : ")
        title = input("enter Titel : ")
        content = input("enter content : ")
        enotes.update({name:{"title":title,"content":content}})

    elif choice==2:
        print("*****View notes******")
        print(enotes)
    elif choice==4:
        print("*****Exit*****")
    else:
        print("Invalid input")