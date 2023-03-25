"""Не локальная область видимости"""

# ПРОБЛЕМА
def ext_func():
    """

    :return:
    """
    my_var = 0

    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var
    return int_func


func_obj = ext_func()
print(func_obj)
print(func_obj())
print(func_obj())
print(func_obj())


"""UnboundLocalError: local variable 'my_var' referenced before assignment"""

# РЕШЕНИЕ
def ext_func():
    my_var = 0
    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var
    return int_func


func_obj = ext_func()
print(func_obj)
print(func_obj())
print(func_obj())
print(func_obj())

"""
<function ext_func.<locals>.int_func at 0x0000009E70C658C8>
1
2
3
"""
