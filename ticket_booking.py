
class Star_Cinema:
    Hall_list=[]
    
    def entery_hall(self,hall):
        Star_Cinema.Hall_list.append(hall)
        
class Hall(Star_Cinema):
    def __init__(self,row,colm,hall_no):
        super().__init__()
        self.seats={}
        self.row=row
        self.colm=colm
        self.hall_no=hall_no
        self.show_list=[]
        self.entery_hall(self)
        
    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self.show_list.append(show)
        
        # self.seats[id]=[]
        # for i in range(self.row):
	    #     colm = []
	    #     for j in range(self.colm):
		#         colm.append(0)
	    #     self.seats.append(colm)
        self.seats[id] = [[0] * self.colm for _ in range(self.row)]
        print("\n\t Show entryed successfully")
        
    def book_seats(self,id,seat_info):
        selected_seat=self.seats.get(id,[])
        
        for row,colm in seat_info:
            selected_seat[row][colm]=1
            
            self.seats[id]=selected_seat
        print(f"Booking 2 seats done Successfully")
    def view_show_list(self):
        
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
       

    def view_available_seats(self, id):
        if id in self.seats:
            print(f"Available seats for show ID {id}:")
            for row in self.seats[id]:
                print(row)
        else:
            print(f"Show ID {id} not found.")
   
    
    
        
    
    
hall = Hall(3, 4, 1)
hall.entry_show(1, "Pathan ", "18:00")
hall.book_seats(1, [(0, 1), (1, 2), (2, 0)])
# hall.view_show_list()
# hall.view_available_seats(1)


run =True

while run:
    print("Option: \n")
    print("1. View All Show todey")
    print("2. View Availaible Seats")
    print("3. Book Tickets")
    print("4. Add Show")
    print("5. Exit")
    
    choice=int(input("\nEnter Option: "))
    
    if choice==1:
        print("\n Today's Show  ")
        hall.view_show_list()
        
    if choice==2:
        id=int(input("Enter Show_Id: "))
        hall.view_available_seats(id)
        
    if choice==3:
        id=int(input("Enter Show Id: "))
        tik=int(input("\n how many ticket you want to buy: "))
        
        for i in range(tik):
            row=int(input("\n\tEnter Row: "))
            colm=int(input("\n\tEnter Colm:"))
            seat=[(row,colm)]
            
        hall.book_seats(id,seat)
            
    if choice==4:
        id=int(input("\n Enter id: "))
        Movie_name=input("\n Enter Movie Name: ")
        time=input("\n Enter Show time: ")
        hall.entry_show(id, Movie_name, time)
        
    if choice==5:
        run= False
        
        
        
        