from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk,Image
from functools import partial
from battle import Battle

root = Tk()
root.title('Pokemon TH')

color_background = '#0F53A6'
color_button = '#A1CBFF'
font1 = ("Arial", 12, BOLD)
font2 = ("Arial", 10)

root.configure(bg=color_background)
#root.geometry('740x475')
pokeball_img = ImageTk.PhotoImage(Image.open('.\images\pokeball.png'))

battle = ''

#Misc Func
def disable_all():
    move1.config(state=DISABLED)
    move2.config(state=DISABLED)
    move3.config(state=DISABLED)
    move4.config(state=DISABLED)
    change_mon_1.config(state=DISABLED)
    change_mon_2.config(state=DISABLED)
    change_mon_3.config(state=DISABLED)
    change_mon_4.config(state=DISABLED)
    change_mon_5.config(state=DISABLED)
    change_mon_6.config(state=DISABLED)

#GUI updates
def update_gui_pkm_names():
    t1 = battle.trainers[0].pokemon[battle.trainers[0].current_mon]
    t2 = battle.trainers[1].pokemon[battle.trainers[1].current_mon]
    if (t1.type[1] == 'None'):
        pkm1_title_data.config(text=''+t1.name+'  '+t1.type[0].upper()+ '  hp: '+str(t1.hp))
    else:
        pkm1_title_data.config(text=''+t1.name+'  '+t1.type[0].upper()+ ', '+t1.type[1].upper()+'  hp: '+str(t1.hp))
    if (t2.type[1] == 'None'):
        pkm2_title_data.config(text=''+t2.name+'  '+t2.type[0].upper()+ '  hp: '+str(t2.hp))
    else:
        pkm2_title_data.config(text=''+t2.name+'  '+t2.type[0].upper()+ ', '+t2.type[1].upper()+'  hp: '+str(t2.hp))

def update_gui_pkm_pic():
    t1 = battle.trainers[0].pokemon[battle.trainers[0].current_mon].name.lower()
    t2 = battle.trainers[1].pokemon[battle.trainers[1].current_mon].name.lower()
    t1_img = ImageTk.PhotoImage(Image.open('./images/'+t1+'.png'))
    pkm1_image.config(image=t1_img)
    pkm1_image.image = t1_img
    t2_img = ImageTk.PhotoImage(Image.open('./images/'+t2+'.png'))
    pkm2_image.config(image=t2_img)
    pkm2_image.image = t2_img

def update_gui_pkm_moves():
    moves = battle.trainers[battle.current_trainer].pokemon[battle.trainers[battle.current_trainer].current_mon].moves
    move1.config(state=NORMAL)
    move2.config(state=NORMAL)
    move3.config(state=NORMAL)
    move4.config(state=NORMAL)
    move1.config(text=moves[0].name+'  '+moves[0].type.upper()+'  '+str(moves[0].pp))
    if (moves[0].pp < 1):
        move1.config(state=DISABLED)
    move2.config(text=moves[1].name+'  '+moves[1].type.upper()+'  '+str(moves[1].pp))
    if (moves[1].pp < 1):
        move2.config(state=DISABLED)
    move3.config(text=moves[2].name+'  '+moves[2].type.upper()+'  '+str(moves[2].pp))
    if (moves[2].pp < 1):
        move3.config(state=DISABLED)
    move4.config(text=moves[3].name+'  '+moves[3].type.upper()+'  '+str(moves[3].pp))
    if (moves[3].pp < 1):
        move4.config(state=DISABLED)

def update_gui_pkm_switch():
    pkmn = battle.trainers[battle.current_trainer].pokemon 

    change_mon_1.config(text=pkmn[0].name)
    if (pkmn[0].is_fainted == True or battle.trainers[battle.current_trainer].current_mon == 0):
        change_mon_1.config(state=DISABLED)
    else: change_mon_1.config(state=NORMAL)

    change_mon_2.config(text=pkmn[1].name)
    if (pkmn[1].is_fainted == True or battle.trainers[battle.current_trainer].current_mon == 1):
        change_mon_2.config(state=DISABLED)
    else: change_mon_2.config(state=NORMAL)

    change_mon_3.config(text=pkmn[2].name)
    if (pkmn[2].is_fainted == True or battle.trainers[battle.current_trainer].current_mon == 2):
        change_mon_3.config(state=DISABLED)
    else: change_mon_3.config(state=NORMAL)

    change_mon_4.config(text=pkmn[3].name)
    if (pkmn[3].is_fainted == True or battle.trainers[battle.current_trainer].current_mon == 3):
        change_mon_4.config(state=DISABLED)
    else: change_mon_4.config(state=NORMAL)
    
    change_mon_5.config(text=pkmn[4].name)
    if (pkmn[4].is_fainted == True or battle.trainers[battle.current_trainer].current_mon == 4):
        change_mon_5.config(state=DISABLED)
    else: change_mon_5.config(state=NORMAL)
    
    change_mon_6.config(text=pkmn[5].name)
    if (pkmn[5].is_fainted == True or battle.trainers[battle.current_trainer].current_mon == 5):
        change_mon_6.config(state=DISABLED)
    else: change_mon_6.config(state=NORMAL)

def update_all_gui_info():
    update_gui_pkm_names()
    update_gui_pkm_pic()
    update_gui_pkm_moves()
    update_gui_pkm_switch()

#Button Functions
def start_game():
    global battle
    try:
        battle = Battle(team1_name.get(), team2_name.get())
        start_confirm.config(state= DISABLED)
        team1_name.config(state=DISABLED)
        team2_name.config(state=DISABLED)
        update_all_gui_info()
    except:
        print("Failed to Create Teams")

def select_move(movenum):
    print(movenum)

def switch_mon(mon_num):
    print(mon_num)

#Emply Labels
empty_label = Label(text='', bg=color_background)
empty_col1 = Label(text="           ", bg=color_background)
empty_col2 = Label(text="           ", bg=color_background)
empty_bottom = Label(text='', bg=color_background)

#Pokemon1 data
pkm1_title_data = Label(root, text='Empty',bg=color_background, font=font1)
pkm1_image = Label(root, image=pokeball_img, bg=color_background)

#Pokemon2 data
pkm2_title_data = Label(root, text='Empty',bg=color_background, font=font1)
pkm2_image = Label(root, image=pokeball_img, bg=color_background)

#Get team information
team1_name = Entry()
team1_name.insert(0, 'team')
team2_name = Entry()
team2_name.insert(0, 'team2')
start_confirm = Button(text='Start', padx=25, command=start_game)

#Current Player
num_player = Label(text="Turn: Player 1", bg=color_background, font=font1)

#Moves
button_length = 75
move1 = Button(text='Move1', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(select_move, 0))
move2 = Button(text='Move2', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(select_move, 1))
move3 = Button(text='Move3', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(select_move, 2))
move4 = Button(text='Move4', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(select_move, 3))

#Swapable Pokemon
change_mon_1 = Button(text='Mon1', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(switch_mon, 0))
change_mon_2 = Button(text='Mon2', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(switch_mon, 1))
change_mon_3 = Button(text='Mon3', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(switch_mon, 2))
change_mon_4 = Button(text='Mon4', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(switch_mon, 3))
change_mon_5 = Button(text='Mon5', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(switch_mon, 4))
change_mon_6 = Button(text='Mon6', bg=color_button, padx= button_length, font=font2, state=DISABLED,command=partial(switch_mon, 5))

#Setup team


#Coloumn0
empty_col1.grid(column=0, row=0)
empty_bottom.grid(column=0, row=12)

#Column1
pkm1_title_data.grid(column=1, row=0)
pkm1_image.grid(column=1, row=1, rowspan=4)

empty_label.grid(column=1, row=5)

move1.grid(column=1, row=7)
move2.grid(column=1, row=8)
move3.grid(column=1, row=9)
move4.grid(column=1, row=10)

#Column2
team1_name.grid(column=2,row=2)
team2_name.grid(column=2,row=3)
start_confirm.grid(column=2,row=4)
num_player.grid(column=2, row=1)

#Column3
pkm2_title_data.grid(column=3, row=0)
pkm2_image.grid(column=3, row=1, rowspan=4)

change_mon_1.grid(column=3, row=6)
change_mon_2.grid(column=3, row=7)
change_mon_3.grid(column=3, row=8)
change_mon_4.grid(column=3, row=9)
change_mon_5.grid(column=3, row=10)
change_mon_6.grid(column=3, row=11)

#Column4
empty_col2.grid(column=5, row=0)

root.mainloop()