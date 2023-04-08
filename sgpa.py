
 
 
# Import tkinter as tk
import tkinter as tk

 
 
# creating a new tkinter window
window = tk.Tk()
 
# assigning a title
window.title("SGPA CALCULATOR")
 
# specifying geometry for window size
window.geometry("700x270")
 
 
# declaring objects for entering data
Entry1 = tk.Entry(window)
Entry2 = tk.Entry(window)
Entry3 = tk.Entry(window)
#Entry4 = tk.Entry(window)
#Entry5 = tk.Entry(window)
#Entry6 = tk.Entry(window)
#Entry7 = tk.Entry(window)
Entry8 = tk.Entry(window)
Entry9 = tk.Entry(window)
Entry10 = tk.Entry(window)
Entry11 = tk.Entry(window)
Entry12 = tk.Entry(window)
Entry13 = tk.Entry(window)
Entry14 = tk.Entry(window)
Entry15 = tk.Entry(window)

tot=0
total=0
GradeL=['O','A+','A','B+','C','F','Ab']

        
Entry4=tk.StringVar()
Entry4.set("Grade 1")
dropG1=tk.OptionMenu(window,Entry4,*GradeL)
dropG1.grid(row=5,column=2)

Entry5=tk.StringVar()
Entry5.set("Grade 2")
dropG1=tk.OptionMenu(window,Entry5,*GradeL)
dropG1.grid(row=6,column=2)

Entry6=tk.StringVar()
Entry6.set("Grade 3")
dropG1=tk.OptionMenu(window,Entry6,*GradeL)
dropG1.grid(row=7,column=2)

Entry7=tk.StringVar()
Entry7.set("Grade 4")
dropG1=tk.OptionMenu(window,Entry7,*GradeL)
dropG1.grid(row=8,column=2)


 
# function to display the total credits and SGPA
def display():
 
    # Variable to store total marks
    global tot
    global total
    tot = 0
 
   
    # give total credits for grade A
    if Entry4.get() == "O":
        tot += (int(cv1.get())*10)

    # total credits for grade B
    if Entry4.get() == "A+":
        tot += (int(cv1.get())*9)


    # total credits for grade C
    if Entry4.get() == "A":
        tot += (int(cv1.get())*8)
     
 

    # give total credits for grade D
    if Entry4.get() == "B+":
        tot += (int(cv1.get())*7)
        

    # total credits for grade P
    if Entry4.get() == "B":
      
        tot += (int(cv1.get())*6)

    if Entry4.get() == "C":

        tot += (int(cv1.get())*5)
 

    # total credits for grade F
    if Entry4.get() == "F":
      
        tot += 0

    if Entry4.get() == "Ab":
        tot += 0
 
   # 10*number of subject credits
    # give total credits for grade A
    if Entry5.get() == "O":

        tot += (int(cv2.get())*10)
 
    # 9*number of subject credits give
    # total credits for grade B
    if Entry5.get() == "A+":
      
        tot += (int(cv2.get())*9)
 
    # 8*number of subject credits give
    # total credits for grade C
    if Entry5.get() == "A":
    
        tot += (int(cv2.get())*8)
 
    # 7*number of subject credits
    # give total credits for grade D
    if Entry5.get() == "B+":
        tot += (int(cv2.get())*7)
 
    # 6*number of subject credits give
    # total credits for grade P
    if Entry5.get() == "B":
       
        tot += (int(cv2.get())*6)

    if Entry5.get() == "C":
        
        tot += (int(cv2.get())*5)
 
    # 0*number of subject credits give
    # total credits for grade F
    if Entry5.get() == "F":
        
        tot += 0

    if Entry5.get() == "Ab":
 
        tot += 0
 
   # 10*number of subject credits
    # give total credits for grade A
    if Entry6.get() == "O":
 
        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
      
        tot += (int(cv3.get())*10)
 
    # 9*number of subject credits give
    # total credits for grade B
    if Entry6.get() == "A+":
      
        tot += (int(cv3.get())*9)
 
    # 8*number of subject credits give
    # total credits for grade C
    if Entry6.get() == "A":
       tot += (int(cv3.get())*8)
 
    # 7*number of subject credits
    # give total credits for grade D
    if Entry6.get() == "B+":
        tot += (int(cv3.get())*7)
 
    # 6*number of subject credits give
    # total credits for grade P
    if Entry6.get() == "B":
      
        tot += (int(cv3.get())*6)

    if Entry6.get() == "C":
      
        tot += (int(cv3.get())*5)
 
    # 0*number of subject credits give
    # total credits for grade F
    if Entry6.get() == "F":

        tot += 0

    if Entry6.get() == "Ab":
        
        tot += 0

      
   # 10*number of subject credits
    # give total credits for grade A
    if Entry7.get() == "O":
 
        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
       
        tot += (int(cv4.get())*10)
 
    # 9*number of subject credits give
    # total credits for grade B
    if Entry7.get() == "A+":

        tot += (int(cv4.get())*9)
 
    # 8*number of subject credits give
    # total credits for grade C
    if Entry7.get() == "A":
        
        tot += (int(cv4.get())*8)
        
    # 7*number of subject credits
    # give total credits for grade D
    if Entry7.get() == "B+":
 
        tot += (int(cv4.get())*7)
 
    # 6*number of subject credits give
    # total credits for grade P
    if Entry7.get() == "B":
      
        tot += (int(cv4.get())*6)

    if Entry7.get() == "C":
    
        tot += (int(cv4.get())*5)
 
    # 0*number of subject credits give
    # total credits for grade F
    if Entry7.get() == "F":
        
        tot += 0

    if Entry7.get() == "Ab":
       
        tot += 0
    # to display total credits
    Tot=int(cv1.get())+int(cv2.get())+int(cv3.get())+int(cv4.get())
    tk.Label(window, text=str(Tot),fg='red').grid(row=9, column=4)

  
    # to display SGPA
    total=round(tot/Tot,2)
    tk.Label(window, text=str(total),fg='red').grid(row=10, column=4)


    import mysql.connector as sqltor   # Imports database programming package
    mycon=sqltor.connect(host="localhost",user="root",passwd="Rishy@1307",database="GPA")
    # Establishes connecton with the database dropdead stored in mysql  
    mycursor=mycon.cursor()   #  Creates a cursor instance that is used to execute queries on the database
    
    query="insert into Student(Name,RegNo,Semester,Dept,SGPA) values('{}','{}',{},'{}',{})".format(Entry1.get(),Entry2.get(),Entry3.get(),Entry15.get(),total)
    # Inserts the Winner's name,score in the table Leaderboard 
    mycursor.execute(query)  # Query executed  
    mycon.commit()
    # Permanent changes made to the table
    mycon.close()   # Cleans up the environment
 
 
# end of display function
 
# label to enter name
tk.Label(window, text="Name").grid(row=0, column=0)
 
# label for registration number
tk.Label(window, text="Reg.No").grid(row=0, column=3)
 
# label for roll Number
tk.Label(window, text="Semester").grid(row=1, column=0)

# label for dept.
#tk.Label(window,text="Dept.").grid(row=1,coloumn=3)

 
# labels for serial numbers
tk.Label(window, text="Srl.No").grid(row=4, column=0)
tk.Label(window, text="1").grid(row=5, column=0)
tk.Label(window, text="2").grid(row=6, column=0)
tk.Label(window, text="3").grid(row=7, column=0)
tk.Label(window, text="4").grid(row=8, column=0)
 


    

tk.Label(window, text="Subject").grid(row=4, column=1)


sub=['18CSS207J','18CSC205J','18CSS202J','18MAB202T','18CSC208L','18PDH103T','18CSC204J','18CYM101T','18MAB102T']

        
curVar=tk.StringVar()
curVar.set("Subject 1")
drop=tk.OptionMenu(window,curVar,*sub)
drop.grid(row=5,column=1)


curVar2=tk.StringVar()
curVar2.set("Subject 2")
drop2=tk.OptionMenu(window,curVar2,*sub)
drop2.grid(row=6,column=1)

curVar3=tk.StringVar()
curVar3.set("Subject 3")

drop3=tk.OptionMenu(window,curVar3,*sub)
drop3.grid(row=7,column=1)

curVar4=tk.StringVar()
curVar4.set("Subject 4")
drop4=tk.OptionMenu(window,curVar4,*sub)
drop4.grid(row=8,column=1)

#Entry11.grid(row=5, column=1)
#Entry12.grid(row=6, column=1)
#Entry13.grid(row=7, column=1)
#Entry14.grid(row=8, column=1)

# tk.Label(window, text="18CSC203J").grid(row=3, column=1)
# tk.Label(window, text="18PDT102T").grid(row=4, column=1)
# tk.Label(window, text="18MAB204T").grid(row=5, column=1)
# tk.Label(window, text="18CSS201J").grid(row=6, column=1)
 
 
# label for grades
tk.Label(window, text="Grade").grid(row=4, column=2)
#Entry4.grid(row=5, column=2)
#Entry5.grid(row=6, column=2)
#Entry6.grid(row=7, column=2)
#Entry7.grid(row=8, column=2)

# labels for subject credits

cv1 = tk.StringVar(value=0)
cv2 = tk.StringVar(value=0)
cv3 = tk.StringVar(value=0)
cv4 = tk.StringVar(value=0)

tk.Label(window, text="Sub Credit").grid(row=4, column=3)
w1=tk.Spinbox(window,from_=0, to_=5,textvariable=cv1,wrap=True).grid(row=5,column=3)
w2=tk.Spinbox(window,from_=0, to_=5,textvariable=cv2,wrap=True).grid(row=6,column=3)
w3=tk.Spinbox(window,from_=0, to_=5,textvariable=cv3,wrap=True).grid(row=7,column=3)
w4=tk.Spinbox(window,from_=0, to_=5,textvariable=cv4,wrap=True).grid(row=8,column=3)


'''tk.Label(window, text="4").grid(row=3, column=3)
tk.Label(window, text="4").grid(row=4, column=3)
tk.Label(window, text="3").grid(row=5, column=3)
tk.Label(window, text="4").grid(row=6, column=3)'''
 

# taking entries of name, reg, roll number respectively
Entry1 = tk.Entry(window)
Entry2 = tk.Entry(window)
Entry3 = tk.Entry(window)
 
# organizing them in the grid
Entry1.grid(row=0, column=1)
Entry2.grid(row=0, column=4)
Entry3.grid(row=1, column=1)
Entry15.grid(row=1,column=4)
tk.Label(window,text="Dept.").grid(row=1,column=3)
#Entry15.grid(row=1,column=4)
 
# button to display all the calculated credit scores and sgpa
button1 = tk.Button(window, text="submit", bg="green", command=display)
button1.grid(row=11, column=2)
 
 
tk.Label(window, text="Total credit").grid(row=9, column=3)
tk.Label(window, text="SGPA").grid(row=10, column=3)
 


window.mainloop()
