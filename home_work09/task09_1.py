#  Декоратор 

def decorator(a):
    def nichego(arg):
        import time
        start_time = time.time()
        a(arg)
        end_time = (time.time()) - start_time
        print("{i} - {param}".format(i=end_time, param=arg))
    return nichego


@decorator
def greetings(greet):
    print(greet)


greetings("TeachMeSkills")