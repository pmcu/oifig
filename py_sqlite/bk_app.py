import database

MENU_PROMPT = """
--- Leabhar App ---
Roghnaigh gníomh as an chlár:

1) Cuir leabhar isteach.
2) Taispeántar gach leabhar.
3) Faigh leabhar de réir teidil.
4) Faigh leabhar de réir noid.
5) Scrios leabhar de réir id.
6) Exit.

Do rogha:
"""

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "6":
        #print(user_input)

        if user_input == "1":
            nod = input("Cuir nod ann: ")
            teideal = input("Cuir teideal ann: ")
            udar = input("Cuir udar ann: ")
            bp = input("Cuir bliain phróiseála ann: ")

            database.add_book(connection,nod, teideal, udar,bp)

            

        elif user_input == "2":
            pass

            books = database.get_all_books(connection)
#
            for book in books:
                 print(book)
#
        elif user_input == "3":
            pass
            teideal = input("Cuir isteach teideal leabhair a ba mhaith leat: ")
            books = database.get_books_by_teideal(connection,teideal)
 
 
            for book in books:
                print(book)
#
        elif user_input == "4":
            pass
#           name = input("Cuir isteach nod an leabhair: ")
#           books = database.get_books_by_nod(connection,nod)
#
#           for book in books:
#                print(book)
#
#           for book in books:
#                print(book)
#
        elif user_input == "5":
            id = input("Cuir isteach an id: ")
            book = database.delete_item(connection,id)




        else:
           print("Invalid input please try again")
#           print("Invalid input please try again")
#        
#


menu()


