##temperature = 36
##print(f"The temperature is:{temperature}")


##name = "Monro"
##age = 35
##email = "monro@gmail.com"
# import random
#classes
class Jazzplayer:
    def __init__(self, name, age):
        print("Hello welcome to jazz junction 2026!!")
        self.name = name
        self.age = age
    def birthday(self):
        self.age = self.age + 1
    def __str__(self):
        return f"{self.name} is {self.age} years old."



Mike = Jazzplayer("Mike", 30)
Mike.birthday()
print(f"Hello there, I'm {Mike.name}, I'm {Mike.age} and I'm ready to help 'Yvan' with the jazz music journey")


Yvan = Jazzplayer("Yvan", 25)
Yvan.birthday()
print(f"Hello there, I'm {Yvan.name}, I'm {Yvan.age} and I'm ready to help 'Mike' with the jazz music journey")



    
