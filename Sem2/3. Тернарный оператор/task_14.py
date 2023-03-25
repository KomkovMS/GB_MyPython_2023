"""Понятие тернарного оператора"""

'''condition_if_true if condition else condition_if_false'''

is_checked = True
mode = "checked" if is_checked else "not checked"
print(mode)  # -> checked

'''(if_check_is_false, if_check_is_true)[param_to_check]'''

checked = False
personality = ("не проверено", "проверено")[checked]
print(personality)  # -> проверено
