from random import randint


def make_progression(start, end, step, lost):
    numbers = []

    while start < end:
        numbers.append(str(start))
        start += step

    lost_char = numbers[lost]
    numbers[lost] = ".."
    string_of_number = " ".join(numbers)
    return string_of_number, lost_char


def get_round_data():
    start_range = 1
    end_range = 10
    min_length = 6
    max_length = 10
    lost_chat_from = 4
    lost_chat_to = -5
    start = randint(start_range, end_range)
    end = randint(min_length, max_length)
    step = randint(start_range, end_range)
    length = start + end * step
    lost = randint(lost_chat_to, lost_chat_from)
    str_of_num, correct_answer = make_progression(start, length, step, lost)
    return str_of_num, correct_answer


def get_round_data_prime():
    """Generate return random number and yes if number is prime otherwise no."""
    start_range = 0
    end_range = 50
    number = randint(start_range, end_range)
    if is_prime(number):
        return number, "yes"
    else:
        return number, "no"


def is_prime(number):
    """Return True if number is prime."""
    if number == 0 or number == 1:
        return False
    for index in range(2, round(number / 2) + 1):
        if number % index == 0:
            return False
    return True
