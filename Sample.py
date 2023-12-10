def dodaty_ravno(func):
    def wrapper():
        print("============")
        tut_peredaemo_fuction = func()
        print("============")
    return wrapper

@dodaty_ravno
def say_hello():
    print("Say hello!")


result = say_hello()
print(result)
