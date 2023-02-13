from datetime import datetime


def change_salary(emp_name, salary, is_bonus=False):
    print(f'employee {emp_name} new salary {salary} is_bonus {is_bonus}')
    return salary


print(change_salary('john', 2000, True))


def time_wrapper(fun):
    def wrapper(*args, **kwargs):
        time_of_entry = datetime.now().isoformat()
        print(f'Time of entry is {time_of_entry}')
        result = fun(*args, **kwargs)
        return result

    return wrapper


new_fun = time_wrapper(change_salary)

print(new_fun('jenny', 2200, False))
