#!/usr/bin/python3

def canUnlockAll(boxes):
    unlock_boxes = set([0])

    keyes = boxes[0].copy()

    while keyes:
        key = keyes.pop()
        if key not in unlock_boxes and key < len(boxes):
            unlock_boxes.add(key)
            keyes.extend(boxes[key])

    return len(unlock_boxes) == len(boxes)
