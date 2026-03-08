
birth_month = int(input("What month were you born in? (Enter a number from 1-12) "))
birth_day = int(input("What day of the month were you born on? "))

if (birth_month == 1 and birth_day >= 20) or (birth_month == 2 and birth_day <= 18):
    zodiac_sign = "Aquarius"
elif (birth_month == 2 and birth_day >= 19) or (birth_month == 3 and birth_day <= 20):
    zodiac_sign = "Pisces"
elif (birth_month == 3 and birth_day >= 21) or (birth_month == 4 and birth_day <= 19):
    zodiac_sign = "Aries"
elif (birth_month == 4 and birth_day >= 20) or (birth_month == 5 and birth_day <= 20):
    zodiac_sign = "Taurus"
elif (birth_month == 5 and birth_day >= 21) or (birth_month == 6 and birth_day <= 20):
    zodiac_sign = "Gemini"
elif (birth_month == 6 and birth_day >= 21) or (birth_month == 7 and birth_day <= 22):
    zodiac_sign = "Cancer"
elif (birth_month == 7 and birth_day >= 23) or (birth_month == 8 and birth_day <= 22):
    zodiac_sign = "Leo"
elif (birth_month == 8 and birth_day >= 23) or (birth_month == 9 and birth_day <= 22):
    zodiac_sign = "Virgo"
elif (birth_month == 9 and birth_day >= 23) or (birth_month == 10 and birth_day <= 22):
    zodiac_sign = "Libra"
elif (birth_month == 10 and birth_day >= 23) or (birth_month == 11 and birth_day <= 21):
    zodiac_sign = "Scorpio"
elif (birth_month == 11 and birth_day >= 22) or (birth_month == 12 and birth_day <= 21):
    zodiac_sign = "Sagittarius"
else:
    zodiac_sign = "Capricorn"

# Print the zodiac sign
print("Your zodiac sign is:", zodiac_sign)
