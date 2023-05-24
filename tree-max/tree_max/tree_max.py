class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def find_maximum_value(self):
        if self is None:
            return None

        maximum = self.value

        if self.left is not None:
            left_max = self.left.find_maximum_value()
            maximum = max(maximum, left_max)

        if self.right is not None:
            right_max = self.right.find_maximum_value()
            maximum = max(maximum, right_max)

        return maximum
