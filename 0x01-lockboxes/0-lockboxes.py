#!/usr/bin/python3

def canUnlockAll(boxes):
    unlock_boxes = set([0])

    keyes = boxes[1].copy()

    while keyes:
        key = keyes.pop()
        if key not in unlock_boxes and key < len(boxes):
            unlock_boxes.add(key)
            key.extend(boxes[key])

    return len(unlock_boxes) == len(boxes)
