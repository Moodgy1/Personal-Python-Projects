from tkinter import *

# Create a function to play FLAMES
def play_flames():
    name1 = name1_entry.get().lower().replace(' ', '')
    name2 = name2_entry.get().lower().replace(' ', '')
    
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
            
    count = len(name1) + len(name2)
    
    flames = ['Friends', 'Lovers', 'Angry', 'Marriage', 'Engaged', 'Siblings']
    
    while len(flames) > 1:
        split_index = (count - 1) % len(flames)
        flames = flames[split_index+1:] + flames[:split_index]
        
    flames_label.config(text=flames[0])

# Create a GUI window
root = Tk()
root.title('FLAMES')

# Create entry boxes for the names
name1_label = Label(root, text='Name 1:')
name1_label.grid(row=0, column=0)

name1_entry = Entry(root, width=20)
name1_entry.grid(row=0, column=1)

name2_label = Label(root, text='Name 2:')
name2_label.grid(row=1, column=0)

name2_entry = Entry(root, width=20)
name2_entry.grid(row=1, column=1)

# Create a button to play FLAMES
play_button = Button(root, text='Play', command=play_flames)
play_button.grid(row=2, column=1)

# Create a label to display the result
flames_label = Label(root, text='')
flames_label.grid(row=3, column=1)

root.mainloop()