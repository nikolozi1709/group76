# 1) მომხმარებელს შემოატანინეთ სიტყვა.  
# -> იტერაციით გაიარეთ თითო ასო  
# -> თუ შეხვდებით ასო 'e'-ს ან 'E'-ს გაჩერდით (break)  
# -> დაბეჭდეთ მხოლოდ ის ასოები, რაც მანამდე იყო  
word = input('enter any word: ')
for i in word:
     if i =='e' or i =='E':
         break
     print(i)
# 2) მომხმარებელს შემოატანინეთ წინადადება.  
# -> შეამოწმეთ არის თუ არა ტექსტში სიტყვა 'bad'  
# -> თუ არის, დაპრინტეთ "აკრძალული სიტყვა!"  
# -> თუ არაა, დაპრინტეთ "ყველაფერი რიგზეა"  
usersent = input("enter any sentence: ")
if not "bad" in usersent:
    print("there isn't word bad in usersent")
else:
    print("there is word bad in usersent!")
# 3) მომხმარებელს შემოატანინეთ წინადადება.  
# -> დაუარეთ ტექსტს for ციკლით  
# -> გამოტოვეთ ყველა space => ' '
# -> დაბეჭდეთ ყველა დანარჩენი სიმბოლო  
usersent_1 = input("enter any sentence: ")
for i in usersent_1:
    if i ==" ":
        continue
    print(i)
# 4) მომხმარებელს შემოატანინეთ წინადადება.  
# -> დაუარეთ მას for ლუპით  
# -> გამოტოვეთ ხმოვნები (a, e, i, o, u)  
# -> დაბეჭდეთ მხოლოდ თანხმოვნები და თავისთავათ ყველა სხვა სიმბოლო 
usersent_2 = input("enter any sentence: ")
for i in usersent_2:
    if i =="a" or i =="e" or i=="i" or i=="o" or i=="u":
        continue
    print(i)
# 5) მომხმარებელს შემოაყვანით ორი რიცხვი
# --> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით პირველი რიცხვი ამ შუალედში რომელიც იყოფა 15-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)
num_1 = int(input("enter first number: "))
num_2 = int(input("enter second number: "))

for i in range(num_1,num_2 + 1):
    if i % 15 ==0:
        print(i)
        break
    

# 6) შექმენით უსასრულო while loop:
# --> სანამ მომხმარებელი არ შემოიყვანს 'python is best', მანამდე დაპრინტეთ 'you should learn python'
while True:
    word0 = input("enter any sentence: ")
    if word0 == 'python is best':
        print("done")
        break
    else:
        print('you should learn python!')
    
# 7) \<.BOSS.>/ 
# მომხმარებელს შემოაყვანით ორი რიცხვი
# --> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით მესამე რიცხვი ამ შუალედში რომელიც იყოფა 3-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
count = 0
for i in range(num1,num2 +1 ):
    if i %3 ==0:
        count +=1
        if count ==3:
            print(i)
            break