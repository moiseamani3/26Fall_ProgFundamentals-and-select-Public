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
        print(f"Hi!! My name is {self.name} and I'm {self.age} years old.")
    def birthday(self):
        self.age = self.age + 1 #self.age += 1`could be used as well`
    def __str__(self):
        return f"{self.name} is {self.age} years old and is a jazz player."

class Bluesplayer(Jazzplayer):
    def __init__(self, name, age):
        super().__init__(name, age)
        print("Hello welcome to blues junction 2026!!")
    def __str__(self):
        # print(super().__str__())
        return f"{self.name} is {self.age} years old and is a blues player."+super().__str__()
    # pass


Bryan = Bluesplayer("Bryan", 40)
print(Bryan)
# Yvan = Jazzplayer("Yvan", 25)
# print(Yvan)

# Mike = Jazzplayer("Mike", 30)
# Mike.birthday()
# print(f"Hello there, I'm {Mike.name}, I'm {Mike.age} and I'm ready to help 'Yvan' with the jazz music journey")


# Yvan = Jazzplayer("Yvan", 25)
# Yvan.birthday()
# print(f"Hello there, I'm {Yvan.name}, I'm {Yvan.age} and I'm ready to help 'Mike' with the jazz music journey")



    
