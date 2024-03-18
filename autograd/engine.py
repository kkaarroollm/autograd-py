class Value:
    def __init__(self, data, _children=(), _operation=""):
        self.data = data
        self._prev = set(_children)
        self._operation = _operation

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), "*")

    def __sub__(self, other):
        return Value(self.data - other.data, (self, other), "-")


a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
d = a * b + c
print(d._prev)
print(d._prev.pop()._operation)

