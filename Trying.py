# עובדות על פייתון
# Case Sensitive - רגישות לגודל האותיות, כלומר אות קטנה לא שווה לאות גדולה


# print(10 * 10)
# print(10 / 2)
# print(10 % 2)
# print(10.5 / 2)
# print(10.5 % 2)  # מחזיר שארית עשרונית
# print(10 / 2 == 5)  # מחזיר אמת, בלי צורך להשתמש בIF
# print(10.3 * 9)
# print(10.5 != 11)
# print(10.5 == 10.5)

# print("show me")
# print("show me" + "everything")  # מחבר בלי רווח
# print("show me" + " everything")  # מחבר עם רווח

# פייתון לא יודעת לשרשר משתנים מסוגים שונים כמו מספר ומחרוזת !

# print("nina \nhi")  # \n ירידת שורה
# print("nina \thi")  # \t הכנסה פנימה של טקסט
# print("nina \n\thi")  # \t הכנסה פנימה של טקסט

# כברירת מחדל בכל הדפבה פייתן יורדת שורה, ניתן לשנות זאת ע"י הפונקציה end שתגדיר מה יהיה בסוף ההדפסה

#print("nina", end=" ")
#print("nina", end="'")

#print("nina","nomi","aasa")# הדפסה של כמה מילים ע"י שימוש בפסיקים, הפסיקים מתורגמים לרווחים
#print("nina", "nomi", "aasa", sep="|")# פונקצייה SEP מחליפה את צורת המפריד בין המילים מברירת המחדל רווח למה שנגדיר

number = 10 #הגדרת משתנה - ללא צורך בהגדרת סוג המשתנה!
print(number)
print(number+8)

name = "nina"
print(name)

name2 = 'nina'
print(name)

#print(name + ' ' + name2 + number) # לא יכול להדפיס מחרוזת ומספר יחד!!!
print(name + name2)

a, b, c = 1, 2, 3 # הגדרה מרובה של משתנים

# משתנים בוליאנים
var = True
var2 = False

# בפייתון המשתנים מצביעים אל ערך בזיכרון ולכן ניתן לבצע השמה של סוגי משתנים שונים

number1 = 18
number1 = "hallo"

print(number1*5)# prints 5 times the value of number1
print((number1+" ")*5)

# משתנה יכול להכיל את הפלט של ביטוי בוליאני
var3 = 2 == 7
print(var3)

# תו וגם מילה נחשב בפייתון מחרוזת ומשתנה מסוג str
string = 'n'
print(type(string))# type - מדפיס את הטיפוס של המשתנה





