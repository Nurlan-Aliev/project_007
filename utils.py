def input_data(message=""):
    choice = input(f"{message}\n-> ")
    print()
    return choice


def join(data, sep="* "):
    return "\n".join(f"{sep}{item}" for item in data)
