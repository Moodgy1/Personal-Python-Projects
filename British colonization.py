#Welcome to my game once you run the script it will create a high-scores.json file
#that will store all you're high scores. If you want to exit full screen use the "esc" key on your keyboard.
#If you want to reset the highscores you can delete the high-scores.json file, and the script will automatically
#create a new blank json file to reset all highscores.



# ------------------------------------- START OF CODE. DO NOT CHANGE ANYTHING --------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, font
import json
import os
import time as t



high_scores_file = 'high_scores.json'

if os.path.exists(high_scores_file):
    with open(high_scores_file, 'r') as f:
        high_scores = json.load(f)
else:
    high_scores = {}


#setting fonts and colors and stuff like that gang


TITLE_FONT = ("Comic Sans MS", 24, "bold")
TEXT_FONT = ("Comic Sans MS", 24, "bold")
BUTTON_FONT = ("Comic Sans MS", 24, "bold")
BG_COLOR = "#1e1e1e"  
FG_COLOR = "#ffffff"  
BUTTON_COLOR = "#333333"
HIGHLIGHT_COLOR = "#4caf50"
CIRCLE_COLOR = "#4caf50"
green = "\033[92m"
red = "\033[91m"
bright_white = "\033[97m"

reset = "\033[0m"


class ColonizationGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"British Colonization Learning Game")
        self.root.configure(bg=BG_COLOR)
        self.root.attributes("-fullscreen", True)  
        self.root.bind("<Escape>", self.toggle_fullscreen)  # a way to exit fullscreen 
        
        
        self.player_name = ""
        self.total_score = 0
        self.country = ""
        self.countries = ["Canada", "Egypt"]  #the countries u will learn bout
        self.country_index = 0  

        self.intro_screen()

    def toggle_fullscreen(self, event=None):
        if self.root.attributes("-fullscreen"):
            self.root.attributes("-fullscreen", False)
        else:
            self.root.attributes("-fullscreen", True)

    def animate_text(self, label, text, delay=30):
        label.config(text="")  
        for i in range(len(text) + 1):
            label.config(text=text[:i])
            label.update()
            t.sleep(delay / 1000)

    
    def intro_screen(self):
        self.clear_screen()
        title = tk.Label(self.root, text=f"British Colonization Learning Game", font=TITLE_FONT, bg=BG_COLOR, fg=HIGHLIGHT_COLOR)
        title.pack(pady=30)

        
        name_label = tk.Label(self.root, text=f"Enter your name:", font=TEXT_FONT, bg=BG_COLOR, fg=FG_COLOR)
        name_label.pack()
        self.name_entry = tk.Entry(self.root, font=TEXT_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
        self.name_entry.pack(pady=10)

        
        self.create_button(f"Start Game", self.start_game).pack(pady=15)
        self.create_button(f"View High Scores", self.show_high_scores).pack(pady=10)
        self.create_button(f"Exit", self.root.quit).pack(pady=10)

    
           # the main menu

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, bd=0,
                           relief="ridge", highlightthickness=0, padx=20, pady=10, command=command)
        button.bind("<Enter>", lambda e: button.config(bg=HIGHLIGHT_COLOR))
        button.bind("<Leave>", lambda e: button.config(bg=BUTTON_COLOR))
        return button

    
    def start_game(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showwarning("No name detected.", "Please enter your name!")
            return
        self.country_index = 0
        self.total_score = 0
        self.start_quiz(self.countries[self.country_index])

    
    def start_quiz(self, country):
        self.country = country
        self.questions = self.get_questions(country)
        self.current_question = 0
        self.show_question()

    
    def get_questions(self, country):
        if country == "Canada":
            return [                #questions for canada
                (f"In which year did Britain officially gain control of Canada?", "1763", ["1763", "1867"]),
                (f"What was the significance of the Hudson's Bay Company?", "It was a British trading company that controlled large parts of Canada.", ["It was a British trading company that controlled large parts of Canada.", "It was the first Canadian political party."]),
                (f"Which event led to the British military victory over the French in Canada?", "The Battle of Quebec in 1759", ["The Battle of Quebec in 1759", "The American Revolutionary War"]),
                (f"What was the main purpose of the Royal Proclamation of 1763?", "To organize new lands and manage relationships with Indigenous peoples.", ["To organize new lands and manage relationships with Indigenous peoples.", "To declare independence from Britain."]),
                (f"What was the significance of the Confederation of Canada in 1867?", "It united the provinces under a federal system while remaining part of the British Empire.", ["It granted Canada complete independence from Britain.", "It united the provinces under a federal system while remaining part of the British Empire."])
            ]
        elif country == "Egypt":
            return [                       #questions for egypt
                (f"When did Britain occupy Egypt?", "1882", ["1882", "1922"]),
                (f"What was Britain's primary interest in Egypt?", "The Suez Canal for trade routes.", ["The Nile River for irrigation.", "The Suez Canal for trade routes."]),
                (f"How did Egypt's strategic importance increase during World War I?", "It was a major supply base and control point for the Allies.", ["It was a major supply base and control point for the Allies.", "It remained neutral and uninvolved in the war."]),
                (f"What was the result of the 1919 Egyptian Revolution against British rule?", "It led to Egypt gaining nominal independence in 1922 but British control remained in key areas.", ["Egypt gained full independence immediately.", "It led to Egypt gaining nominal independence in 1922 but British control remained in key areas."]),
                (f"What was the impact of the 1952 Egyptian Revolution on British presence in Egypt?", "It marked the end of British influence and led to the establishment of the Republic of Egypt.", ["It marked the end of British influence and led to the establishment of the Republic of Egypt.", "It resulted in closer cooperation between Britain and Egypt."])
            ]

    
    def show_question(self):
        self.clear_screen()
        question_text, correct_answer, options = self.questions[self.current_question]
        self.correct_answer = correct_answer

        
        question_label = tk.Label(self.root, text="", font=TEXT_FONT, bg=BG_COLOR, fg=FG_COLOR, wraplength=800)
        question_label.pack(pady=20)
        self.animate_text(question_label, f"Question {self.current_question + 1}: {question_text}", delay=40)

        
        self.option_var = tk.StringVar(value="")

        for option in options:
            option_frame = tk.Frame(self.root, bg=BG_COLOR)
            option_frame.pack(pady=5)

            option_button = tk.Radiobutton(option_frame, text=option, variable=self.option_var, value=option, font=TEXT_FONT,
                                           bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR, activebackground=BG_COLOR)
            option_button.pack(anchor="w", padx=50)

        
            option_button.bind("<Enter>", lambda e: self.create_circle(option_frame))
            option_button.bind("<Leave>", lambda e: self.remove_circle(option_frame))

        submit_button = self.create_button(f"Submit Answer", self.check_answer)
        submit_button.pack(pady=15)

    
    def create_circle(self, frame):
        self.circle = tk.Canvas(frame, width=120, height=120, bg='', highlightthickness=0)
        self.circle.place(x=0, y=0)
        self.circle.create_oval(10, 10, 110, 110, fill=CIRCLE_COLOR, outline=CIRCLE_COLOR)

    
    def remove_circle(self, frame):
        if hasattr(self, 'circle'):
            self.circle.destroy()

    
    def check_answer(self):
        answer = self.option_var.get()
        if answer == self.correct_answer:
            self.total_score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Wrong answer. The correct answer was: {self.correct_answer}")

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.next_country_or_score()

     
    def next_country_or_score(self):
        self.country_index += 1
        if self.country_index < len(self.countries):
            self.start_quiz(self.countries[self.country_index])
        else:
            self.show_score()

    
    def show_score(self):
        self.clear_screen()
        score_label = tk.Label(self.root, text=f"{self.player_name}'s Final Score: {self.total_score}", font=TITLE_FONT, bg=BG_COLOR, fg=HIGHLIGHT_COLOR)
        score_label.pack(pady=30)

        self.update_high_scores()
        self.create_button(f"Back to Main Menu", self.intro_screen).pack(pady=20)

    
    def update_high_scores(self):
        if self.player_name in high_scores:
            if self.total_score > high_scores[self.player_name]:
                high_scores[self.player_name] = self.total_score
        else:
            high_scores[self.player_name] = self.total_score

        with open(high_scores_file, 'w') as f:
            json.dump(high_scores, f)

    
    def show_high_scores(self):
        self.clear_screen()
        title = tk.Label(self.root, text=f"High Scores", font=TITLE_FONT, bg=BG_COLOR, fg=HIGHLIGHT_COLOR)
        title.pack(pady=30)

        if high_scores:
            for name, score in high_scores.items():
                score_label = tk.Label(self.root, text=f"{name}: {score} / 10", font=TEXT_FONT, bg=BG_COLOR, fg=FG_COLOR)
                score_label.pack(pady=5)
        else:
            no_scores_label = tk.Label(self.root, text=f"No high scores yet!", font=TEXT_FONT, bg=BG_COLOR, fg=FG_COLOR)
            no_scores_label.pack(pady=5)

        self.create_button(f"Back to Main Menu", self.intro_screen).pack(pady=20)

    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ColonizationGameApp(root)
    root.mainloop()