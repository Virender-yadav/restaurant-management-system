import pymysql
from tkinter import *
from tkinter import messagebox 

conn=pymysql.connect(host="localhost",user="root",password="",db="hotelm")
mycursor=conn.cursor()

def staff_det():
    mycursor.execute("SELECT * FROM staff_details  ;")#short the rows and columns
    #to fetch a single row=> fetchone() 
    #2. to fetch all rows from database=>fetchall()
    #3.To fetch any no. of rows from database=>fetchmany(size)
    # PRINT ON CONSOLE.
    res=mycursor.fetchall()
    vary=80
    sd=Toplevel()
    sd.geometry("1350x700+0+0")
    sd.config(bg="yellow")
    Label(sd,text="STAFF DETAILS",font="times  20 underline bold ", fg="red",bg="yellow").place(x=342,y=10)
    
    Label(sd,text="EMP. id",font="times  10 underline bold  ", fg="red",bg="yellow").place(x=2,y=50)
    Label(sd,text="EMP. NAME",font="times  10 underline bold  ", fg="red",bg="yellow").place(x=175,y=50)
    Label(sd,text="EMP. PASSWORD ",font="times 10 underline bold  ", fg="red",bg="yellow").place(x=348,y=50)
    Label(sd,text="SHIFT",font="times 10 underline bold ", fg="red",bg="yellow").place(x=521,y=50)
    Label(sd,text="CONTACT_NO",font="times 10 underline bold ", fg="red",bg="yellow").place(x=640,y=50)
    Label(sd,text="EMP_ADDRESS",font="times 10 underline bold ", fg="red",bg="yellow").place(x=790,y=50)


    for i in range(0,mycursor.rowcount):
        Label(sd,text=res[i][0],font="times 10", fg="red",bg="yellow").place(x=50,y=vary)
        Label(sd,text=res[i][1],font="times 10", fg="red",bg="yellow").place(x=175,y=vary)
        Label(sd,text=res[i][2],font="times 10", fg="red",bg="yellow").place(x=348,y=vary)
        Label(sd,text=res[i][3],font="times 10", fg="red",bg="yellow").place(x=521,y=vary)
        Label(sd,text=res[i][4],font="times 10", fg="red",bg="yellow").place(x=640,y=vary)
        Label(sd,text=res[i][5],font="times 10", fg="red",bg="yellow").place(x=790,y=vary)


        vary+=30   
    


def it_details():
    td=Toplevel()
    td.geometry("1350x700+0+0")
    td.config(bg="yellow")
    Label(td,text="ITEMS DETAILS",font="times  20 underline bold ", fg="red",bg="yellow").grid(row=0,column=1,columnspan=2,ipadx=20,ipady=20)
    Label(td,text="RATE ON THE BASIS OF PRISE",font="times  20 underline bold  ", fg="red",bg="yellow").grid(row=1,column=0,columnspan=2,ipadx=20,ipady=20,padx=100,pady=5)

    Label(td,text="FRENCH FRIES",font="times 11 underline bold ", fg="red",bg="yellow").grid(row=2,column=0,ipadx=10,ipady=5,padx=10,pady=5)
    Label(td,text="40/f.plate",font="times 11", fg="red",bg="yellow").grid(row=2,column=1,ipadx=10,ipady=10,padx=10,pady=5)

    Label(td,text="BURGER",font="times 11", fg="red",bg="yellow").grid(row=3,column=0)
    Label(td,text="35/piece",font="times 11", fg="red",bg="yellow").grid(row=3,column=1,ipadx=20,ipady=20,padx=10,pady=5)

    Label(td, text="SANDWICH",font="times 11", fg="red",bg="yellow").grid(row=4,column=0)
    Label(td,text="40/piece",font="times 11", fg="red",bg="yellow").grid(row=4,column=1,ipadx=20,ipady=20,padx=10)

    Label(td, text="PASTA",font="times 11", fg="red",bg="yellow").grid(row=5,column=0)
    Label(td,text="80/f.plate",font="times 11", fg="red",bg="yellow").grid(row=5,column=1,ipadx=20,ipady=20,padx=10,pady=5)

    Label(td, text="THALI",font="times 11", fg="red",bg="yellow").grid(row=6,column=0)
    Label(td,text="190/f.thali",font="times 11", fg="red",bg="yellow").grid(row=6,column=1,ipadx=20,ipady=20,padx=10)

    Label(td, text="COFFE",font="times 11", fg="red",bg="yellow").grid(row=7,column=0)
    Label(td,text="30/cup",font="times 11", fg="red",bg="yellow").grid(row=7,column=1,ipadx=20,ipady=20,padx=10,pady=5)
    Button(td,text="BACK",font="times 11",bg="green",bd="4",height="1",width="11",command=td.destroy).grid(row=8,column=1,columnspan=2,ipadx=20,ipady=10)
    Label(td, text="* 1 RUPEES = 1 POINT",font="times 11", fg="red",bg="yellow").grid(row=9)

    Label(td,text="RATE ON THE BASIS OF POINTS",font="times  20 underline bold  ", fg="red",bg="yellow").grid(row=1,column=2,columnspan=2,ipadx=20,ipady=20,padx=100,pady=5)
    Label(td,text="FRENCH FRIES",font="times 11", fg="red",bg="yellow").grid(row=2,column=2,ipadx=10,ipady=5,padx=10,pady=5)
    Label(td,text="40/f.plate",font="times 11", fg="red",bg="yellow").grid(row=2,column=3,ipadx=10,ipady=10,padx=10,pady=5)
    Label(td,text="BURGER",font="times 11", fg="red",bg="yellow").grid(row=3,column=2)
    Label(td,text="35/piece",font="times 11", fg="red",bg="yellow").grid(row=3,column=3,ipadx=20,ipady=20,padx=10,pady=5)
    Label(td, text="SANDWICH",font="times 11", fg="red",bg="yellow").grid(row=4,column=2)
    Label(td,text="40/piece",font="times 11", fg="red",bg="yellow").grid(row=4,column=3,ipadx=20,ipady=20,padx=10)
    Label(td, text="PASTA",font="times 11", fg="red",bg="yellow").grid(row=5,column=2)
    Label(td,text="80/f.plate",font="times 11", fg="red",bg="yellow").grid(row=5,column=3,ipadx=20,ipady=20,padx=10,pady=5)
    Label(td, text="THALI",font="times 11", fg="red",bg="yellow").grid(row=6,column=2)
    Label(td,text="190/f.thali",font="times 11", fg="red",bg="yellow").grid(row=6,column=3,ipadx=20,ipady=20,padx=10)
    Label(td, text="COFFE",font="times 11", fg="red",bg="yellow").grid(row=7,column=2)
    Label(td,text="30/cup",font="times 11", fg="red",bg="yellow").grid(row=7,column=3,ipadx=20,ipady=20,padx=10,pady=5)

#module of customer point game
    
def cmp():#here cmp means customer points game

    
        
    def insp():
        a=orderno.get()
        b=cs_name.get()
        c=ph_no.get()
        d=mail.get()
        e=cpo.get()
        f=tpo.get()
        g=tco.get()
        def calp():
            x=int(tco.get())
            y=a*0.05
            cpo.set(y)

        
        try:
            mycursor.execute("INSERT INTO customer_points(order_no,customer_name,phone_no,email,customer_points,total_points)VALUES('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"');")
            conn.commit()
            messagebox.showinfo("message","inserted successfully")
            
        except:
            conn.rollback()
            conn.close()
                   
    

    cd=Toplevel()
    cd.geometry("500x700+250+15")
    cd.config(bg="yellow")
    Label(cd,text="Customer Information",font="times 30 bold underline", fg="blue",bg="yellow").grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10,columnspan=2)

    Label(cd,text="ORDER NO.",font="times 14 ", fg="red",bg="yellow").grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    orderno=StringVar()
    Entry(cd,textvariable=orderno).grid(row=1,column=1,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(cd,text="CUSTOMER NAME",font="times 14 ", fg="red",bg="yellow").grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    cs_name=StringVar()
    Entry(cd,textvariable=cs_name).grid(row=2,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Label(cd,text="PHONE NO.",font="times  14  ", fg="red",bg="yellow").grid(row=3,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    ph_no=StringVar()
    Entry(cd,textvariable=ph_no).grid(row=3,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Label(cd,text="EMAIL",font="times 14 ", fg="red",bg="yellow").grid(row=4,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    mail=StringVar()
    Entry(cd,textvariable=mail).grid(row=4,column=1,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(cd,text="TOTAL COST",font="times 14 ", fg="red",bg="yellow").grid(row=5,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    tco=StringVar()
    Entry(cd,textvariable=tco).grid(row=5,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Label(cd,text="CUSTOMER POINTS",font="times 14 ", fg="red",bg="yellow").grid(row=6,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    cpo=StringVar()
    Entry(cd,textvariable=cpo).grid(row=6,column=1,ipadx=10,ipady=5,padx=10,pady=6)

    Label(cd,text="TOTAL POINTS",font="times 14 ", fg="red",bg="yellow").grid(row=7,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    tpo=StringVar()
    Entry(cd,textvariable=tpo).grid(row=7,column=1,ipadx=10,ipady=5,padx=10,pady=5)
    
    Button(cd,text="SET",font="times 11",bg="green",bd="4",height="1",width="11",command=insp).grid(row=8,column=1,ipadx=20,ipady=10,padx=20,pady=20)
    Button(cd,text="back",font="times 11",bg="green",bd="4",height="1",width="11",command=cd.destroy).grid(row=8,column=0,ipadx=20,ipady=10,padx=20,pady=20)


           

def billing_s():
    mp=Toplevel()
    mp.geometry("1200x1200+5+5")

    def ins():
        order=ordno.get()
        a=qty1.get()
        b=qty2.get()
        c=qty3.get()
        d=qty4.get()
        e=qty5.get()
        f=qty6.get()

        g=fr_fries.get()
        h=burger.get()
        i=sandwich.get()
        j=pasta.get()
        k=thali.get()
        l=coffe.get()

        m=totalqty.get()
        n=net_total.get()
        p=gst.get()
        q=total_amt.get()
        
        
        
       
        
        #try:
        mycursor.execute("INSERT INTO billing_sy(order_no,qty_ff,amount_ff,qnty_burg,burg_amount,qnty_san,san_amount,qty_pasta,pasta_amount,qnty_thali,thali_amount,qnty_coffe,coffe_amount,total_qty,net_amount,gst,total_amount)VALUES('"+order+"','"+a+"','"+g+"','"+b+"','"+h+"','"+c+"','"+i+"','"+d+"','"+j+"','"+e+"','"+k+"','"+f+"','"+l+"','"+m+"','"+n+"','"+p+"','"+q+"');")
        conn.commit()
        messagebox.showinfo("message","inserted successfully")
        
        #except:
        #conn.rollback()
        #print("will not execute")
        #conn.close()
        
    def add():
        a=int(qty1.get())
        b=int(qty2.get())
        c=int(qty3.get())
        d=int(qty4.get())
        e=int(qty5.get())
        f=int(qty6.get())
        s=a+b+c+d+e+f
        totalqty.set(s)
        
        tf=40*a
        tb=35*b
        ts=40*c
        tp=80*d
        tt=190*e
        tc=30*f
        
        fr_fries.set(tf)
        burger.set(tb)
        sandwich.set(ts)
        pasta.set(tp)
        thali.set(tt)
        coffe.set(tc)

        g=int(fr_fries.get())
        h=int(burger.get())
        i=int(sandwich.get())
        j=int(pasta.get())
        k=int(thali.get())
        l=int(coffe.get())
        namt=g+h+i+j+k+l
        net_total.set(namt)

        m=int(net_total.get())
        gnt=m*(2.5/100)
        gst.set(gnt)
        toa=gnt+namt
        total_amt.set(toa)
        
       
    mp.title("BILLING PAGE")
    mp.config(bg="yellow")
    Label(mp,text="ORDER NO.",font="times 14 bold underline", fg="red",bg="yellow").grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    ordno=StringVar()
    Entry(mp,textvariable=ordno).grid(row=0,column=1,ipadx=10,ipady=5,padx=10,pady=5)
    Label(mp,text="ITEMS",font="times 14 bold underline", fg="red",bg="yellow").grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=10)
    Label(mp,text="RATE",font="times  14  bold underline", fg="red",bg="yellow").grid(row=1,column=1,ipadx=20,ipady=20,padx=10,pady=10)
    Label(mp,text="QUANTITY",font="times 14  bold underline", fg="red",bg="yellow").grid(row=1,column=2,ipadx=20,ipady=20,padx=10,pady=10)
    Label(mp,text="AMOUNT",font="times 14  bold underline", fg="red",bg="yellow").grid(row=1,column=3,ipadx=20,ipady=20,padx=10,pady=10)
    
    Label(mp,text="FRENCH FRIES",font="times 11", fg="red",bg="yellow").grid(row=2,column=0,ipadx=10,ipady=5,padx=10,pady=5)
    Label(mp,text="40/f.plate",font="times 11", fg="red",bg="yellow").grid(row=2,column=1,ipadx=10,ipady=10,padx=10,pady=5)
    qty1=StringVar()
    Entry(mp,textvariable=qty1).grid(row=2,column=2,ipadx=10,ipady=5,padx=10,pady=5)
    fr_fries=StringVar()
    Entry(mp,textvariable=fr_fries).grid(row=2,column=3,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(mp,text="BURGER",font="times 11", fg="red",bg="yellow").grid(row=3,column=0)
    Label(mp,text="35/piece",font="times 11", fg="red",bg="yellow").grid(row=3,column=1,ipadx=20,ipady=20,padx=10,pady=5)
    qty2=StringVar()
    Entry(mp,textvariable=qty2).grid(row=3,column=2,ipadx=10,ipady=5,padx=10,pady=5)
    burger=StringVar()
    Entry(mp,textvariable=burger).grid(row=3,column=3,ipadx=10,ipady=5,padx=10,pady=5)
    Button(mp,text="CALCULATE",bd="4",height="1",width="15",command=add).grid(row=3,column=4)

    
    Label(mp, text="SANDWICH",font="times 11", fg="red",bg="yellow").grid(row=4,column=0)
    Label(mp,text="40/piece",font="times 11", fg="red",bg="yellow").grid(row=4,column=1,ipadx=20,ipady=20,padx=10)
    qty3=StringVar()
    Entry(mp,textvariable=qty3).grid(row=4,column=2,ipadx=10,ipady=5,padx=10)
    sandwich=StringVar()
    Entry(mp,textvariable=sandwich).grid(row=4,column=3,ipadx=10,ipady=5,padx=10)
    Button(mp,text='SUBMIT',bd="4",height="1",width="15",command=ins).grid(row=4,column=4,padx=10,pady=5)
    
    Label(mp, text="PASTA",font="times 11", fg="red",bg="yellow").grid(row=5,column=0)
    Label(mp,text="80/f.plate",font="times 11", fg="red",bg="yellow").grid(row=5,column=1,ipadx=20,ipady=20,padx=10,pady=5)
    qty4=StringVar()
    Entry(mp,textvariable=qty4).grid(row=5,column=2,ipadx=10,ipady=5,padx=10,pady=5)
    pasta=StringVar()
    Entry(mp,textvariable=pasta).grid(row=5,column=3,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(mp, text="THALI",font="times 11", fg="red",bg="yellow").grid(row=6,column=0)
    Label(mp,text="190/f.thali",font="times 11", fg="red",bg="yellow").grid(row=6,column=1,ipadx=20,ipady=20,padx=10)
    qty5=StringVar()
    Entry(mp,textvariable=qty5).grid(row=6,column=2,ipadx=10,ipady=5,padx=10)
    thali=StringVar()
    Entry(mp,textvariable=thali).grid(row=6,column=3,ipadx=10,ipady=5,padx=10)
    
    Label(mp, text="COFFE",font="times 11", fg="red",bg="yellow").grid(row=7,column=0)
    Label(mp,text="30/cup",font="times 11", fg="red",bg="yellow").grid(row=7,column=1,ipadx=20,ipady=20,padx=10,pady=5)
    qty6=StringVar()
    Entry(mp,textvariable=qty6).grid(row=7,column=2,ipadx=10,ipady=5,padx=10,pady=5)
    coffe=StringVar()
    Entry(mp,textvariable=coffe).grid(row=7,column=3,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(mp,text="===================================================================================================", fg="red",bg="yellow").grid(row=8,column=0,columnspan=4)

    Label(mp, text="TOTAL",font="times 11", fg="red",bg="yellow").grid(row=9,column=1)
    totalqty=StringVar()
    Entry(mp,textvariable=totalqty).grid(row=9,column=2,ipadx=10,ipady=5,padx=10,pady=5) 
    net_total=StringVar()
    Entry(mp,textvariable=net_total).grid(row=9,column=3,ipadx=10,ipady=5,padx=10,pady=5)

    Label(mp,text="GST",font="times 11", fg="red",bg="yellow").grid(row=10,column=2)
    gst=StringVar()
    Entry(mp,textvariable=gst).grid(row=10,column=3,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(mp,text="TOTAL AMOUNT",font="times 11", fg="red",bg="yellow").grid(row=11,column=2)
    total_amt=StringVar()
    Entry(mp,textvariable=total_amt).grid(row=11,column=3,ipadx=10,ipady=5,padx=10,pady=5)

    
    
def main_page():
    ma=Toplevel()
    ma.title("MAIN PAGE")
    ma.geometry("600x500+450+80")
    ma.config(bg="yellow")
    Label(ma,text="",bg="yellow").grid(row=0,column=0,padx=40,pady=30)
    Button(ma,text="CUSTOMER MEAL POINTS",font="times 11",bd="4",height="1",width="15",command=cmp).grid(row=1,column=0,ipadx=40,ipady=20,pady=20,padx=40)
    Button(ma,text="BILLING SYSTEM",font="times 11",bd="4",height="1",width="15",command=billing_s).grid(row=1,column=1,ipadx=40,ipady=20,padx=40,pady=20)
    Label(ma,text="",bg="yellow").grid(row=2,column=0,padx=20,pady=10)
    Button(ma,text="PRODUCTS DETAIL",font="times 11",bd="4",height="1",width="15",command=it_details).grid(row=3,column=0,ipadx=40,ipady=20,padx=40,pady=20)
    Button(ma,text="STAFF DETAIL",font="times 11",bd="4",height="1",width="15",command=staff_det).grid(row=3,column=1,ipadx=40,ipady=20,padx=40,pady=20)
    Label(ma,text="",bg="yellow").grid(row=4,column=0,padx=40)
    Button(ma,text="LOGOUT",font="times 11",bd="4",height="1",width="15",command=ma.destroy).grid(row=5,column=0,ipadx=40,ipady=20,padx=20,pady=20,columnspan=2)
    
root=Tk()

def login():
    aco=userid.get()
    pn=password.get()
    
    if(mycursor.execute("SELECT * FROM reset_pass WHERE user_name='"+aco+"' AND password='"+pn+"' ;")== True):
        main_page()
        conn.commit()
    else:
        conn.rollback()
        messagebox.showinfo("message","Please check user id and password")

def forgot_pass():

    def set_pass():
       u=usn.get()
       p=ph.get()
       n=np.get()
       r=rnp.get()
       if(n==r):
           mycursor.execute("UPDATE reset_pass SET password='"+r+"' WHERE  user_name='"+u+"' AND phone_no='"+p+"';")
           conn.commit()
           messagebox.showinfo("message","PASSWORD HAS CHANGED")
       else:
           conn.rollback()
           messagebox.showinfo("message","your password not match")
         
       
        
        
    cd=Toplevel()
    cd.geometry("500x700+250+15")
    cd.config(bg="yellow")
    Label(cd,text="RESET PASSWORD",font="times 30 bold underline", fg="blue",bg="yellow").grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10,columnspan=2)

    Label(cd,text="USER NAME",font="times 14 ", fg="red",bg="yellow").grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    usn=StringVar()
    Entry(cd,textvariable=usn).grid(row=1,column=1,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(cd,text="PHONE NO.",font="times 14 ", fg="red",bg="yellow").grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    ph=StringVar()
    Entry(cd,textvariable=ph).grid(row=2,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Label(cd,text="NEW PASSWORD ",font="times  14  ", fg="red",bg="yellow").grid(row=3,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    np=StringVar()
    Entry(cd,textvariable=np).grid(row=3,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Label(cd,text="REENTER PASSWORD ",font="times  14  ", fg="red",bg="yellow").grid(row=4,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    rnp=StringVar()
    Entry(cd,textvariable=rnp).grid(row=4,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Button(cd,text="SET",font="times 11",bg="green",bd="4",height="1",width="11",command=set_pass).grid(row=5,column=1,ipadx=20,ipady=10,padx=20,pady=20)
    Button(cd,text="back",font="times 11",bg="green",bd="4",height="1",width="11",command=cd.destroy).grid(row=5,column=0,ipadx=20,ipady=10,padx=20,pady=20)


def sign_up():

    def set_sdet():
        a=emp_id.get();
        b=emp_name.get();
        c=emp_pass.get();
        d=shift.get();
        e=contact_no.get();
        f=emp_addr.get();
        
        mycursor.execute("INSERT INTO staff_details(emp_id,emp_name,emp_password,shift,contact_no,emp_address)VALUES('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"');")
        conn.commit()
        mycursor.execute("INSERT INTO reset_pass(user_name,phone_no,password)VALUES('"+b+"','"+e+"','"+c+"');")
        conn.commit()

        messagebox.showinfo("message","sign up successfully")
         

    cd=Toplevel()
    cd.geometry("500x700+250+15")
    cd.config(bg="yellow")
    Label(cd,text="SIGN UP",font="times 30 bold underline", fg="blue",bg="yellow").grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10,columnspan=2)

    Label(cd,text="EMP_ID",font="times 14 ", fg="red",bg="yellow").grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    emp_id=StringVar()
    Entry(cd,textvariable=emp_id).grid(row=1,column=1,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(cd,text="EMP_NAME",font="times 14 ", fg="red",bg="yellow").grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    emp_name=StringVar()
    Entry(cd,textvariable=emp_name).grid(row=2,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Label(cd,text="EMP_PASSWORD",font="times  14  ", fg="red",bg="yellow").grid(row=3,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    emp_pass=StringVar()
    Entry(cd,textvariable=emp_pass).grid(row=3,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Label(cd,text="SHIFT",font="times 14 ", fg="red",bg="yellow").grid(row=4,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    shift=StringVar()
    Entry(cd,textvariable=shift).grid(row=4,column=1,ipadx=10,ipady=5,padx=10,pady=5)
    
    Label(cd,text="contact_no",font="times 14 ", fg="red",bg="yellow").grid(row=5,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    contact_no=StringVar()
    Entry(cd,textvariable=contact_no).grid(row=5,column=1,ipadx=10,ipady=5,padx=10,pady=5)

    Label(cd,text="emp_address",font="times 14 ", fg="red",bg="yellow").grid(row=6,column=0,ipadx=20,ipady=20,padx=10,pady=5)
    emp_addr=StringVar()
    Entry(cd,textvariable=emp_addr).grid(row=6,column=1,ipadx=10,ipady=5,padx=10,pady=5)
    
    Button(cd,text="SET",font="times 11",bg="green",bd="4",height="1",width="11",command=set_sdet).grid(row=7,column=1,ipadx=20,ipady=10,padx=20,pady=20)
    Button(cd,text="back",font="times 11",bg="green",bd="4",height="1",width="11",command=cd.destroy).grid(row=7,column=0,ipadx=20,ipady=10,padx=20,pady=20)
    

        

root.geometry("400x500+450+80")
root.config(bg="yellow")
Label(root,text="RESTAURANT",font="calibri 35 bold underline",fg="blue").grid(row=0,column=0,columnspan=2,ipadx=45)

Label(root,text="USER NAME").grid(row=1,column=0,padx=20,pady=30,ipadx=20,ipady=10)
userid=StringVar()
Entry(root,textvariable=userid).grid(row=1,column=1,padx=30,pady=30,ipadx=20,ipady=10)
Label(root,text="PASSWORD").grid(row=2,column=0,padx=20,pady=20,ipadx=20,ipady=10)
password=StringVar()
Entry(root,textvariable=password,show="*").grid(row=2,column=1,padx=20,pady=20,ipadx=20,ipady=10)

Button(root,text="LOGIN",font="times 11",bg="green",bd="4",height="1",width="11",command=login).grid(row=3,column=0,ipadx=20,ipady=10,padx=20,pady=20)
Button(root,text="SIGN UP",font="times 11",bd="4",height="1",width="11",command=sign_up).grid(row=3,column=1,ipadx=20,ipady=10,padx=20,pady=20)
Button(root,text="FORGOT PASSWORD",font="calibri 9 bold",bd="4",height="1",width="11",command=forgot_pass).grid(row=4,column=0,ipadx=20,ipady=10,padx=20,pady=20)

