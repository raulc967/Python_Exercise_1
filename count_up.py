def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    answer = []
    while start <= stop:
        answer.append(start)
        start = start + 1
    return answer
    # YOUR CODE HERE


print(count_up(5, 7))        
