#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """-
    Args:
        boxes: list of boxes
    Return:
        true if no lock box, else false"""
    unlock_boxes = set([0])

    keyes = boxes[0].copy()

    while keyes:
        key = keyes.pop()
        if key not in unlock_boxes and key < len(boxes):
            unlock_boxes.add(key)
            keyes.extend(boxes[key])

    return len(unlock_boxes) == len(boxes)
