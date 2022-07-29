import tkinter as tk
import tkinter.ttk as ttk
import datetime


x = {'Amsterdam': -6,'Bangkok': -1, 'Berlin': -6, 'Dubai': -4, 'Korea': 1,\
     'Kuala Lumpur': 0, 'London': -7, 'Mexico': -13, 'New York': -12, 'Paris': -6,\
         'Rome': -6,'Sydney': 2,'Singapore': 0, 'Toronto': -12, 'Taipei': 0, 'Tokyo': 1}

def t():
    if lb_bnt2['text'] in x:
        lb_bnt['text'] = lb_bnt2['text']
        time_now = datetime.datetime.now()   
        time_delta = datetime.timedelta(hours=int(x[lb_bnt2['text']])) 
        new_dt = time_now + time_delta 
        tz = new_dt.strftime("%Y/%m/%d" +"\n"+ "%H:%M:%S")
        var_1.set(tz)
    lb_bnt.after(1000,t)


def hide():
    lb_bnt2['text'] = cbx.get()
    print(lb_bnt2['text'])

    
root = tk.Tk()
root.title('SELECT TIME')
root.geometry('380x300+700+300')
root.resizable(False,False)
root.attributes('-topmost',1)
root.config(bg='#678F8D')

lb_top = tk.Label(root, text='Please choose a country', fg='white', bg='#678F8D', font=('Muyao-Softbrush',24))
lb_top.grid(row=0, column=0, padx=12, pady=(12,10))


cbx_value = ('Amsterdam', 'Bangkok', 'Berlin', 'Dubai', 'Korea',\
             'Kuala Lumpur', 'London', 'Mexico', 'New York', 'Paris',\
                 'Rome', 'Sydney', 'Singapore', 'Toronto', 'Taipei', 'Tokyo')
cbx = ttk.Combobox(root, value=cbx_value, width=18, height=5)
cbx.configure(state='readonly')
cbx.set('-----------')
cbx.grid(row=10, column=0, padx=10, pady=10)


bnt = tk.Button(root, text='SELECT', bg='#598987', font=('Muyao-Softbrush',14), command=hide)
bnt.grid(row=20, column=0, padx=10, pady=5)

lb_bnt = tk.Label(root,  fg='white', bg='#678F8D', font=('Muyao-Softbrush',24))
lb_bnt.grid(row=30, column=0, padx=10, pady=5)

lb_bnt2 = tk.Label(root,text='') #隱藏標籤
t()

var_1 = tk.StringVar() #最後取時區
lb_time = tk.Label(root, textvariable=var_1, fg='white', bg='#678F8D', font=('Muyao-Softbrush',24))
lb_time.grid(row=40, column=0, padx=10, pady=(10,10))

root.mainloop()
