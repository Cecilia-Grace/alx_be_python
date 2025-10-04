class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def _validate_inputs(self, a, b):
        """validates that both inputs are numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Error: Input numeric values only")
    
    
    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b
        

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b
    

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b


    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero")
        return a / b