
class Tale():
    def __init__(self,author,genre,year,name):
        self.author=author
        self.genre=genre
        self.year=year
        self.name=name

    def getAuthor(self):
        return self.author
    
    def getGenre(self):
        return self.genre
    
    def getYear(self):
        return self.year
    
    def getName(self):
        return self.name
    
    def setAuthor(self,author):
        self.author=author

    def setGenre(self,genre):
        self.genre=genre
    
    def setYear(self,year):
        self.year=year

    def toString(self):
        print("\n"+"Name: "+self.getName()+"\n"+"Author: "+self.getAuthor().getName()+"\n"+"Genre: "+self.getGenre()+"\n"+"Year: "+str(self.getYear())+"\n")

class Author():
    def __init__(self,name,gender,datebirth,datedeath):
        self.name=name
        self.gender=gender
        self.datebirth=datebirth
        self.datedeath=datedeath
    
    def getName(self):
        return self.name
    
    def getDateDeath(self):
        return self.datedeath
    
    def getGender(self):
        return self.gender

listAuthors = []

for i in range(2):
    print("Enter Name of the Author")
    name = input()
    print("Enter Gender of the Author")
    gender = input()
    print("Enter the DateBirth of the Author")
    dateBirth = input()
    print("Enter the DateDeath of the Author")
    dateDeath = input()
    author = Author(name,gender,dateBirth,dateDeath)
    listAuthors.append(author)


def searchAuthor(nameAuthor):
    for i in listAuthors:
        if i.getName() == nameAuthor:
            return i

listTales = []

for i in range(2):
    print(f"Book {i+1} ",)
    print('Enter the Name of the Tale')
    name = input()
    print('Enter the Author of the Tale')
    nameauthor = input()
    author = searchAuthor(nameauthor)
    print('Enter the Genre of the Tale')
    genre = input()
    print('Enter the Year of the Tale')
    year = int(input())
    tale = Tale(author,genre,year,name)
    listTales.append(tale)

print('\nList of the Tales')
for i in listTales:
    i.toString()

def foundRafael(listTales):
    print("\nBooks by Rafael Pombo\n")
    for i in listTales:
        if i.getAuthor() == "Rafael Pombo":
            i.toString()

def bookslastCentury(listTales):
    print("\nBooks Last Century \n")
    for i in listTales:
        if i.getYear() < 2001:
            i.toString()

def authorLive(listAuthors):
    print("Authors that are alive")
    for i in listAuthors:
        if i.getDateDeath == "No ha muerto":
            print(i.getName(),"is alive")

def authorFemale(listAuthors):
    print("Female Authors")
    for i in listAuthors:
        if i.getGender() == "F":
            print(i.getName())

foundRafael(listTales) 
bookslastCentury(listTales) 
authorLive(listAuthors)
authorFemale(listAuthors)

