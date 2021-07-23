#!/usr/bin/python3
"""Define canUnlockAll funtion"""
from collections import namedtuple


def canUnlockAll(boxes):
    """\
    Return True or False depending if all box can be unlock
    Params:
    - boxes (list): List of list of positive integer numbers.
    """
    n_boxes = len(boxes)
    if n_boxes == 1:
        return True

    Box = namedtuple('Box', ['keys', 'unlock', 'evaluated'])
    tuple_boxes = [Box(b, False, False) for b in boxes]
    tuple_boxes[0] = tuple_boxes[0]._replace(unlock=True)

    for n in range(len(boxes)):
        current_box = []
        idx = 0

        for box in tuple_boxes:
            if box.unlock and not box.evaluated:
                current_box = box
                break
            idx += 1

        if not current_box or len(current_box) > n_boxes:
            return False

        for key in current_box.keys:
            if key >= n_boxes:
                return False
            tuple_boxes[key] = tuple_boxes[key]._replace(unlock=True)

        if all(box.unlock for box in tuple_boxes):
            return True

        tuple_boxes[idx] = current_box._replace(evaluated=True)

    return False
