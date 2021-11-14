prev_calculations = []


class Calculation:
    def __init__(self,calc_input):
        self.calc_input = calc_input

    def perform_calculation(self):
        self.calc_input = self.calc_input.strip("=")
        calculated = eval(self.calc_input)
        return f"{self.calc_input}={calculated}"

    def check_valid_input(self):
        num_operators = 0
        i = 0
        for characters in self.calc_input:
            if characters == " ":
                print("\nPlease don't add spaces to the calculation.")
                return False
                break
            if characters not in ["+", "-", "*", "/", "=", "."]:
                if not characters.isdigit():
                    print("\nPlease only enter '+' '-' '/' '*' '=' and numbers.")
                    return False
                    break
            if characters in ["+", "-", "*", "/"]:
                if not self.calc_input[i + 1].isdigit() and self.calc_input[i + 1] != "-":
                    print("\nA number must be after an operator.")
                    return False
                    break
                else:
                    num_operators += 1
            i += 1
        if num_operators < 1:
            print("\nCalculation needs at least one valid operator.")
            return False
        else:
            if self.calc_input[-1] != "=":
                print("\nPlease end your calculation with '='")
                return False
            else:
                return True


def display_menu():
    print("\nCalculator application. Here are the available options:\n"
          "1. Perform new calculation\n"
          "2. View previous calculations\n"
          "3. Return to main menu\n"
          "4. Help")


def new_calc():
    calculation = input("\nThe following operators are available (+, -, *, / ). End your calculation with '='\n"
                        "Enter your calculation: ")
    calculation = Calculation(calculation)
    if calculation.check_valid_input():
        try:
            answer = calculation.perform_calculation()
            print(f"\n{answer}")
            prev_calculations.append(answer)
        except SyntaxError:
            print("\nMake sure you only have one '=' in the calculation")
            new_calc()
        except ZeroDivisionError:
            print("\nSorry, computers cannot divide a value 0, they aren't smart enough for that.")
            new_calc()
    else:
        new_calc()


def display_previous_calcs():
    if len(prev_calculations) == 0:
        print("\nNo calculations stored.")
    else:
        for calculation in prev_calculations:
            print(f"\n{calculation}")


def calculator_main():
    calc_open = True
    while calc_open:
        display_menu()
        function_selection = input("Please enter your choice of function (1, 2, 3 or 4): ").strip(" ")
        if function_selection in ["1","2","3","4"]:
            if function_selection == "1":
                new_calc()
            elif function_selection == "2":
                display_previous_calcs()
            elif function_selection == "3":
                calc_open = False
            elif function_selection == "4":
                print("\nEnter the number of the function you would like to perform, for example: to perform a new\n"
                      "calculation enter '1'. A new calculation can only contain numbers and the following operators\n"
                      "(+, -, *, / ). End your calculation with a '=' and then press enter. If the calculation is\n"
                      "valid the answer will be displayed and the calculation will be remembered. To view previous\n"
                      "calculations type 2 at the main menu. Entering 3 at the main menu will return you to the\n"
                      "application selection menu.")
        else:
            print(f"\n{function_selection} is not a valid input, choose from 1, 2, 3 or 4.")

