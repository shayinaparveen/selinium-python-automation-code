from modules.addition import addition
from modules.substraction import s1
from modules.multiplication import multiplication


class division(multiplication, s1, addition):
    def div(self):
        z = self.x / self.y
        print("Division of 2 numbers:", z)


d = division()
print(d.sum())
print(d.sub())
print(d.mult())
print(d.div())
