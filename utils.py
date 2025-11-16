def input_data(message=''):
    choice = input(f'{message}\n-> ')
    print()
    return choice


def join(data):
    return "\n".join(f"* {item}" for item in data)
