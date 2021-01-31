
class Calculator:
    def __init__(self, init_value=0, max_count_of_attributes=10):
        self.max_count_of_attributes = max_count_of_attributes
        self.value = init_value
        self.start_iteration = True

    # при итерирование возращать одно value
    def __iter__(self):
        self.start_iteration = True
        return self

    def __next__(self):
        if self.start_iteration:
            self.start_iteration = False
            return self.value
        else:
            raise StopIteration

    #

    # ограниченность кол-ва атрибутов

    def __setattr__(self, key, value):
        if key == 'max_count_of_attributes':
            if key in self.__dict__:
                print('Максимальное количество атрибутов фиксируется при создании калькулятора')
                return
            else:
                self.__dict__[key] = value
                return

        if key in self.__dict__ or len(self.__dict__) < self.max_count_of_attributes:
            self.__dict__[key] = value
        else:
            print('Слишком много атрибутов: ' + key)

    #

    # функционал калькулятора
    def __add__(self, other):
        result = self
        if isinstance(other, Calculator):
            result.value += other.value
        else:
            result.value += other
        return result

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        result = self

        if isinstance(other, Calculator):
            result.value -= other.value
        else:
            result.value -= other
        return result

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        result = self
        if isinstance(other, Calculator):
            result.value *= other.value
        else:
            result.value *= other
        return result

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        result = self
        if isinstance(other, Calculator):
            result.value /= other.value
        else:
            result.value /= other
        return result

    def __rtruediv__(self, other):
        return self /other

    def __floordiv__(self, other):
        result = self
        if isinstance(other, Calculator):
            result.value //= other.value
        else:
            result.value //= other
        return result

    def __rfloordiv__(self, other):
        return self//other

    def __pow__(self, other):
        result = self
        if isinstance(other, Calculator):
            self.value **= other.value
        else:
            self.value **= other
        return result

    def __rpow__(self, other):
        return self**other

    def __repr__(self):
        calculator_string = "\n"
        for element in self.__dict__.keys():
            if element != "max_count_of_attributes" and element != "start_iteration":
                calculator_string += element + "=" + str(self.__dict__[element]) + '\n'
        calculator_string += '\n'
        return calculator_string

    def __str__(self):
        return str(self.__dict__)

    #


if __name__ == '__main__':
    calc1 = Calculator(init_value=100, max_count_of_attributes=4)


    print(*(Calculator(10) + 5))
    print(*(10 + Calculator(20)))
    print(*(Calculator(1) + Calculator(5)))
    print(*(10 - Calculator(200)))
    print(*(Calculator(7) * Calculator(100)))
    print(*(Calculator(47 ) /10))
    print(*(100 /Calculator(34)))
    print(*(Calculator(13 )//Calculator(6)))
    print(*(Calculator(3 )**2))
    print(*(Calculator(4 )**Calculator(3)))

    print(calc1.__repr__())

    print(str(calc1))
    calc1.x = 1
    calc1.y = 2
    calc1.z = 3
    calc1.n = 4

    for calc in calc1:
        print("Calculator: " + str(calc))
