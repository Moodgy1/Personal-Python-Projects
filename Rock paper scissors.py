from tkinter import *
import random

# Define the game logic
def play_game(player_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    if player_choice == computer_choice:
        result_label.config(text='Tie!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        result_label.config(text='You Win!')
    elif player_choice == 'paper' and computer_choice == 'rock':
        result_label.config(text='You Win!')
    elif player_choice == 'scissors' and computer_choice == 'paper':
        result_label.config(text='You Win!')
    else:
        result_label.config(text='Computer Wins!')

# Create a GUI window
root = Tk()
root.title('Rock Paper Scissors')
root.configure(bg='#6699CC')

# Create buttons for the player's choices
button_font = ('Arial', 20, 'bold')
button_padx = 30
button_pady = 10

rock_button = Button(root, text='Rock', font=button_font, padx=button_padx, pady=button_pady, command=lambda: play_game('rock'))
rock_button.grid(row=0, column=0)

paper_button = Button(root, text='Paper', font=button_font, padx=button_padx, pady=button_pady, command=lambda: play_game('paper'))
paper_button.grid(row=0, column=1)

scissors_button = Button(root, text='Scissors', font=button_font, padx=button_padx, pady=button_pady, command=lambda: play_game('scissors'))
scissors_button.grid(row=0, column=2)

# Create a label to display the result
label_font = ('Arial', 30, 'bold')
result_label = Label(root, text='', font=label_font, bg='#6699CC')
result_label.grid(row=1, column=1)

root.mainloop()