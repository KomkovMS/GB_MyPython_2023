task_1
for j in range(len(lst_obj)):          # !!! O(n)
        if lst_obj[j] in lst_obj[j+1:]:    # !!! O(n)
            return False                   # !!! O(1)
    return True                            # !!! O(1)
    # T(n) = n * n + 1 + 1 = n**2 + 2
