# #1) შემოაყვანიეთ მომხმარებელს რაღაცა სიტყვა:
# -> შეამოწმეთ არის თუ არა 'a' ან 'A' ამ სიტყვაში/ტექსტში
# -> შეამოწმეთ თუ არ არის სიტყვა 'car' ამ სიტყვაში/ტექსტში

# userinp = input("enter any word: ")
# if "a" in userinp or "A" in userinp:
#     print("there is a or A in your text: ")

# if not "car" in userinp:
#     print("there isnt car in your word")
# else:
#     print("there is car in your car")

# for i in range(10):
#     print(i,"სერიოზული გამოთვლა")
#     if i==5:
#         break
# print(" for ციკლი დასრულდა")

# counter = 0
# while counter < 10:
#     print(counter< "სერიოზული გამოთვლა")
#     counter += 1
#     if counter >5:
#         break

# for i in range(10):
#     if i ==5 or i==8:
#         continue
#     print(i,'სერიოზული გამოთვლა')
    
# print('for ციკლი დასრულდა')

# counter = 0
# while counter < 10:
#     counter += 1
#     if counter == 5:
#     print(counter,'სერიოზული გამოთვლა')


# 2) მომხმარებელს შემოატანინეთ ტექსტი.
# -> დაუარეთ ამ ტექტის ასოებს for ლუპით
# -> თუ ასო არის 'a' ან 'A' დასკიპეთ, სხვა შემთხვევაში დაპრინტეთ ასო

# მაგალითა: შემოიყვანა 'bananA'
# უნდა დაიპრინტოს: 
# b
# n
# n
word = input('enter any word: ')
for i in word:
     if i =='a' or i =='A':
         continue
     print(i)