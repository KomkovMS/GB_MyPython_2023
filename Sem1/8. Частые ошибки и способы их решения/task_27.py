# Проблема 7. UnboundLocalError: local variable 'my_var' referenced before assignment
def my_func():
    my_var += 1
    print(my_var)

my_var = 10
my_func()
# Ошибка:
# UnboundLocalError: local variable 'my_var' referenced before assignment

def my_func(my_var):
    my_var += 1
    print(my_var)

my_var = 10
my_func(my_var)
