import time as t
red = "\033[91m"
green = "\033[92m"       # Declaring vars and importing libraries
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"
white = "\033[37m"       
bright_white = "\033[97m"
bold = "\033[1m"
#################################Beginning of quiz#####################################################

def intro():
    print(f"{bold}Welcome to the British Colonization Learning Game!")
    print(f"{bold}You will learn about the British colonization of Canada and Egypt.")
    print(f"{bold}Make choices and answer questions to explore historical events.")
    print(f"{bold}\nWhich country would you like to learn about first?")
    print(f"{bold}1. Canada")
    print(f"{bold}2. Egypt")
    choice = input(f"{reset}{bold}Enter the number of your choice: ")
    if choice == '1':
        canada_colonization()
    elif choice == '2':
        egypt_colonization()
    else:
        print("Invalid choice, please try again.")
        intro()

def canada_colonization():
    print(f"{bold}\nYou have chosen to learn about British colonization in Canada.")
    print(f"{bold}Let's start with a historical scenario.")
    
    print(f"{reset}{bold}\nQuestion 1: In which year did Britain officially gain control of Canada?")
    print("1. 1763")
    print("2. 1867")
    answer = input(f"{reset}{bold}Enter the number of your answer: ")
    if answer == '1':
        print(f"{bold}{green}Correct! The Treaty of Paris in 1763 marked the end of French rule in Canada.{reset}")
    else:
        print(f"{bold}{red}Incorrect. The correct answer is 1763. Confederation occurred in 1867.{reset}")

    print(f"{reset}{bold}\nQuestion 2: What was the significance of the Hudson's Bay Company?")
    print(f"{reset}{bold}1. It was a British trading company that controlled large parts of Canada.")
    print(f"{reset}{bold}2. It was the first Canadian political party.")
    answer = input(f"{bold}Enter the number of your answer: ")
    if answer == '1':
        print(f"{bold}{green}Correct! The Hudson's Bay Company played a key role in British expansion.{reset}")
    else:
        print(f"{bold}{red}Incorrect. The Hudson's Bay Company was involved in the fur trade and land control.{reset}")

    print(f"{reset}{bold}\nQuestion 3: Which event led to the British military victory over the French in Canada?")
    print(f"{reset}{bold}1. The Battle of Quebec in 1759")
    print(f"{reset}{bold}2. The American Revolutionary War")
    answer = input(f"{reset}{bold}Enter the number of your answer: ")
    if answer == '1':
        print(f"{bold}{green}Correct! The Battle of Quebec in 1759 was a decisive moment in British control over Canada.{reset}")
    else:
        print(f"{bold}{red}Incorrect. The British victory in the Battle of Quebec paved the way for British dominance.{reset}")

    print(f"{reset}{bold}\nQuestion 4: What was the main purpose of the Royal Proclamation of 1763?")
    print(f"{reset}{bold}1. To organize new lands and manage relationships with Indigenous peoples.")
    print(f"{reset}{bold}2. To declare independence from Britain.")
    answer = input(f"{reset}{bold}Enter the number of your answer: ")
    if answer == '1': 
        print(f"{bold}{green}Correct! The Royal Proclamation aimed to structure British rule and protect Indigenous land rights.{reset}")
    else:
        print(f"{bold}{red}Incorrect. The proclamation was issued to help manage territories gained after the Seven Years' War.{reset}")

    print(f"{reset}{bold}\nQuestion 5: What was the significance of the Confederation of Canada in 1867?")
    print(f"{reset}{bold}1. It granted Canada complete independence from Britain.")
    print(f"{reset}{bold}2. It united the provinces under a federal system while remaining part of the British Empire.")
    answer = input(f"{reset}{bold}Enter the number of your answer: ")
    if answer == '2':
        print(f"{bold}{green}Correct! Confederation united the provinces while Canada remained part of the British Empire.{reset}")
    else:
        print(f"{bold}{red}Incorrect. Confederation was about forming a federal union, not full independence.{reset}")

    print(f"{reset}{bold}\nNow let's move to Egypt...")
    egypt_colonization()

def egypt_colonization():
    print(f"{reset}{bold}\nYou have chosen to learn about British colonization in Egypt.")
    
    print(f"{reset}{bold}\nQuestion 1: When did Britain occupy Egypt?")
    print(f"{reset}{bold}1. 1882")
    print(f"{reset}{bold}2. 1922")
    answer = input(f"{reset}{bold}Enter the number of your answer: ")
    if answer == '1':
        print(f"{bold}{green}Correct! Britain occupied Egypt in 1882 after the Anglo-Egyptian War.{reset}")
    else:
        print(f"{bold}{red}Incorrect. Egypt gained nominal independence in 1922, but Britain occupied it in 1882.{reset}")

    print(f"{reset}{bold}\nQuestion 2: What was Britain's primary interest in Egypt?")
    print(f"{reset}{bold}1. The Nile River for irrigation.")
    print(f"{reset}{bold}2. The Suez Canal for trade routes.")
    answer = input(f"{bold}{reset}Enter the number of your answer: ")
    if answer == '2':
        print(f"{bold}{green}Correct! The Suez Canal was a vital trade route linking Europe with Asia.{reset}")
    else:
        print(f"{bold}{red}Incorrect. Britain's primary interest was in securing control of the Suez Canal.{reset}")

    print(f"{reset}{bold}\nQuestion 3: How did Egypt's strategic importance increase during World War I?")
    print(f"{reset}{bold}1. It was a major supply base and control point for the Allies.")
    print(f"{reset}{bold}2. It remained neutral and uninvolved in the war.")
    answer = input(f"{reset}{bold}Enter the number of your answer: ")
    if answer == '1':
        print(f"{bold}{green}Correct! Egypt's location made it a key base for British operations during the war.{reset}")
    else:
        print(f"{bold}{red}Incorrect. Egypt became a strategic asset for the Allies, especially regarding the Suez Canal.{reset}")

    print(f"{reset}{bold}\nQuestion 4: What was the result of the 1919 Egyptian Revolution against British rule?")
    print(f"{reset}{bold}1. Egypt gained full independence immediately.")
    print(f"{reset}{bold}2. It led to Egypt gaining nominal independence in 1922 but British control remained in key areas.")
    answer = input(f"{reset}{bold}Enter the number of your answer: ")
    if answer == '2':
        print(f"{bold}{green}Correct! The revolution resulted in limited independence for Egypt, but Britain retained influence.{reset}")
    else:
        print(f"{bold}{red}Incorrect. While the revolution was significant, Britain kept control of critical matters like defense.{reset}")

    print(f"{reset}{bold}{bold}\nQuestion 5: What was the impact of the 1952 Egyptian Revolution on British presence in Egypt?")
    print(f"{reset}{bold}1. It marked the end of British influence and led to the establishment of the Republic of Egypt.")
    print(f"{reset}{bold}2. It resulted in closer cooperation between Britain and Egypt.")
    answer = input(f"{bold}Enter the number of your answer: ")
    if answer == '1':
        print(f"{bold}{green}Correct! The 1952 revolution led to the end of British influence and the declaration of a republic.{reset}")
    else:
        print(f"{bold}{red}Incorrect. The 1952 revolution significantly reduced British control and influence in Egypt.{reset}")

    print(f"{reset}{bold}\nCongratulations! You have completed the British Colonization Learning Game.")
    print(f"{reset}{bold}You learned about British rule in Canada and Egypt.")

intro()

print(f"{blue}{bold}Credits")
t.sleep(1)
print(f"{yellow}{bold}Mohamed")
t.sleep(1)
print(f"{yellow}{bold}OpenAI Company")
t.sleep(1)
print(f"{yellow}{bold}Thanks for playing")
print(f"{reset}ㅤ")

#By Mohamed
#OpenAI companys ChatGPT contributed for minor error handling
#Thanks for Playing