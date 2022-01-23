"""The Game "Guess the number"
The computer makes its own guess and guesses the number itself
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: number of tries
    """
    count = 0
    x = 1
    y = 101
    predict_number = np.random.randint(x, y)
    if number == predict_number:
        return count == 1 # when guessing on the first try
    else:               # reducing the interval for searching for a number
        while number != predict_number:
            if number > predict_number: # reducing the left border of the interval
                x = predict_number
                predict_number = np.random.randint(x, y)
                count += 1
            elif number < predict_number: # reducing the right border of the interval
                y = predict_number
                predict_number = np.random.randint(x, y)
                count += 1
    return count

def score_game(random_predict) -> int:
    """For how many attempts on average for 1000 approaches does our algorithm guess

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    #np.random.seed(1)  # fixed conditions for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # made a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average for:{score} tries")
    return score


if __name__ == "__main__":
    score_game(random_predict)
