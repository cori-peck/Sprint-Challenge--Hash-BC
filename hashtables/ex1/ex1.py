#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    results = []
    hash_table = {}

    for c in range(0, len(weights)):
        new = limit - weights[c]
        hash_table[weights[c]] = new

    for d in range(0, len(weights)):
        if limit - weights[d] in hash_table:
            results.insert(0, d)
    
    return results


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
