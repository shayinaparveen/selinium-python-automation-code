from modules.addition import addition
from modules.substraction import s1


class multiplication(s1, addition):
    def mult(self):
        z = self.x * self.y
        print("Multiplication of 2 numbers:", z)


