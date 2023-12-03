class Monkey(object):
    def __init__(self, name, starting_items, operation, test_mod, targets):
        self.items = starting_items[:]
        self.name = name
        self.operation = operation
        self.test_mod = test_mod
        self.if_true = targets[0]
        self.if_false = targets[1]
        self.inspected = 0
