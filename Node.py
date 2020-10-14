# Linked-list Node
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new):
        self.next = new

    def get_previous(self):
        return self.previous

    def set_previous(self, new):
        self.previous = new
