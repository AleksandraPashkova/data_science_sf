""" The game 'Guess the number'
The computer makes a number from 1 to 100
and guesses this number itself

"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Guessing a number. This algorithm takes into accoun information
    about whether a random number is more or less a hidden number.

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: count of attempts
        
    """
    count = 0    # atempt counter
    
    # set the boundaries of the range in which guess the number
    left_border = 1
    right_border = 101
    
    while True:
        count += 1
        # expected number
        predict_number = np.random.randint(left_border, right_border)  
        
        if predict_number == number:
            break  # exit the cycle if guessed right
        
        # change the right border of the range 
        # if the expected number is more than the hidden number
        elif predict_number > number:
            right_border = predict_number + 1
            
        # change the left border of the range 
        # if the expected number is less than the hidden number  
        else:
            left_border = predict_number - 1
    return count


def score_game(random_predict) -> int:
    """The average number of attempts per 1000 appoaches
    for which the algorithm guesses

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
        
    """
    count_ls = []
    
    # make a list of numbers
    np.random.seed(1)  
    random_array = np.random.randint(1, 101, size=(1000))  

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number in a average:{score} attempts")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
