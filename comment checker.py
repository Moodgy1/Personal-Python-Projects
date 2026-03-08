user_input = input("Enter your text: ")
commentlen = len(user_input)
bad_wordschecker = False
bad_words = ['funk', 'spit', 'beach']  # List of bad words. You can add remove or replace the words in this list for your needs.

def check_for_bad_words(input_text):
    for word in bad_words:
        if word in input_text:
            return True
    return False


if check_for_bad_words(user_input.lower()):
    bad_wordschecker = True


if commentlen < 5 or commentlen > 1000 or bad_wordschecker == True:
    print("Your comment is not eligible according to our rules or contains badwords")
else:
    print("The comment you sent was: (" + user_input + ")")    


