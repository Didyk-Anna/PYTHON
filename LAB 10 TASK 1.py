
class Vector :
        def __init__(self, size):
            self.size = size
            self.tops = []

        def get_elements(self):
            for i in range(self.size):
                self.tops.append(float(input('введіть координату {0} = '.format(i + 1))))

        def vector_output(self):
            print(str(self.tops))

        def get_length(self):

            return (sum(map(lambda x: x ** 2, self.tops))) ** (1 / 2)

        def norm_vector(self):
            return [(x / self.get_length()) for x in self.tops]
#------------------------------------------------------

v1 = Vector(int(input(' розмірність = ')))
v1.get_elements()
v1.vector_output()
print(v1.get_length())
print(v1.norm_vector())