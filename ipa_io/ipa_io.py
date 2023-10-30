import numpy as np

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[34m'
RESET = '\033[0m'


def input_lpp() -> tuple[np.array, np.array, np.array, float]:
    """
    Function reads input and returns
        1) maximize or minimize - true or false correspondingly.
        1) vector of coefficients of objective function - C.
        2) A matrix of coefficients of constraint function - A.
        3) A vector of right-hand side numbers - b.
        4) Learning rate - alpha.
    """

    print(BLUE + "Enter the number of variables in z function")

    var_count = 0
    while True:
        try:
            input_args = input().split()
            if len(input_args) != 1:
                print(RED + "Only one argument is required, please re-enter the number of variables" + BLUE)
                continue
            var_count = int(input_args[0])
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion for number of variables: {e}" + BLUE)

    print("Enter the number of constraints")

    constr_count = 0
    while True:
        try:
            input_args = input().split()
            if len(input_args) != 1:
                print(RED + "Only one argument is required, please re-enter the number of constraints" + BLUE)
                continue
            constr_count = int(input_args[0])
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion for number of constraints: {e}" + BLUE)

    print(f"Enter the line with {GREEN}{var_count + constr_count}{BLUE} coefficients of the objective function "
          f"separated by spaces")

    c = np.array([])
    while True:
        try:
            input_args = input().split()
            input_args_len = len(input_args)
            if input_args_len != var_count + constr_count:
                print(RED + f"You need to enter exactly {var_count + constr_count} coefficients, not {input_args_len}")
                print(BLUE + "Please re-enter the coefficients")
            var_list = list(map(float, input_args))
            c = np.array(var_list)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into floats: {e}" + BLUE)

    print(f"Enter {GREEN}{constr_count}{BLUE} lines with {GREEN}{var_count + constr_count}{BLUE} coefficients of "
          f"constraint function separated by spaces")

    a = []
    while True:
        a = []
        try:
            for i in range(constr_count):
                input_str = input().split()
                if len(input_str) != var_count + constr_count:
                    print(RED + f'You need to enter exactly {var_count + constr_count} coefficients,'
                                f' not {len(input_str)}' + BLUE)
                temp = list(map(float, input_str))
                a.append(temp)
            a = np.array(a)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into floats: {e}" + BLUE)

    print(f"Enter the line with {GREEN}{len(c)}{BLUE} coordinates of the initial point ")

    x_initial = np.array([])
    while True:
        try:
            input_args = input().split()
            input_args_len = len(input_args)
            if input_args_len != len(c):
                print(RED + f"You need to enter exactly {len(c)} coefficients, not {input_args_len}" + BLUE)
                print("Please re-enter the coefficients")
            var_list = list(map(float, input_args))
            x_initial = np.array(var_list)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into floats: {e}" + BLUE)

    print("Enter the alpha, learning rate of the method")
    print(f"It's is recommended to use {GREEN}.5{BLUE} or any other number in range (0, 1)")

    alpha = 0
    while True:
        try:
            input_args = input().split()
            if len(input_args) != 1:
                print(RED + "Only one number for alpha is required" + BLUE)
                continue
            alpha = float(input_args[0])
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion for epsilon: {e}" + BLUE)
    # alpha = 0
    # while eps < 1:
    #     alpha += 1
    #     eps *= 10

    return c, a, x_initial, alpha


def output_not_applicable_error() -> None:
    print(RED + "The method is not applicable!" + BLUE)


def output_lpp(x: np.array, result_value: float) -> None:
    """outputs the vector of decision variables and maximum (minimum) value of the objective function"""
    print(f"The resulting vector of decision variables is: \n{GREEN}{x}{BLUE}")
    print(f"And it produced the final value of: {GREEN}{result_value}{BLUE}")


def print_error(msg: str) -> None:
    """prints the red-colored msg in stdout"""
    print(f"{RED}{msg}{BLUE}")