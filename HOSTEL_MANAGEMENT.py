#RDBMS PROJECT ---------- HOTEL MANAGEMENT SYSTEM
#IMPORTING MODULES
import os
from tkinter import *
import mysql.connector

userlog=mysql.connector.connect(host="localhost",user="root",passwd="vansh",database="hotel_management")
C=userlog.cursor()

def SCREEN_EXIT(SCREEN):
    SCREEN.destroy()
path=os.getcwd()

#--ABOUT SCREEN---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ABOUT_SCREEN():
    AS=Tk()
    AS.geometry('440x489')
    AS.minsize(440,489)
    AS.maxsize(440,489)
    AS.title('About...')
    AS.iconbitmap(path+'\\IMAGES\\favicon.ico')

    label=Label(AS,text="",pady=50)
    label.pack()
    Heading=Button(AS,text=" | A B O U T | ",font=('Elephant',20),fg = 'white',bg='#91d18b', padx=120, pady=40)
    Heading.place(relx = 0.5, anchor='n')

    info=Label(AS,fg='white',bg='#00796b',padx=400,text='''
CREATOR:       PARV JAIN

SESSION:       2023-2024

CLASS  :       CCE - B

SUBJECT:       RDBMS PROJECT''',pady=90)
    info.pack()

    EXIT=Button(AS,text="BACK TO THE MAIN MENU",bg='#FF7F7F',fg='white',command=lambda:SCREEN_EXIT(AS), pady=20,padx=145)
    EXIT.pack()
        


    AS.mainloop()
    
#--RECORDS SCREEN---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def RECORDS_SCREEN():
    RS=Tk()
    RS.geometry('444x515')
    RS.minsize(444,515)
    RS.maxsize(444,515)
    RS.title('RECORDS')
    RS.iconbitmap(path+'\\IMAGES\\favicon.ico')

    label=Label(RS, text="            ",pady=60)
    label.grid(row=0,column=0)#label for better placing

    HEADING=Button(RS,text=" R E C O R D S ",font=('Elephant',20),fg = 'white',bg='#428', padx=100, pady=40)
    HEADING.place(relx = 0.5, anchor='n')

    GUEST=Button(RS,text="GUESTS", padx=86, pady=40, command = GUEST_RECORD)
    GUEST.grid(row=1,column=0)
    STATE=Button(RS,text="STATE", padx=95, pady=40, command = STATE_RECORD)
    STATE.grid(row=1,column=1)
    ROOMS=Button(RS,text="ROOMS", padx=85, pady=40,command=ROOM_RECORD)
    ROOMS.grid(row=2,column=0)
    HOTELS=Button(RS,text="HOTELS", padx=90, pady=40,command=HOTEL_RECORD)
    HOTELS.grid(row=2, column=1)
    RESTAURANT=Button(RS,text="RESTAURANTS",padx=60,pady=40,command=RESTAURANT_RECORD)
    RESTAURANT.grid(columnspan=2,row=3)

    BACK_BUTTON=Button(RS,text="BACK TO THE MAIN MENU",command=lambda:SCREEN_EXIT(RS), padx=146.5, pady=20,bg='#FF7F7F',fg='white')
    BACK_BUTTON.grid(row=5, columnspan=2)#BACK BUTTON
    RS.mainloop()

#--DEPARTMENT RECORD---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def STATE_RECORD():
    DP=Tk()
    DP.title('STATE RECORDS')
    DP.iconbitmap(path+'\\IMAGES\\favicon.ico')
    LB1=Listbox(DP,bg='azure',height=38)
    LB2=Listbox(DP,bg='azure',height=38)
    try:
        C.execute("SELECT * FROM STATE;")
        L=C.fetchall()
        ini=1
        for i in L:
            LB1.insert(ini,i[0])
            LB2.insert(ini,i[1])
            ini=ini+1
    except:
            LB1.insert(1,"NO       ")
            LB2.insert(1,"RECORDS   FOUND      ")
    
    LABEL=Label(DP,text="""STATE RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=2)
    LABEL=Label(DP,text='STATE CODE').grid(row=1,column=0)
    LABEL=Label(DP,text='STATE NAME').grid(row=1,column=1)
    LB1.grid(row=2,column=0)
    LB2.grid(row=2,column=1)

    BACK_BUTTON=Button(DP,text="BACK TO THE LEADERBOARD MENU",command=lambda:SCREEN_EXIT(DP), padx=40, pady=20,bg='#FF7F7F',fg='white').grid(row=4,columnspan=3)

    DP.mainloop()

    
#--ROOM RECORD---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ROOM_RECORD():
    room=Tk()
    room.title('ROOM RECORDS')
    room.iconbitmap(path+'\\IMAGES\\favicon.ico')
    LB1=Listbox(room,bg='azure',height=40)
    LB2=Listbox(room,bg='azure',height=40)
    LB3=Listbox(room,bg='azure',height=40)
    LB4=Listbox(room,bg='azure',height=40)
    
    try:
        C.execute("SELECT * FROM ROOM;")
        L=C.fetchall()
        ini=1
        for i in L:
            if(i[1]=='N'):
                LB3.insert(ini,"NULL")
            else:
                LB3.insert(ini,i[2])
            LB1.insert(ini,i[0])
            LB2.insert(ini,i[1])
            LB4.insert(ini,i[3])
            ini=ini+1
    except:
            LB1.insert(1,"NO       ")
            LB2.insert(1,"RECORDS         ")
            LB3.insert(1,"FOUND          ")


    LABEL=Label(room,text="""ROOM RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=4)
    LABEL=Label(room,text='ROOM NUMBER').grid(row=1,column=0)
    LABEL=Label(room,text='ALLOTED').grid(row=1,column=1)
    LABEL=Label(room,text='GUEST.AADHAR').grid(row=1,column=2)
    LABEL=Label(room,text='HOTEL.NAME').grid(row=1,column=3)
    LB1.grid(row=2,column=0)
    LB2.grid(row=2,column=1)
    LB3.grid(row=2,column=2)
    LB4.grid(row=2,column=3)

    BACK_BUTTON=Button(room,text="BACK TO THE LEADERBOARD MENU",command=lambda:SCREEN_EXIT(room), padx=150, pady=20,bg='#FF7F7F',fg='white').grid(row=4,columnspan=4)


    room.mainloop()
    
#--HOSTEL RECORD---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def HOTEL_RECORD():
    hs=Tk()
    hs.title('HOTEL RECORDS')
    hs.iconbitmap(path+'\\IMAGES\\favicon.ico')
    LB1=Listbox(hs,bg='azure')
    LB2=Listbox(hs,bg='azure')
    LB3=Listbox(hs,bg='azure')
    LB4=Listbox(hs,bg='azure')
    
    try:
        C.execute("SELECT * FROM HOTEL;")
        L=C.fetchall()
        ini=1
        for i in L:
            LB1.insert(ini,i[0])
            LB2.insert(ini,i[1])
            LB3.insert(ini,i[2])
            LB4.insert(ini,i[3])
            ini=ini+1
    except:
            LB1.insert(1,"NO       ")
            LB2.insert(1,"RECORDS         ")
            LB3.insert(1,"FOUND          ")


    LABEL=Label(hs,text="""HOTEL RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=4)
    LABEL=Label(hs,text='NAME').grid(row=1,column=0)
    LABEL=Label(hs,text='MANAGER').grid(row=1,column=1)
    LABEL=Label(hs,text='GENDER').grid(row=1,column=2)
    LABEL=Label(hs,text='RESTAURANT_ID').grid(row=1,column=3)
    LB1.grid(row=2,column=0)
    LB2.grid(row=2,column=1)
    LB3.grid(row=2,column=2)
    LB4.grid(row=2,column=3)

    BACK_BUTTON=Button(hs,text="BACK TO THE LEADERBOARD MENU",command=lambda:SCREEN_EXIT(hs), padx=150, pady=20,bg='#FF7F7F',fg='white').grid(row=4,columnspan=4)


    hs.mainloop()

#--MESS RECORD---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def RESTAURANT_RECORD():
    ms=Tk()
    ms.title('RESTAURANT RECORDS')
    ms.iconbitmap(path+'\\IMAGES\\favicon.ico')
    LB1=Listbox(ms,bg='azure')
    LB2=Listbox(ms,bg='azure')
    LB3=Listbox(ms,bg='azure')
    LB4=Listbox(ms,bg='azure')
    
    try:
        C.execute("SELECT * FROM RESTAURANT;")
        L=C.fetchall()
        ini=1
        for i in L:
            LB1.insert(ini,i[0])
            LB2.insert(ini,i[1])
            LB3.insert(ini,i[2])
            LB4.insert(ini,i[3])
            ini=ini+1
    except:
            LB1.insert(1,"NO       ")
            LB2.insert(1,"RECORDS         ")
            LB3.insert(1,"FOUND          ")


    LABEL=Label(ms,text="""RESTAURANT RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=4)
    LABEL=Label(ms,text='RESTAURANT_ID').grid(row=1,column=0)
    LABEL=Label(ms,text='TYPE').grid(row=1,column=1)
    LABEL=Label(ms,text='BUFFET CHARGES').grid(row=1,column=2)
    LABEL=Label(ms,text='MANAGER').grid(row=1,column=3)
    LB1.grid(row=2,column=0)
    LB2.grid(row=2,column=1)
    LB3.grid(row=2,column=2)
    LB4.grid(row=2,column=3)

    BACK_BUTTON=Button(ms,text="BACK TO THE LEADERBOARD MENU",command=lambda:SCREEN_EXIT(ms), padx=150, pady=20,bg='#FF7F7F',fg='white').grid(row=4,columnspan=4)


    ms.mainloop()
#--STUDENT RECORD---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def GUEST_RECORD():
    student=Tk()
    student.title('GUEST RECORDS')
    student.iconbitmap(path+'\\IMAGES\\favicon.ico')
    LB1=Listbox(student,bg='azure',height=25)
    LB2=Listbox(student,bg='azure',height=25)
    LB3=Listbox(student,bg='azure',height=25)
    LB4=Listbox(student,bg='azure',height=25)
    
    try:
        C.execute("SELECT * FROM GUEST;")
        L=C.fetchall()
        ini=1
        for i in L:
            LB1.insert(ini,i[0])
            LB2.insert(ini,i[1])
            LB3.insert(ini,i[2])
            LB4.insert(ini,i[3])
            ini=ini+1
    except:
            LB1.insert(1,"NO       ")
            LB2.insert(1,"RECORDS         ")
            LB3.insert(1,"FOUND          ")


    LABEL=Label(student,text="""GUEST RECORDS""",font=('Elephant',20),fg='red').grid(row=0,columnspan=4)
    LABEL=Label(student,text='AADHAR').grid(row=1,column=0)
    LABEL=Label(student,text='NAME').grid(row=1,column=1)
    LABEL=Label(student,text='GENDER').grid(row=1,column=2)
    LABEL=Label(student,text='STATE_CODE').grid(row=1,column=3)
    LB1.grid(row=2,column=0)
    LB2.grid(row=2,column=1)
    LB3.grid(row=2,column=2)
    LB4.grid(row=2,column=3)

    BACK_BUTTON=Button(student,text="BACK TO THE LEADERBOARD MENU",command=lambda:SCREEN_EXIT(student), padx=150, pady=20,bg='#FF7F7F',fg='white').grid(row=4,columnspan=4)


    student.mainloop()
#--NEW REGISTRATION PAGE--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def NEW_REGISTRATION():
    NR=Tk()
    NR.geometry('750x250')
    NR.title('NEW REGISTRATION')
    NR.iconbitmap(path+'\\IMAGES\\favicon.ico')
    LABEL=Label(NR,text="""                                NEW REGISTRATION""",font=('Elephant',20),fg='#428').grid(row=0,columnspan=2)
    LABEL=Label(NR,text="""                 """,font=('Elephant',20),fg='red').grid(row=1,columnspan=2)
    label=Label(NR,text="NAME   : ").grid(row=1,column=0)
    label=Label(NR,text="AADHAR : ").grid(row=2,column=0)
    def REGISTER(gender_button_var,DEPT_VALUE):
        #--DATA COLLECTION
        name=entry.get()
        aadhar=entry2.get()
        DEPT=DEPT_VALUE.get()
        GENDER=GENDER_VALUE.get()
        C.execute("SELECT * FROM STATE WHERE STATE_NAME='"+DEPT+"';")
        L=C.fetchall()
        dept_code=L[0][0]
        C.execute("SELECT * FROM ROOM WHERE ALLOTED='N'")
        L=C.fetchall()
        emptyroom=L[0][0]
        #--DATA PROCESSING------------------------------------------------------------------
        C.execute("START TRANSACTION")
        C.execute("INSERT INTO GUEST(AADHAR,NAME,GENDER,STATE_CODE) VALUES('"+str(aadhar)+"','"+name+"','"+GENDER+"',"+str(dept_code)+");")
        C.execute("UPDATE ROOM SET ALLOTED='Y',AADHAR="+str(aadhar)+" WHERE ROOM_NO="+str(emptyroom)+";")


        
        SCREEN_EXIT(NR)

    global entry
    entry=Entry(NR)
    entry.focus_set()
    entry.grid(row=1,column=1)

    global entry2
    entry2=Entry(NR)
    entry2.focus_set()
    entry2.grid(row=2,column=1)
    
    label=Label(NR,text="GENDER : ").grid(row=3,column=0)
    GENDERLIST=['Male','Female']
    GENDER_VALUE=StringVar(NR)
    GENDER_VALUE.set("Choose gender")
    gender_button_var=OptionMenu(NR,GENDER_VALUE,*GENDERLIST)
    gender_button_var.grid(row=3,column=1)


    label=Label(NR,text="STATE : ").grid(row=4,column=0)
    DEPT_LIST=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
    DEPT_VALUE=StringVar(NR)
    DEPT_VALUE.set("Select a state")
    DEPT_MENU=OptionMenu(NR,DEPT_VALUE,*DEPT_LIST)
    DEPT_MENU.grid(row=4,column=1)


    SUBMIT_BUTTON=Button(NR,text="SUBMIT",bg='light blue',command=lambda:REGISTER(gender_button_var,DEPT_VALUE))
    SUBMIT_BUTTON.grid(row=5,column=0)
    CANCEL_BUTTON=Button(NR,text="CANCEL",bg='#FF7F7F',fg='white',command=lambda:SCREEN_EXIT(NR)).grid(row=5,column=1)

    
    NR.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MAIN PAGE

MAINPAGE=Tk()
MAINPAGE.geometry('580x530')
MAINPAGE.minsize(580,530)
MAINPAGE.maxsize(580,530)
MAINPAGE.title('HOTEL MANAGEMENT')
MAINPAGE.iconbitmap(path+'\\IMAGES\\favicon.ico')

label=Label(MAINPAGE,text="",pady=40)
label.grid(row=0,column=0)

photo1=PhotoImage(file = path+'\\IMAGES\\HOTEL MANAGEMENT.gif')
image=Label(MAINPAGE,image=photo1,padx=200)
image.place(relx=0.5,anchor='n')
    
    
label2=Label(MAINPAGE,text="==============================================================================",pady=10)
label2.grid(row=1,columnspan=5)


NS=Button(MAINPAGE,text="NEW REGISTRATION",font=("Product Sans",10), padx=220, pady=20,bg='light blue',command = NEW_REGISTRATION)
NS.grid(row=2,columnspan=2)
label=Label(MAINPAGE, text="            ")
label.grid(row=3,column=0)#label for better placing 
RECORDS=Button(MAINPAGE,text="RECORDS",command = RECORDS_SCREEN, font=("Product Sans",10), padx=250,pady=20,bg='light blue')
RECORDS.grid(row=4,columnspan=2)
label=Label(MAINPAGE, text="            ")
label.grid(row=5,column=0)#label for better placing 
ABOUT=Button(MAINPAGE,text="ABOUT...", padx=260 ,command = ABOUT_SCREEN, font=("Product Sans",10), pady=20, bg='light blue')
ABOUT.grid(row=6,columnspan=2)
label=Label(MAINPAGE, text="            ", pady=30)
label.grid(row=7,columnspan=2)#label for better placing
EXIT=Button(MAINPAGE,text="EXIT",pady=20, command=lambda:SCREEN_EXIT(MAINPAGE),fg='white',font=('Elephant'),bg='#FF7F7F',padx=240)
EXIT.grid(row=8,columnspan=2)

MAINPAGE.mainloop()

