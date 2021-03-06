from book import Movie
global row
global seats

row=int(input("Enter the number of rows: "))
seats=int(input("Enter the number of seats in each row: "))
while True:
    print("*** Welcome to Bookyourmovies ***")
    catlog=input("1. show seats\n2.Buy tickets\n3.view statistics\n4. show booked tickets customer info\n0.exit\n\n")

    obj=Movie()
    if catlog == "1":
        obj.show_seats(row,seats)
    elif catlog == "2":
        obj.buy_tickets(row,seats)
    elif catlog == "3":
        obj.show_statistics(row,seats)
    elif catlog =="4":
        obj.show_booked_tickets()
    elif catlog == "0":
        break




