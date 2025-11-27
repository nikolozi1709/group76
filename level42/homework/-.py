# 1) შექმენი სია ხილებზე და დაამატე მასში კიდევ 2 ხილი extend() ფუნქციით.
fruits = ["cherry","apple","banana"]
fruits2 = ["grape","pineapple"]
fruits.extend(fruits2)
print(fruits)
# 2) შექმენი სია numbers და დაამატე მასში [40, 50] extend()-ით.
nums = [1,2,3,4,5,6,7]
nums2 = [40,50]
nums.extend(nums)
print(nums)
# 3) შექმენი სია names და შეაბრუნე reverse()-ით.
names = letters = ["a","b","a","c"] 
names.reverse()
print(names)
# 4) შექმენი სია სახელად nums და დათვალე რამდენი ცალი 5 არის მასში count()-ით.
nums3 = [1,2,3,4,5,6,7,8,5,6,7,8,5,5,6,7,]
print(nums3.count(5))
# 5) შექმენი letters = ["a","b","a","c"] და დაბეჭდე რამდენი ცალი "a" არის ჩვენს სიაში.
letters = ["a","b","a","c"] 
print(letters.count("a"))
# 6) შექმენი სია სახელად names და იპოვე "saba"-ს ინდექსი index()-ით.
names_1 = ["lasha","dato","saba","vaxo"]
print(names_1.index("saba"))

# 7) შექმენი list = ["red","green","blue"] და იპოვე რომელ ინდექსზე დგას "blue". გამოიყენე შესაბამისი ფუნქცია.
colors = ["red","green","blue"]
print(colors.index("blue"))
# 8) შექმენი სია სახელად nums და დამატე მასში extend()-ით [7, 8, 9].
nums123 = [1,3,45,1,15]
nums312 = [7, 8, 9]
nums123.extend(nums312)
print(nums123)
# 9) შექმენი სია სახელად foods და დააბრუნე შებრუნებული სია.
foods = ["pizza","xinkali","burger"]
foods.reverse()
print(foods)
# 10) შექმენი სია cities და იპოვე რომელ ინდექსზე დგას "tbilisi".
cities = ["tbilisi","wiatura","qutaisi","sachxere"]
print(cities.index("tbilisi"))
# 11) შექმენი animals = ["cat","dog","cat","cow"] და დაითვალე ამ სიაში რამდენი "cat" არის.
animals = ["cat","dog","cat","cow"]
print(animals.count("cat"))
# 12)შექმენი სია fruits = ["apple", "banana"] და append ფუნქციით დაამატე "grape". დაბეჭდე სია.
fruits_12 = ["apple", "banana"]
fruits_12.append("grape")
print(fruits_12)
# 13)შექმენი სია numbers = [1, 2, 3] და extend()-ით დაუმატე [4, 5]. დაბეჭდე სია.
numbers43 = [1, 2, 3]
nums1 = [4, 5]
numbers43.extend(nums1)
print(numbers43)

# 14)შექმენი სია names = ["goga", "saba"] და insert()-ით ჩასვი "luka" პირველ ინდექსზე. დაბეჭდე სია.
names213 = ["goga", "saba"]
names213.insert(1,"luka")
print(names213)
# 15)შექმენი სია items = ["pen", "pencil", "eraser"] და pop()-ით წაშალე ბოლო ელემენტი; დაბეჭდე განახლებული სია.
items = ["pen", "pencil", "eraser"]
items.pop(2)
print(items)
# 16)შექმენი სია colors = ["red", "green", "blue"] და remove()-ით წაშალე "green". დაბეჭდე შედეგი.
colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)
# 17)შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", შემდეგ დაბეჭდე სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.
foods13 = ["bread", "milk"]
if len(foods13) <=2:
    foods13.append("cheese")
    print(foods13)
else:
    foods13.append("meat")
    print(foods13)
    
# 18)შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი. თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.
nums32 = [10, 20, 30]
user_inp = int(input("enter any number"))
if user_inp in nums32:
    print("already in list")
else:
    nums32.append(40)
    print(nums32)
# 19)შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, შემდეგ insert()-ით ჩასვი ის სიის შუაში (ცენტრალურ ინდექსზე). დაბეჭდე სია.
letters55 = ["a", "b", "c"]
usr_inp = input("enter any letter")
letters55.insert(1,usr_inp)
print(letters55)
# 20)შექმენი სია values = [1, 2, 3, 4]. მომხმარებელს შემოატანინე ინდექსი. თუ ინდექსი სიის ფარგლებშია, pop()-ით ამოშალე შესაბამისი ელემენტი; თუ არა, დაბეჭდე "Index out of range". ბოლოს დაბეჭდე სია.
values = [1, 2, 3, 4]
usrinp = int(input("enter any index"))
if 0 <= usrinp < len(values):
    values.pop(usrinp)
else:
    print("index out of range")
    
print(values)
    
# 21)შექმენი სია pets = ["cat", "dog", "hamster"].  მომხმარებელს შემოატანინე შინაური ცხოველის სახელი. თუ იგი არის სიის შიგნით, remove()-ით ამოშალე და დაბეჭდე "Removed", თუ არა — დაბეჭდე "Not found" და სია უცვლელი დატოვე; საბოლოოდ დაბეჭდე სია.შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", შემდეგ დაბეჭდე სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.
pets = ["cat", "dog", "hamster"]
pet_name = input("enter your pets name: ")
if pet_name in pets :
    pets.remove(pet_name)
    print("removed")
else:
    print("not found!")
print(pets)
# 22)შექმენი სია a = [5, 5, 7]. მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი არის სიის ელემენტი, დაბეჭდე რამდენჯერ არის სიაში - count() ფუნქციის გამოყენებით. სხვა შემთხვევაში append()-ით ჩასვი ის სიაში და დაბეჭდე სია.
a = [5,5,7]
inp = int(input("enter any number: "))
if inp in a :
    print(a.count(inp))
else:
    a.append(inp)
    print(a)
# 23)შექმენი სია queue = ["first", "second"].  მომხმარებელს შემოატანინე ახალი ელემენტი და insert()-ით ჩასვი სიის დასაწყისში. შემდეგ if-ით შეამოწმე სიის სიგრძე — თუ უფრო დიდია 5-ზე, pop()-ით ამოშალე ბოლო ელემენტი; ბოლოს დაბეჭდე სია, თუ არ არის 5-ზე მეტი დაბეჭდე შებრუნებული სია.
queue = ["first", "second"]
usr1_inp = input("enter new element")
queue.insert(0,usr1_inp)
if len(queue) < 5 :
    queue.reverse()
    print(queue)
else:
    queue.pop()
    print(queue)
# 24)შექმენი სია nums = [2, 4, 6].  მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი დადებულია, append()-ით დაამატე; თუ 0-ია ან ნაკლებია ნულზე, დაბეჭდე "Only positive allowed". ბოლოს დაბეჭდე სია.
numbers9 = [2, 4, 6]
ussr_inp = int(input("enter any number: "))
if ussr_inp > 0:
    numbers9.append(ussr_inp)
else:
    print("positives are allowed! ")
print(numbers9)
# 25) შექმენი სია mix = ["x", "y", "z"]. extend()-ით დაუმატე [1, 2, 3]. შემდეგ მომხმარებელს შემოატანინე ასო; თუ ეს ასო არის სიაში, remove()-ით წაშალე პირველად როცა შეგხვდება და დაბეჭდე "Removed", თუ არა — დაბეჭდე "No such element". ბოლოს დაბეჭდე სია.
mix = ["x", "y", "z"] 
lis = [1,2,3]
mix.extend(lis)
usr = input("enter any letter")

if usr in mix:
    mix.remove(usr)
    print("removed")
else:
    print("no matching elements! ")

print(mix)

