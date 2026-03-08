import os
#BLAH BLAH BLAH


def create_notepad_on_desktop():
    
    #Add your Desktop Directory here.
    desktop_path = r'YOUR/DESKTOP/DIRECTORY'
    
    
    notepad_name = input("Enter the name of the Notepad file (without extension): ") + ".txt"
    notepad_content = input("Enter the content for the Notepad file: ")
    
    
    notepad_path = os.path.join(desktop_path, notepad_name)
    
    
    with open(notepad_path, 'w') as file:
        file.write(notepad_content)
        print(f"Notepad file '{notepad_name}' created on the desktop with the specified content.")

create_notepad_on_desktop()
