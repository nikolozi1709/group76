# 1) შექმენით სია სადაც შეინახავთ სხვადასხვა ქალაქების სახელებს.  
#    for loop ით დაბეჭდეთ მხოლოდ ის ქალაქები, რომელთა სახელის სიგრძე მეტია 6-ზე.
city = ["tbilisi","batumi","paris","wiatura","shota"]
for i in city:
    if len(i) > 6:
        print(i)
    
# 2) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად იყოფა 15-ზე.
words_random = ["dassasasadsa","adsfgshedfesad","gasasdaffaff","aaaaaaaaaaaaaaa"]
for i in words_random:
        if len(i) % 15 ==0:
            print(i)
        
        
# 3) შექმენით სია რიცხვებით.  
# -> გამოიყენეთ for loop რათა დათვალოთ რამდენი რიცხვია სიაში.  
# -> არ გამოიყენოთ len() — დაითვალეთ ხელით.
numbers = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in numbers:
    count +=1
print(count)
   
# 4) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად 5 სიმბოლოა.
words = ["mama","deda","sasha","lashvardi"]
for i in words:
    if len(i) == 5:
        print(i)
        
    

# 5) მომხმარებელს შემოატანინე წინადადება.  
# -> გაიგე რამდენი სიმბოლოა წინადადებაში.  
# -> for ციკლით დათვალე რამდენი აso "a" ან "A" არის ტექსტში.
user_inp = input("enter any sentence: ")
print(len(user_inp))
count_1 = 0
for i in user_inp:
    if i == "a" or i =="A":
        count_1 +=1
print(f"count of (a,A)is {count_1}")
        
        


# 6) <= Boss Level =>
# შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
# --> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი
Words = ["dassasasadsa","adsfgshedfesad","gasasdaffaff","AAAAAAAAAAAAAAAAAAAAAAAAAAAA"]
long = ""
for i in Words:
    if len(i) > len(long):
        long = i
print(long)
    
        