# example class


class Example:
    """
    Example class

    Attributes:
        name: str
        age: int
    """

    def __init__(self):
        self.name: str = "example"
        self.age: int = 12

    def print_name(self):
        """
        print the name of the class
        """
        print(self.name)

    def print_age(self):
        print(self.age)

    def print_age_n_times(self, n: int):
        for _ in range(n):
            print(self.age)