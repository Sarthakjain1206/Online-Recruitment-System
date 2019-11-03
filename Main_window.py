from tkinter import *
from tkinter import messagebox
import pandas as pd
import sqlite3
# from Apply_job_window import job_window
conn = sqlite3.connect('OnlineRecruitment.db')
c = conn.cursor()

####################################### For jobseeker registeration window
def focus1(event): 
	password_field.focus_set() 
# Function to set focus 
def focus2(event): 
	can_name_field.focus_set() 
# Function to set focus 
def focus3(event): 
	CV_field.focus_set() 
# Function to set focus 
def focus4(event):
	projects_field.focus_set() 
# Function to set focus 
def focus5(event):
	father_name_field.focus_set() 
# Function to set focus
def focus6(event): 
	DOB_field.focus_set() 
def focus7(event): 
	contact_field.focus_set() 
#######################################

################## For employer registeration window
def focus11(event):
    password_emp_field.focus_set()
def focus12(event):
    emp_name_field.focus_set()
def focus13(event):
    emp_id_field.focus_set()
def focus14(event):
    email_field.focus_set()
def focus15(event):
    information_field.focus_set()
##################
def focus21(event):
    password_jobseeker_field.focus_set()
def focus31(event):
    password_employer_field.focus_set()
##################
def focus41(event):
    technical_field.focus_set()
def focus42(event):
    academic_qualifications_field.focus_set()
def focus43(event):
    cocurricular_activities_field.focus_set()
def focus44(event):
    package_field.focus_set()
def focus45(event):
    criteria_field.focus_set()
################ for clearing text in enteries of jobseeker registeration window
def clear():
    username_field.delete(0,END)
    password_field.delete(0,END)
    can_name_field.delete(0,END)
    CV_field.delete(0,END)
    projects_field.delete(0,END)
    father_name_field.delete(0,END)
    DOB_field.delete(0,END)
    contact_field.delete(0,END)
################# for clearing text in enteries of employer registeration window
def clear2():
    username_emp_field.delete(0,END)
    password_emp_field.delete(0,END)
    emp_name_field.delete(0,END)
    emp_id_field.delete(0,END)
    information_field.delete(0,END)
    email_field.delete(0,END)
def clear3():
    post_field.delete(0,END)
    technical_field.delete(0,END)
    cocurricular_activities_field.delete(0,END)
    academic_qualifications_field.delete(0,END)
    criteria_field.delete(0,END)
    package_field.delete(0,END)

#################  

############-------->>> All functions for managing the databases
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def insert_jobseeker_id_password(table,can_id,username,password):
    try:
        sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_jobseeker_username_query = f"INSERT INTO {table}(can_id,'username','password') VALUES (?,?,?)"

        # Convert data into tuple format
        data_tuple = (can_id,username,password)
        cursor.execute(sqlite_insert_jobseeker_username_query, data_tuple)
        sqliteConnection.commit()
        print("Data inserted successfully into a employer table")
        cursor.close()
        # return True
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
        # return False
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")
def insert_jobseeker_data(table,can_id, can_name, CV,projects):
    try:
        sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = f"INSERT INTO {table}('can_id', 'can_name', 'CV','projects') VALUES (?, ?, ?,?)"

        can_CV = convertToBinaryData(CV)
        # Convert data into tuple format
        data_tuple = (can_id, can_name,can_CV,projects)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a jobseeker table")
        cursor.close()
        # return True
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
        # return False
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

def insert_personal_info_of_jobseeker(table,can_id,father_name,DOB,contact):
    try:
        sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_info_query = f"INSERT INTO {table}('can_id', 'father_name', 'DOB','contact') VALUES (?, ?, ?,?)"

        # Convert data into tuple format
        data_tuple = (can_id, father_name,DOB,contact)
        cursor.execute(sqlite_insert_info_query, data_tuple)
        sqliteConnection.commit()
        print("Data inserted successfully into a Personal_info table")
        cursor.close()
        # return True
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
        # return False
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

def insert_employer_data(emp_id,emp_name,information,email):
    try:
        sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_employer_query = """ INSERT INTO 'Employer'
                                  ('emp_id', 'emp_name', 'information','email') VALUES (?,?,?,?)"""

        # Convert data into tuple format
        data_tuple = (emp_id, emp_name,information,email)
        cursor.execute(sqlite_insert_employer_query, data_tuple)
        sqliteConnection.commit()
        print("Data inserted successfully into a employer table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

def insert_employer_id_password(emp_id,username,password):
    try:
        sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_employer_username_query = """ INSERT INTO 'employer_data'
                                  (emp_id,'username','password') VALUES (?,?,?)"""

        # Convert data into tuple format
        data_tuple = (emp_id,username,password)
        cursor.execute(sqlite_insert_employer_username_query, data_tuple)
        sqliteConnection.commit()
        print("Data inserted successfully into a employer table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

def insert_skill_data(skill_id,technical,academic_qualifications,cocurricular_activities):
    try:
        sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_skill_query = """ INSERT INTO 'skill'
                                  ('skill_id', 'technical', 'academic_qualifications','cocurricular') VALUES (?,?,?,?)"""

        # Convert data into tuple format
        data_tuple = (skill_id, technical,academic_qualifications,cocurricular_activities)
        cursor.execute(sqlite_insert_skill_query, data_tuple)
        sqliteConnection.commit()
        print("Data inserted successfully into a skill table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into skill table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")
def insert_requistion_data(req_id,emp_id,post,skill_id, package,criteria):
    try:
        sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_requistion_query = """ INSERT INTO 'requistion'
                                    (req_id, emp_id, 'post',skill_id,'package','criteria') VALUES (?,?,?,?,?,?)"""

        # Convert data into tuple format
        data_tuple = (req_id,required_emp_id,post,skill_id, package,criteria)
        cursor.execute(sqlite_insert_requistion_query, data_tuple)
        sqliteConnection.commit()
        print("Data inserted successfully into a requistion table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into requistion table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")


def check_credentials(table,username,password):
    for row in c.execute(f"SELECT * FROM '{table}' where username='{username}' "):
        if password==row[2]:
            return True
        else:
            return False
    return False

############-------->>>
def insert_job_profile_data():
    answer = messagebox.askquestion('Confirmation',"Are you sure you want to submit?")
    if answer=='yes':
        for row in c.execute("SELECT max(skill_id) from skill"):
            temp = row[0]
        skill_id = temp+1
    
        for row in c.execute("SELECT max(req_id) from requistion"):
            temp2 = row[0]
        req_id = temp2+1
        
        insert_skill_data(skill_id,technical_field.get(),academic_qualifications_field.get(),cocurricular_activities_field.get())
        insert_requistion_data(req_id,required_emp_id,post_field.get(),skill_id,package_field.get(),criteria_field.get())
        # messagebox.showerror("Error","Data is Not Inserted Bcoz of Integrity error that means you might have violated the database rules. Please Enter Your Actual Details..")
        messagebox.showinfo("Window","Your Data has submitted..")
        post_field.focus_set()
        clear3()
    else:
        messagebox.showinfo("Window","You chose, Not to submit data..")

def insert_job_profile_window():
    job_window = Toplevel(root_employer_window)
    job_window.configure(background="#cad1db")
    job_window.title("Post Job")
    job_window.geometry("600x350")

    heading = Label(job_window,text="Provide skills and details for Job",bg="#cad1db",fg="black",font=("Times",16,"bold italic underline"),pady=5)

    post = Label(job_window, text="Job Title", bg="#c3d2de")
    technical = Label(job_window, text="Technical Skills", bg="#c3d2de")
    academic_qualifications = Label(job_window, text="Academic Qualifications", bg="#c3d2de")
    cocurricular_activities = Label(job_window, text="Cocurricular Activities", bg="#c3d2de")
    package = Label(job_window, text="Salary Package", bg="#c3d2de")
    criteria = Label(job_window, text="Criteria of Hiring", bg="#c3d2de")

    heading.grid(row=0,column=1)
    post.grid(row=1,column=0)
    technical.grid(row=2,column=0)
    academic_qualifications.grid(row=3,column=0)
    cocurricular_activities.grid(row=4,column=0)
    package.grid(row=5,column=0)
    criteria.grid(row=6,column=0)
    global post_field,technical_field,academic_qualifications_field,cocurricular_activities_field,package_field,criteria_field
    post_field = Entry(job_window,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    technical_field = Entry(job_window,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    academic_qualifications_field = Entry(job_window,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    cocurricular_activities_field = Entry(job_window,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    package_field = Entry(job_window,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    criteria_field = Entry(job_window,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 

    post_field.grid(row=1,column=1,ipadx=100,ipady=5)
    technical_field.grid(row=2,column=1,ipadx=100,ipady=7)
    academic_qualifications_field.grid(row=3,column=1,ipadx=100,ipady=8)
    cocurricular_activities_field.grid(row=4,column=1,ipadx=100,ipady=8)
    package_field.grid(row=5,column=1,ipadx=100,ipady=5)
    criteria_field.grid(row=6,column=1,ipadx=100,ipady=10)
    
    post_field.bind("<Return>",focus41)
    technical_field.bind("<Return>",focus42)
    academic_qualifications_field.bind("<Return>",focus43)
    cocurricular_activities_field.bind("<Return>",focus44)
    package_field.bind("<Return>",focus45)

    submit = Button(job_window, text="Submit", fg="white", bg="#3e434a",pady='5',command=insert_job_profile_data) 
    submit.grid(row=7, column=1,ipadx='10')

################################################################ ALL FUNCTIONS FOR JOB SEARCH/APPLY WINDOW #####################
def focus_1(event):
    package_text.focus_set()
def focus_2(event):
    emp_name_text.focus_set()
def isExit():
    isExit = messagebox.askyesno("Apply For Job","Confirm if you want to exit")
    if isExit>0:
        apply_job_window.destroy()
        return
def normal_states():
    post_text.config(state=NORMAL)
    technical_text.config(state=NORMAL)
    academic_qualifications_text.config(state=NORMAL)
    cocurricular_activities_text.config(state=NORMAL)
    emp_name_text.config(state=NORMAL)
    information_text.config(state=NORMAL)
    package_text.config(state=NORMAL)
    criteria_text.config(state=NORMAL)

def clearData():
    normal_states()

    post_text.delete(0,END)
    technical_text.delete(0,END)
    academic_qualifications_text.delete(0,END)
    cocurricular_activities_text.delete(0,END)
    emp_name_text.delete(0,END)
    information_text.delete(0,END)
    package_text.delete(0,END)
    criteria_text.delete(0,END)

    academic_qualifications_text.config(state=DISABLED)
    cocurricular_activities_text.config(state=DISABLED)
    criteria_text.config(state=DISABLED)
    information_text.config(state=DISABLED)
    technical_text.config(state=DISABLED)

def display_jobs():
    jobpost_list.delete(0,END)
    sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
    cursor = sqliteConnection.cursor()
    for rows in cursor.execute("""SELECT post,technical,academic_qualifications,cocurricular,package,criteria,emp_name,information from
            ((requistion INNER JOIN skill ON requistion.skill_id=skill.skill_id)
            INNER JOIN Employer on requistion.emp_id=Employer.emp_id)"""):
        
        jobpost_list.insert(END,rows,str(""))
    button_display.config(state=DISABLED)

def job_details_rec(event):
    global job_record
    key = jobpost_list.curselection()[0]
    job_record = jobpost_list.get(key)
    
    normal_states()
    post_text.delete(0,END)
    post_text.insert(END,job_record[0])
    technical_text.delete(0,END)
    technical_text.insert(END,job_record[1])
    academic_qualifications_text.delete(0,END)
    academic_qualifications_text.insert(END,job_record[2])
    cocurricular_activities_text.delete(0,END)
    cocurricular_activities_text.insert(END,job_record[3])
    package_text.delete(0,END)
    package_text.insert(END,job_record[4])
    criteria_text.delete(0,END)
    criteria_text.insert(END,job_record[5])
    emp_name_text.delete(0,END)
    emp_name_text.insert(END,job_record[6])
    information_text.delete(0,END)
    information_text.insert(END,job_record[7])

    academic_qualifications_text.config(state='readonly')
    cocurricular_activities_text.config(state='readonly')
    package_text.config(state='readonly')
    criteria_text.config(state='readonly')
    information_text.config(state='readonly')
    technical_text.config(state='readonly')
    emp_name_text.config(state='readonly')
    post_text.config(state='readonly')

def search_job():
    search_job_post(j_post.get(),j_emp_name.get(),j_package.get())
def search_job_post(j_post='', j_emp_name='',j_package=''):
    button_display.config(state=NORMAL)
    jobpost_list.delete(0,END)
    try:
        sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        # Convert data into tuple format
        data_tuple = (j_post, j_emp_name,j_package)
        print(data_tuple)
        for row in cursor.execute("""SELECT post,technical,academic_qualifications,cocurricular,package,criteria,emp_name,information from
                        ((requistion INNER JOIN skill ON requistion.skill_id=skill.skill_id) INNER JOIN Employer on requistion.emp_id=Employer.emp_id)
                        WHERE post=? OR emp_name=? OR package=?""", data_tuple):
            jobpost_list.insert(END,row,str(""))
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to search data from requistion table", error)
        return -1
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

def apply_for_job():
    # print(post.get(),technical.get(),academic_qualifications.get(),cocurricular_activities.get())
    sqliteConnection = sqlite3.connect('OnlineRecruitment.db')
    cursor = sqliteConnection.cursor()
    cursor.execute(f"SELECT can_id from jobseeker_data where username='{username_jobseeker_field.get()}' ")
    required_can_id=cursor.fetchone()[0]
    
    cursor.execute(f"SELECT skill_id from skill where technical='{j_technical.get()}' AND academic_qualifications='{j_academic_qualifications.get()}' AND cocurricular='{j_cocurricular_activities.get()}' ")
    temp2 = cursor.fetchone()[0]
    
    cursor.execute(f"SELECT req_id from requistion where skill_id='{temp2}' ")
    required_req_id = cursor.fetchone()[0]
    
    cursor.execute("SELECT MAX(app_id) FROM applications")
    temp = cursor.fetchone()[0]
    required_app_id = temp+1
    cursor.execute("INSERT INTO applications(app_id,req_id,can_id) VALUES(?,?,?)",(required_app_id,required_req_id,required_can_id))
    sqliteConnection.commit()
    print("Data Is Inserted in application table")


def job_window():
    global apply_job_window
    apply_job_window=Toplevel(root4)
    apply_job_window.title("Apply For JOb")
    apply_job_window.geometry("1450x650+0+0")
    apply_job_window.config(bg="#a1bccc")

    global j_post,j_technical,j_academic_qualifications,j_cocurricular_activities,j_package,j_criteria,j_emp_name,j_information
    j_post = StringVar()
    j_technical = StringVar()
    j_academic_qualifications=StringVar()
    j_cocurricular_activities=StringVar()
    j_package=StringVar()
    j_criteria=StringVar()
    j_emp_name=StringVar()
    j_information=StringVar()

    ############################################ FRAMES ################################
    MainFrame = Frame(apply_job_window,bg="#a1bccc")
    MainFrame.grid()

    TitFrame = Frame(MainFrame,bd=6,padx=54,pady=8,bg="#a1bccc",relief=RIDGE)
    TitFrame.pack(side=TOP)

    heading = Label(TitFrame,font=('arial',47,'bold'),text="Apply For Job",bg="#a1bccc")
    heading.grid()

    ButtonFrame = Frame(MainFrame,bd=7,width=1350,height=70,padx=18,pady=10,bg="#deeffa",relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    DataFrame = Frame(MainFrame,bd=7,width=1300,height=400,padx=20,pady=20,bg="#a1bccc",relief=RIDGE)
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame,bd=8,width=1000,height=600,padx=20,bg="#deeffa",relief=RIDGE,
                                font=('arial',20,'bold'),text="Job Details\n")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRIGHT = LabelFrame(DataFrame,bd=5,width=450,height=300,padx=31,pady=3,bg="#deeffa",relief=RIDGE,
                                font=('arial',20,'bold'),text="Job Post\n")
    DataFrameRIGHT.pack(side=RIGHT)
    ####################################### Labels and Entry Widget############################
    global post_text,technical_text,academic_qualifications_text,cocurricular_activities_text,package_text,criteria_text,emp_name_text,information_text
    lbl_post = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Job Title",bg="Ghost White",padx=2,pady=2)
    lbl_post.grid(row=0,column=0,stick=W)
    post_text = Entry(DataFrameLEFT,font=('arial',15,'bold'),textvariable=j_post,width=50)
    post_text.grid(row=0,column=1)

    post_text.bind("<Return>",focus_1)

    lbl_technical = Label(DataFrameLEFT,font=('arial',18,'bold'),text="Technical Skills",bg="Ghost White",padx=2,pady=2)
    lbl_technical.grid(row=1,column=0,stick=W)
    technical_text = Entry(DataFrameLEFT,font=('arial',15,'bold'),width=50,textvariable=j_technical,state=DISABLED)
    technical_text.grid(row=1,column=1)

    lbl_academic_qualifications = Label(DataFrameLEFT,font=('arial',17,'bold'),text="Academic Qualifications",bg="Ghost White",padx=2,pady=2)
    lbl_academic_qualifications.grid(row=2,column=0,stick=W)
    academic_qualifications_text = Entry(DataFrameLEFT,font=('arial',15,'bold'),width=50,textvariable=j_academic_qualifications,state=DISABLED)
    academic_qualifications_text.grid(row=2,column=1)

    lbl_cocurricular_activities = Label(DataFrameLEFT,font=('arial',17,'bold'),text="Cocurricular Activities",bg="Ghost White",padx=2,pady=2)
    lbl_cocurricular_activities.grid(row=3,column=0,stick=W)
    cocurricular_activities_text = Entry(DataFrameLEFT,font=('arial',15,'bold'),width=50,textvariable=j_cocurricular_activities,state=DISABLED)
    cocurricular_activities_text.grid(row=3,column=1)

    lbl_package = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Package",bg="Ghost White",padx=2,pady=2)
    lbl_package.grid(row=4,column=0,stick=W)
    package_text = Entry(DataFrameLEFT,font=('arial',15,'bold'),width=50,textvariable=j_package)
    package_text.grid(row=4,column=1)

    package_text.bind("<Return>",focus_2)

    lbl_criteria = Label(DataFrameLEFT,font=('arial',17,'bold'),text="Criteria For Hiring",bg="Ghost White",padx=2,pady=2)
    lbl_criteria.grid(row=5,column=0,stick=W)
    criteria_text = Entry(DataFrameLEFT,font=('arial',15,'bold'),width=50,textvariable=j_criteria,state=DISABLED)
    criteria_text.grid(row=5,column=1)

    lbl_emp_name = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Employer Name",bg="Ghost White",padx=2,pady=2)
    lbl_emp_name.grid(row=6,column=0,stick=W)
    emp_name_text = Entry(DataFrameLEFT,font=('arial',15,'bold'),width=50,textvariable=j_emp_name)
    emp_name_text.grid(row=6,column=1)

    lbl_information = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Information",bg="Ghost White",padx=2,pady=2)
    lbl_information.grid(row=7,column=0,stick=W)
    information_text = Entry(DataFrameLEFT,font=('arial',15,'bold'),width=50,textvariable=j_information,state=DISABLED)
    information_text.grid(row=7,column=1)
    ####################################### ListBox and ScrollBar Widget############################
    global jobpost_list
    scrollbar= Scrollbar(DataFrameRIGHT)
    scrollbar.grid(row=0,column=1,sticky='ns')

    jobpost_list=Listbox(DataFrameRIGHT,width=41,height=15,font=('arial',10,'bold italic'),yscrollcommand=scrollbar.set)
    jobpost_list.bind("<<ListboxSelect>>",job_details_rec)
    jobpost_list.grid(row=0,column=0,padx=8)
    scrollbar.config(command=jobpost_list.yview)

    ####################################### Button Widget############################
    global button_apply,button_search,button_display, button_clear,button_exit
    button_apply = Button(ButtonFrame,text="Apply",font=('arial',12,'bold'),height=1,width=18,bd=6,command=apply_for_job)
    button_apply.grid(row=0,column=0)
    button_search = Button(ButtonFrame,text="Search",font=('arial',12,'bold'),height=1,width=18,bd=6,command=search_job)
    button_search.grid(row=0,column=1)
    button_display = Button(ButtonFrame,text="Display",font=('arial',12,'bold'),height=1,width=18,bd=6,command=display_jobs)
    button_display.grid(row=0,column=2)
    button_clear = Button(ButtonFrame,text="Clear",font=('arial',12,'bold'),height=1,width=18,bd=6,command=clearData)
    button_clear.grid(row=0,column=3)
    button_exit = Button(ButtonFrame,text="Exit",font=('arial',12,'bold'),height=1,width=18,bd=6,command=isExit)
    button_exit.grid(row=0,column=4)



def jobseeker_window():
    if check_credentials('jobseeker_data',username_jobseeker_field.get(),password_jobseeker_field.get()):
        global root4
        root4 = Toplevel(root)
        root3.withdraw()
        root4.configure(background="#cad1db")
        root4.title("Welcome Jobseeker")
        root4.geometry("500x300")
        c.execute(f"Select JobSeeker.can_name from JobSeeker where JobSeeker.can_id=(Select can_id from jobseeker_data where username='{username_jobseeker_field.get()}')")
        Name = c.fetchone()[0]
        f1 = Frame(root4,background="#cad1db")
        f1.pack(side=TOP,fill="both")

        heading = Label(f1,text=f"Welcome!! {Name}",font=("Courier", 20,"bold"),bg='#cad1db')
        heading.pack()

        f2 = Frame(f1,bg="#cad1db")
        f2.pack(side=LEFT,fill='both',padx=160,pady=50)

        b = Button(f2, text = "Job Search",width=14,bg="#8fa8bd",activebackground="#464747",activeforeground="#edecdd",borderwidth=5,relief=SUNKEN,command=job_window)
        b.grid(row=0,column=1,ipadx=20,ipady=5)
        b1 = Button(f2, text = "Apply for job",width=14,bg="#8fa8bd",activebackground="#464747",activeforeground="#edecdd",borderwidth=5,relief=SUNKEN)
        b1.grid(row=1, column=1,ipadx=20,ipady=5)
        b2 = Button(f2, text = "Scheduled Interview",bg="#8fa8bd",width=14,activebackground="#464747",activeforeground="#edecdd",borderwidth=5,relief=SUNKEN)
        b2.grid(row=2, column=1,ipadx=20,ipady=5)
        b3 = Button(f2, text = "Offer Letter",width=14,bg="#8fa8bd",activebackground="#464747",activeforeground="#edecdd",borderwidth=5,relief=SUNKEN)
        b3.grid(row=3, column=1,ipadx=20,ipady=5)

        print("Correct")
    else:
        messagebox.showerror("Error","Invalid Credentials! Try Again..")

def employer_window():

    if check_credentials('employer_data',username_employer_field.get(),password_employer_field.get()):
        global root_employer_window
        global required_emp_id
        c.execute(f"SELECT emp_id from employer_data where username='{username_employer_field.get()}' ")
        required_emp_id = c.fetchone()[0]
        root_employer_window = Toplevel(root)
        root_employer.withdraw()
        root_employer_window.configure(background="#cad1db")
        root_employer_window.title("Welcome Employer")
        root_employer_window.geometry("500x300")
        c.execute(f"Select Employer.emp_name from Employer where Employer.emp_id=(Select emp_id from employer_data where username='{username_employer_field.get()}')")
        Name = c.fetchone()[0]
        f1 = Frame(root_employer_window,background="#cad1db")
        f1.pack(side=TOP,fill="both")

        heading = Label(f1,text=f"Welcome!! {Name}",font=("Courier", 20,"bold"),bg='#cad1db')
        heading.pack()

        f2 = Frame(f1,bg="#cad1db")
        f2.pack(side=LEFT,fill='both',padx=160,pady=50)

        b = Button(f2, text = "Post Job Profile",width=14,bg="#8fa8bd",activebackground="#464747",activeforeground="#edecdd",borderwidth=5,relief=SUNKEN,command=insert_job_profile_window)
        b.grid(row=0,column=1,ipadx=20,ipady=5)
        b1 = Button(f2, text = "Delete Job Profile",width=14,bg="#8fa8bd",activebackground="#464747",activeforeground="#edecdd",borderwidth=5,relief=SUNKEN)
        b1.grid(row=1, column=1,ipadx=20,ipady=5)
        b2 = Button(f2, text = "View Applications",bg="#8fa8bd",width=14,activebackground="#464747",activeforeground="#edecdd",borderwidth=5,relief=SUNKEN)
        b2.grid(row=2, column=1,ipadx=20,ipady=5)
        b3 = Button(f2, text = "Call For Interview",width=14,bg="#8fa8bd",activebackground="#464747",activeforeground="#edecdd",borderwidth=5,relief=SUNKEN)
        b3.grid(row=3, column=1,ipadx=20,ipady=5)

        print("Correct")
    else:
        messagebox.showerror("Error","Invalid Credentials! Try Again..")

def login_jobseeker():
    global root3
    root3 = Toplevel(root)
    root3.configure(background="#cad1db")
    root3.title("Log-In Jobseeker")
    root3.geometry("400x200")

    heading = Label(root3, text="Log-In", bg="#cad1db")
    username_emp = Label(root3, text="Username", bg="#cad1db")   
    password_emp = Label(root3, text="Password", bg="#cad1db") 
    
    heading.grid(row=0, column=1) 
    username_emp.grid(row=1, column=0) 
    password_emp.grid(row=2, column=0) 
    global username_jobseeker_field,password_jobseeker_field
    username_jobseeker_field = Entry(root3)
    password_jobseeker_field = Entry(root3,show='*') 
    
    username_jobseeker_field.bind("<Return>",focus21)  
    username_jobseeker_field.grid(row=1, column=1, ipadx="60") 
    password_jobseeker_field.grid(row=2, column=1, ipadx="60") 
    
    submit = Button(root3, text="Log In", fg="white", bg="#3e434a",pady='5',command=jobseeker_window) 
    submit.grid(row=3,column=1,ipadx='10')


def login_employer():
    global root_employer
    root_employer = Toplevel(root)
    root_employer.configure(background="#cad1db")
    root_employer.title("Log-In Jobseeker")
    root_employer.geometry("400x200")

    heading = Label(root_employer, text="Log-In", bg="#cad1db")
    username_emp = Label(root_employer, text="Username", bg="#cad1db")   
    password_emp = Label(root_employer, text="Password", bg="#cad1db") 
    
    heading.grid(row=0, column=1) 
    username_emp.grid(row=1, column=0) 
    password_emp.grid(row=2, column=0) 
    global username_employer_field,password_employer_field
    username_employer_field = Entry(root_employer)
    password_employer_field = Entry(root_employer,show='*') 
    
    username_employer_field.bind("<Return>",focus31)  
    username_employer_field.grid(row=1, column=1, ipadx="60") 
    password_employer_field.grid(row=2, column=1, ipadx="60") 
    
    submit = Button(root_employer, text="Log In", fg="white", bg="#3e434a",pady='5',command=employer_window) 
    submit.grid(row=3,column=1,ipadx='10')


def insert_jobseeker():  
    # print(type(can_name_field.get()))
    answer = messagebox.askquestion('Confirmation',"Are you sure you want to submit?")
    if answer=='yes':
        for row in c.execute("SELECT MAX(can_id) from JobSeeker"):
            temp = row[0]
        can_id=temp+1

        jobseeker_data_table = pd.read_sql_query("SELECT * FROM jobseeker_data", conn)
        JobSeeker_table = pd.read_sql_query("SELECT * FROM JobSeeker", conn)
        personal_info_table = pd.read_sql_query("SELECT * FROM personal_info", conn)

        ######
        X = JobSeeker_table['can_id'].isin([can_id]).any()
        Y = jobseeker_data_table['username'].isin([username_field.get()]).any()
        Z = personal_info_table['contact'].isin([contact_field.get()]).any()
        ######

        if not X and not Y and not Z:
            insert_jobseeker_id_password('jobseeker_data',can_id,username_field.get(),password_field.get())
            insert_jobseeker_data('JobSeeker',can_id,can_name_field.get(),CV_field.get(),projects_field.get())
            insert_personal_info_of_jobseeker('personal_info',can_id,father_name_field.get(),DOB_field.get(),contact_field.get())
        else:
            messagebox.showerror("Error","Data is Not Inserted Bcoz of Integrity error that means you might have violated the database rules. Please Enter Your Actual Details..")
        messagebox.showinfo("Window","Your Data has submitted..")
        username_field.focus_set() 
        clear() 
    else:
        messagebox.showinfo("Window","Your chose, Not to submit data..")

def insert_employer():
    answer = messagebox.askquestion('Confirmation',"Are you sure you want to submit?")
    if answer=='yes':
        
        employer_data_table = pd.read_sql_query("SELECT * FROM employer_data", conn)
        X = employer_data_table['emp_id'].isin([emp_id_field.get()]).any()
        Y = employer_data_table['username'].isin([username_emp_field.get()]).any()
        if not X and not Y:
            insert_employer_id_password(emp_id_field.get(),username_emp_field.get(),password_emp_field.get())
            insert_employer_data(emp_id_field.get(),emp_name_field.get(),information_field.get(),email_field.get())
        else:
            messagebox.showerror("Error","Data is Not Inserted Bcoz of Integrity error that means you might have violated the database rules. Please Enter Your Actual Details..")
        messagebox.showinfo("Window","Your Data has submitted..")
        username_emp_field.focus_set() 
        clear2()

    else:
        messagebox.showinfo("Window","Your chose, Not to submit data..")

def register_employer():

    print("Hello! World")
    root2 = Toplevel(root)
    root2.configure(background="#cad1db")
    root2.title("Registeration Form of Employer")
    root2.geometry("500x300")
    
    heading = Label(root2, text="Form", bg="#cad1db")
    username_emp = Label(root2, text="Username", bg="#cad1db")   
    password_emp = Label(root2, text="Password", bg="#cad1db") 
    emp_name = Label(root2, text="Name", bg="#cad1db")
    emp_id = Label(root2, text="Employee Id", bg="#cad1db")
    email = Label(root2,text="E-mail",bg="#cad1db")
    information = Label(root2,text="Information",bg="#cad1db")

    heading.grid(row=0, column=1) 
    username_emp.grid(row=1, column=0) 
    password_emp.grid(row=2, column=0) 
    emp_name.grid(row=3, column=0)
    emp_id.grid(row=4, column=0)
    email.grid(row=5, column=0) 
    information.grid(row=6, column=0)

    global username_emp_field, password_emp_field, emp_name_field, email_field, information_field,emp_id_field

    username_emp_field = Entry(root2)
    password_emp_field = Entry(root2,show='*') 
    # password_emp_field = Entry(root2) 
    emp_name_field = Entry(root2)
    emp_id_field = Entry(root2)
    email_field = Entry(root2) 
    information_field = Entry(root2) 

    username_emp_field.bind("<Return>",focus11)  
    password_emp_field.bind("<Return>",focus12)    
    emp_name_field.bind("<Return>",focus13)
    emp_id_field.bind("<Return>",focus14) 
    email_field.bind("<Return>",focus15)

    username_emp_field.grid(row=1, column=1, ipadx="100") 
    password_emp_field.grid(row=2, column=1, ipadx="100") 
    emp_name_field.grid(row=3, column=1, ipadx="100")
    emp_id_field.grid(row=4, column=1, ipadx="100")
    email_field.grid(row=5,column=1,ipadx="100")
    information_field.grid(row=6, column=1, ipadx="100",ipady="15") 
    
    submit2 = Button(root2, text="Submit", fg="white", bg="#3e434a",pady='5',command=insert_employer) 
    submit2.grid(row=7, column=1,ipadx='10')
    
def register_jobseeker():
    print("Hello")
    
    root1 = Toplevel(root)
    # set the background colour of GUI window 
    root1.configure(background='#c3d2de') 
    root1.title("registration form of job seeker")

    root1.geometry("500x300") 
    # global username,password,can_name,CV,projects,father_name,DOB,contact
    heading = Label(root1, text="Form", bg="#c3d2de") 
    username = Label(root1, text="Username", bg="#c3d2de")   
    password = Label(root1, text="Password", bg="#c3d2de") 
    can_name = Label(root1, text="Name", bg="#c3d2de") 
    CV = Label(root1, text="CV(path)", bg="#c3d2de") 
    projects = Label(root1, text="Projects", bg="#c3d2de") 
    father_name = Label(root1, text="Father Name", bg="#c3d2de") 
    DOB = Label(root1, text="DOB", bg="#c3d2de")    
    contact = Label(root1, text="Contact No.", bg="#c3d2de") 

    heading.grid(row=0, column=1) 
    username.grid(row=1, column=0) 
    password.grid(row=2, column=0) 
    can_name.grid(row=3, column=0) 
    CV.grid(row=4, column=0) 
    projects.grid(row=5, column=0) 
    father_name.grid(row=6, column=0) 
    DOB.grid(row=7, column=0) 
    contact.grid(row=8, column=0) 
  
    global username_field,password_field,can_name_field,CV_field,projects_field,father_name_field,DOB_field,contact_field
    # create a text entry box 
    # for typing the information 
    scrollbar = Scrollbar(root1,orient=HORIZONTAL)
    
    username_field = Entry(root1,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    password_field = Entry(root1,show='*',borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    can_name_field = Entry(root1,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    CV_field = Entry(root1,borderwidth=2,relief=SUNKEN,bg="#e1e5e8")
    projects_field = Entry(root1,xscrollcommand=scrollbar.set,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    father_name_field = Entry(root1,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    DOB_field = Entry(root1,borderwidth=2,relief=SUNKEN,bg="#e1e5e8") 
    contact_field = Entry(root1,borderwidth=2,relief=SUNKEN,bg="#e1e5e8")

    username_field.bind("<Return>", focus1) 
    password_field.bind("<Return>", focus2) 
    can_name_field.bind("<Return>", focus3) 
    CV_field.bind("<Return>", focus4) 
    projects_field.bind("<Return>", focus5) 
    father_name_field.bind("<Return>", focus6)
    DOB_field.bind("<Return>", focus7)

    username_field.grid(row=1, column=1, ipadx="100") 
    password_field.grid(row=2, column=1, ipadx="100") 
    can_name_field.grid(row=3, column=1, ipadx="100") 
    CV_field.grid(row=4, column=1, ipadx="100") 
    projects_field.grid(row=5, column=1, ipadx="100",ipady="15")
    scrollbar.grid(row=5,column=1)
    scrollbar.config(command=projects_field.xview)

    father_name_field.grid(row=6, column=1, ipadx="100") 
    DOB_field.grid(row=7, column=1, ipadx="100") 
    contact_field.grid(row=8, column=1, ipadx="100") 
    
    # create a Submit Button and place into the root window 
    submit = Button(root1, text="Submit", fg="white", 
                            bg="#1f2c36", command=insert_jobseeker,borderwidth=4,relief=SUNKEN) 
    submit.grid(row=9, column=1) 

root = Tk()
root.configure(background='light grey')
root.title("Online Recruitment System")
root.geometry("500x300")

heading = Label(root,text="Welcome to Online Recruitment System!",font=("Courier", 14,"bold"),bg='light grey')
welcome = Label(root,text="Hello User, we welcome you here",font=('Courier',10),bg='light grey')
heading.grid(row=0,column=1)
welcome.grid(row=1,column=1)

LogIn = Menubutton(root, text="Log-In", fg="Black", bg="white",activebackground='black',activeforeground='white') 
Register = Menubutton(root, text="Register", fg="Black", bg="white",activebackground='black',activeforeground='white') 

LogIn.grid(row=3,column=1,padx=110,pady=50)
Register.grid(row=4,column=1)

LogIn.menu = Menu(LogIn,tearoff=0)
LogIn["menu"] = LogIn.menu
LogIn.menu.add_radiobutton(label="Log in as Job seeker",activebackground="#656a70",activeforeground="#ebeced",command=login_jobseeker)
LogIn.menu.add_radiobutton(label="Log in as Employer",activebackground="#656a70",activeforeground="#ebeced",command=login_employer)

Register.menu = Menu(Register,tearoff=0)
Register["menu"] = Register.menu
Register.menu.add_radiobutton(label="Register as Job seeker",command=register_jobseeker,activebackground="#656a70",activeforeground="#ebeced")
Register.menu.add_radiobutton(label="Register as Employer",command=register_employer,activebackground="#656a70",activeforeground="#ebeced")

root.mainloop()