# Question 16(a)
# Name and School:Karla Patino 

books = []
num = int(input("How many books have you read?"))
x=0
while num > x:
    book=input("Enter the title of the book you've read :")
    books.append(book)
    x+=1
    
if num >= 3:
    print("Fantastic you've read",num,"books! - Keep reading")

print("Book(s) read :")
print(books)


