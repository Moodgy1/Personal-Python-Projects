




import time as t   #here I  imported the time library and renamed it to "t" so i can type it faster  and i imported this so i can use the "time.sleep" function

bully = False                #here i created the variable that will determine if your a bully or not
positive_answers = 0
age = int(input("\033[1m What is your age? "))  # ask for the player's age
empathy = input("\033[1m do you feel empathetic for others? ") # asks if they feel empathy for others
helpfulness = input("\033[1m Do you consider your self a helpful person? ") # asks if they're helpful
influence = input("\033[1m Do you have such a strong influence that people look up to you? ") # asks if people look up to them / big influence


if influence == "y":
    influ = True
else:
    influ = False


if helpfulness == "y":
    helpful = True
else:
    helpful = False


if age >= 18:
    print("\033[1m You're 18 or older, the game will be harsher.") # and here it asks for your age and if your over 18 it will be harsher to you
    harsher = True
else:
    print("\033[1m You are under the age of 18 the game will not be harsh. ")
    harsher = False





if empathy == "y":
    empathyy = True
else:
    empathyy = False





#here are the questions that it will ask you some questions lower your score so your less likey to be a bully or highers your score so your more likely to be a bully





a = input("\033[1m Do you feel better when insulting people? ")
if a == "y":
    positive_answers += 1
    bully = True
if harsher == True and a == "y":
    positive_answers += 1
    
b = input("\033[1m Do you think you're better than classmates? ")
if b == "y":
    positive_answers += 1
if harsher == True and b == "y":
    positive_answers += 1


c = input("\033[1m Do you watch or laugh at people when they get bullied? ")
if c == "y":
    positive_answers += 1
if harsher == True and c == "y":
    positive_answers += 1
if helpful == True and c == "n":
    positive_answers -= 0.5
if influ == True and c == "y":
    positive_answers += 1
    
    
d = input("\033[1m Do you choose your friends based on their weight or looks? ")
if d == "y":
    positive_answers += 1
    bully = True
if harsher == True and d == "y":
    positive_answers += 1
    
    
    
e = input("\033[1m Do your actions result in other people experiencing physical or emotional pain? ")
if e == "y":
    positive_answers += 1
    bully = True
if harsher == True and e == "y":
    positive_answers += 1

f = input("\033[1m Do you think your religion is superior to other religions? ")
if f == "y":
    positive_answers += 1
if harsher == True and f == "y":
    positive_answers += 1
    
    
g = input("\033[1m Do you choose your friends based on their race, ethnicity, or culture? ")
if g == "y":
    positive_answers += 1
    bully = True
if harsher == True and g == "y":
    positive_answers += 1
    
    
h = input("\033[1m When someone makes a mistake, are you quick to judge them? ")
if h == "y":
    positive_answers += 1
if harsher == True and h == "y":
    positive_answers += 1
if helpful == True and h == "y":
    positive_answers -= 0.5
    
    
    
i = input("\033[1m Do you call people mean names often? ")
if i == "y":
    positive_answers += 1
if harsher == True and i == "y":
    positive_answers += 1
    
j = input("\033[1m Do you help people in need? ")

if j == "y":
    positive_answers -= 1
if empathyy == True and j == "y":
    positive_answers -= 1
if helpful == True and c == "y":
    positive_answers -= 1
    
    
k = input("\033[1m Do you help people when they're being bullied? ")

if k == "y":
    positive_answers -= 1
if  empathyy == True and k == "y":
    positive_answers -= 1
if helpful == True and c == "y":
    positive_answers -= 0.5
    

l = input("Have you ever comforted someone at their lowest time of their lives ")

if l == "y":
    bully = False
    positive_answers -= 3
if empathyy == True and l == "y":
    positive_answers -= 1

m = input("\033[1m Do you cause people embarassment for who they are? ")

if m == "y":
    bully = True
    positive_answers += 1
if harsher == True and m == "y":
    positive_answers += 1
    
    
n = input("\033[1m Do you talk about other people negatively online? ")

if n == "y":
    bully = True
    positive_answers += 2
if harsher == True and n == "y":
    positive_answers += 1
if influ == True and n == "y":
    positive_answers += 1

o = input("\033[1m Do you brag your posseison to someone who doesn't have it? ")

if o == "y":
    positive_answers += 1
if harsher == True and o == "y":
    positive_answers += 1
    
       
if positive_answers >= 3 or bully: # here it checks if you answered yes to 3 or more question or if youve answered yes to a very bad trait
   




    t.sleep(1)
    
    print(".")
    
    t.sleep(1)
    
    print("..")
    
    t.sleep(1)
    
    print("...")
    
    
    t.sleep(1)
    
    print("\033[1m im sorry, but you failed. This is your score😔", positive_answers)    # This part tells you that you are a bully and tells you your score
    print("\033[1m You Are A Bully, Try to be Better 😔")
    
    
    if positive_answers < 0:
        positive_answers = 0
    
    
else:
    
    
    if positive_answers < 0:
        positive_answers = 0
    
    
    t.sleep(1)
    
    print(".")
    
    
    t.sleep(1)
    
    print("..")
    
    t.sleep(1)

    print("...")
    
    t.sleep(1)

    
    print("\033[1m You Are Not A Bully, Good Job! 😁")
                                                # this section tellls your not a bully and what your score is
    
    print("\033[1m here is your score! 😁", positive_answers)


    
    


    
    #THANK YOU FOR PLAYING    