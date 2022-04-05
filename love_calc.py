# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_names = name1.lower() + name2.lower()

t1 = both_names.count('t')
tr = both_names.count('r')
tu = both_names.count('u')
te = both_names.count('e')
total_true = (str(t1 + tr + tu + te))






l1 = both_names.count('l')
lo = both_names.count('o')
lv = both_names.count('v')
le = both_names.count('e')
total_love = (str(l1 + lo + lv + le))


true_love = (str(total_true)) + (str(total_love))

love_score = (int(true_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score <= 50 and love_score >= 40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
