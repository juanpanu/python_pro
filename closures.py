def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Only str accepted"
        return string * n
    return repeater


def make_division_by(n):
    def divide(x):
        return x//n
    return divide

## Decorador
def mayusculas(func) :
    def envoltura(texto) :
        return func(texto).title()
    return envoltura
@mayusculas
def mensaje( nombre) :
    return f'{nombre}, recibiste un mensaje'


def run():
    # repeat_5 = make_repeater_of(5)
    # print(repeat_5("hola"))
    # division_by_3 = make_division_by(3)
    # print(division_by_3(18))

    # division_by_5 = make_division_by(5)
    # print(division_by_5(100))

    # division_by_18 = make_division_by(18)
    # print(division_by_18(54))
    jp=mensaje('juan')
    print(jp)

if __name__ == '__main__':
    run()
