def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is unlocked
    keys = [0]  # Start with the first box's keys

    while keys:
        current_box = keys.pop()  # Get the last box we can open
        for key in boxes[current_box]:  # Check the keys in the current box
            if key < n and not unlocked[key]:  # If the key is valid and the box is locked
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add the key to our list to explore later

    return all(unlocked)  # Return True if all boxes are unlocked

# Example usage
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

