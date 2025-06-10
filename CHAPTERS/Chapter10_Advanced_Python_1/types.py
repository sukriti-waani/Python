from typing import List, Tuple, Dict, Union

n : int = 5

name: str = "sukriti"

def sum(a: int, b: int) -> int:
  return a + b

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and integer
person: Tuple[str, int] = ("Karan", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Math": 90, "Science": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid
