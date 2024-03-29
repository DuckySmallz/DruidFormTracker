from src import *

# Variables
weekly = ['aurostor', 'fyrakk']
daily = ['moragh', 'mosa', 'cain', 'ristar', 'keevah', 'ashwhisper']
change = True

# Functions

def popup(name):
    name_caps = str.capitalize(name)
    win = Toplevel(bg="#000000")
    win.iconbitmap('assets/DFT.ico')
    win.geometry(f'300x150+{int(screen_width/2-150)}+{int(screen_height/2-75)}')
    win.title('Form Drop?')
    wintitle = Label(win,text=f"Did {name_caps} drop a form?", font=('arial',15,'bold'),bg='#000000',fg='#ffffff')
    wintitle.place(x=25,y=50)
    def yes():
        global change
        change = True
        file = open('data/save.json','r')
        data = load(file)
        file.close()
        data[name]['item_dropped'] = "True"
        file = open('data/save.json','w')
        dump(data,file,indent=4)
        file.close()
        win.destroy()
    def no():
        global change
        change = True
        file = open('data/save.json','r')
        data = load(file)
        file.close()
        data[name]['dead'] = "True"
        file = open('data/save.json','w')
        dump(data,file,indent=4)
        file.close()
        win.destroy()
    yes_button = Button(win,text='Yes',height=1, width=10,command=yes)
    yes_button.place(x=25,y=100)
    no_button = Button(win,text='No',height=1,width=10,command=no)
    no_button.place(x=200,y=100)
    win.update()
    sleep(0.025)

def aurostor_func():
    popup('aurostor')

def fyrakk_func():
    popup('fyrakk')

def moragh_func():
    popup('moragh')

def mosa_func():
    popup('mosa')

def cain_func():
    popup('cain')

def ristar_func():
    popup('ristar')

def keevah_func():
    popup('keevah')

def ashwhisper_func():
    popup('ashwhisper')

def weekly_func():
    file = open('data/save.json','r')
    data = load(file)
    file.close()
    for n in weekly:
        if data[n]['item_dropped'] == "True":
            pass
        elif data[n]['dead'] == "True":
            data[n]['dead'] = "False"
            file = open('data/save.json','w')
            dump(data,file,indent=4)
            exec(f'{n}_x_place.destroy()')
            file.close()
        else:
            pass
    
def daily_func():
    file = open('data/save.json','r')
    data = load(file)
    file.close()
    for n in daily:
        if data[n]['item_dropped'] == "True":
            pass
        elif data[n]['dead'] == "True":
            data[n]['dead'] = "False"
            file = open('data/save.json','w')
            dump(data,file,indent=4)
            exec(f'{n}_x_place.destroy()')
            file.close()
        else:
            pass

def reset_popup():
    win = Toplevel(bg='#000000')
    win.title('Are you sure?')
    win.geometry(f'300x150+{int(screen_width/2-150)}+{int(screen_height/2-75)}')
    win.iconbitmap('assets/DFT.ico')
    def reset():
        file = open('data/save.json','r')
        data = load(file)
        file.close()
        for n in daily:
            data[n]['item_dropped'] = 'False'
            data[n]['dead'] = 'False'
            try:
                exec(f'{n}_x_place.destroy()')
            except:
                pass
            try:
                exec(f'{n}_check_place.destroy()')
            except:
                pass
        for n in weekly:
            data[n]['item_dropped'] = 'False'
            data[n]['dead'] = 'False'
            try:
                exec(f'{n}_x_place.destroy()')
            except:
                pass
            try:
                exec(f'{n}_check_place.destroy()')
            except:
                pass
        file = open('data/save.json','w')
        dump(data,file,indent=4)
        file.close()
        win.destroy()
    def no():
        win.destroy()
    verify = Label(win,text='Are you sure you want to reset?',font=('aerial',10,'bold'),bg="#000000",fg='#FFFFFF')
    verify_cont = Label(win,text='(This will erase all progress recorded)',font=('aerial',8),bg="#000000",fg='#FFFFFF')
    yes_button = Button(win,text='Yes',height=2,width=10,command=reset)
    no_button = Button(win,text='No',height=2,width=10,command=no)
    verify.place(x=40,y=15)
    verify_cont.place(x=45,y=35)
    yes_button.place(x=40,y=100)
    no_button.place(x=160,y=100)
    win.update()
    sleep(0.025)

# Window Init
root = Tk()
screen_height=root.winfo_screenheight()
screen_width=root.winfo_screenwidth()
root.resizable(False,False)
root.title("Druid Form Tracker V 1.1.0")
root.geometry(f'1300x825+{int(screen_width/2-650)}+{int(screen_height/2-413)}')
canvas = Canvas(root)
canvas.config(height=825, width=1300, bg='#000000')
canvas.pack()

# Asset Init
logo = PhotoImage(file='assets/logo.png')
check = PhotoImage(file='assets/check.png')
x = PhotoImage(file='assets/x.png')
aurostorpic = PhotoImage(file='assets/aurostor.png')
fyrakkpic = PhotoImage(file='assets/fyrakk.png')
moraghpic = PhotoImage(file='assets/moragh.png')
mosapic = PhotoImage(file='assets/mosa.png')
cainpic = PhotoImage(file='assets/cain.png')
ristarpic = PhotoImage(file='assets/ristar.png')
keevahpic = PhotoImage(file='assets/keevah.png')
ashwhisperpic = PhotoImage(file='assets/ashwhisper.png')

# Labels
logo_place = Label(image=logo,bg='#000000')
title = Label(text="Druid Form Tracker V1.1.0", font=('arial',25,'bold'),bg='#000000',fg='#ffffff')
aurostor_place = Label(image=aurostorpic,bg='#000000')
fyrakk_place = Label(image=fyrakkpic,bg='#000000')
moragh_place = Label(image=moraghpic,bg='#000000')
mosa_place = Label(image=mosapic,bg='#000000')
cain_place = Label(image=cainpic,bg='#000000')
ristar_place = Label(image=ristarpic,bg='#000000')
keevah_place = Label(image=keevahpic,bg='#000000')
ashwhisper_place = Label(image=ashwhisperpic,bg='#000000')
check_place = Label(image=check,bg='#000000')
x_place = Label(image=x,bg='#000000')

# Buttons
aurostor_button = Button(text="Aurostor",height=2,width=20,command=aurostor_func)
fyrakk_button = Button(text="Mythic Fyrakk",height=2,width=20,command=fyrakk_func)
moragh_button = Button(text="Moragh",height=2,width=20,command=moragh_func)
mosa_button = Button(text="Mosa",height=2,width=20,command=mosa_func)
cain_button = Button(text='Cain',height=2,width=20,command=cain_func)
ristar_button = Button(text="Ristar",height=2,width=20,command=ristar_func)
keevah_button = Button(text="Keevah",height=2,width=20,command=keevah_func)
ashwhisper_button = Button(text="Ashwhisper",height=2,width=20,command=ashwhisper_func)
weekly_reset_button = Button(text='Weekly Reset',height=2,width=50,command=weekly_func)
daily_reset_button = Button(text='Daily Reset',height=2,width=50,command=daily_func)
full_reset = Button(text='Full Reset',height=1,width=10,command=reset_popup)

# Window Build
root.iconbitmap('assets/DFT.ico')
logo_place.place(x=575,y=25)
title.place(x=450,y=125)
aurostor_place.place(x=100,y=200)
fyrakk_place.place(x=100,y=300)
moragh_place.place(x=100,y=400)
mosa_place.place(x=100,y=500)
cain_place.place(x=800,y=200)
ristar_place.place(x=800,y=300)
keevah_place.place(x=800,y=400)
ashwhisper_place.place(x=800,y=500)
aurostor_button.place(x=225,y=235)
fyrakk_button.place(x=225,y=335)
moragh_button.place(x=225,y=435)
mosa_button.place(x=225,y=535)
cain_button.place(x=925,y=235)
ristar_button.place(x=925,y=335)
keevah_button.place(x=925,y=435)
ashwhisper_button.place(x=925,y=535)
daily_reset_button.place(x=450,y=700)
weekly_reset_button.place(x=450,y=775)
full_reset.place(x=10,y=10)

# Main Loop
while True:

    # Load JSON data
    if change == True:
        change = False
        data = open('data/save.json','r')
        vars = load(data)
        for n in weekly:
            exec(f'{n}_for_check = PhotoImage(file="assets/check.png")')
            exec(f"{n}_for_x = PhotoImage(file='assets/x.png')")
            if vars[n]['item_dropped'] == 'True':
                exec(f'{n}_check_place = Label(root,image={n}_for_check,bg="#000000")')
                exec(f'{n}_check_place.place(x=vars[n]["x"],y=vars[n]["y"])')
            elif vars[n]['dead'] == 'True':
                exec(f'{n}_x_place = Label(root,image={n}_for_x,bg="#000000")')
                exec(f'{n}_x_place.place(x=vars[n]["x"],y=vars[n]["y"])')
            else:
                pass
        for n in daily:
            exec(f'{n}_for_check = PhotoImage(file="assets/check.png")')
            exec(f"{n}_for_x = PhotoImage(file='assets/x.png')")
            if vars[n]['item_dropped'] == 'True':
                exec(f'{n}_check_place = Label(root,image={n}_for_check,bg="#000000")')
                exec(f'{n}_check_place.place(x=vars[n]["x"],y=vars[n]["y"])')
            elif vars[n]['dead'] == 'True':
                exec(f'{n}_x_place = Label(root,image={n}_for_x,bg="#000000")')
                exec(f'{n}_x_place.place(x=vars[n]["x"],y=vars[n]["y"])')
            else:
                pass
        data.close()
    else:
        sleep(0.025)
        root.update()