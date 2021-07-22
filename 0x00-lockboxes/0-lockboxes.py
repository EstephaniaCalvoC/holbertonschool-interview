#!/usr/bin/python3
"""Define canUnlockAll funtion"""
from collections import deque


def canUnlockAll(boxes):
    """\
    Return True or False depending if all box can be unlock
    Params:
    - boxes (list): List of list of positive integer numbers.
    """
    n_boxes = len(boxes)
    if n_boxes == 1:
        return True

    lock_state = [1] + [0] * (n_boxes - 1)
    deque_boxes = [deque(b) for b in boxes]

    current_box = deque_boxes[0]

    max_jumps, jumps = (n_boxes, 0)

    while (current_box and jumps <= max_jumps):
        new_max_jumps = len(current_box) ** n_boxes
        max_jumps = new_max_jumps if max_jumps < new_max_jumps else max_jumps

        idx_next_box = current_box[0]
        current_box.rotate(-1)
        lock_state[idx_next_box] = 1

        if all(box for box in lock_state):
            return True

        current_box = deque_boxes[idx_next_box]
        jumps += 1

    return False
