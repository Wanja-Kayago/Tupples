**TUPLE OPERATIONS IN PYTHON:**

- This script demonstrates various operations you can perform with tuples in Python.

**CODE EXAMPLE:**

- Cars = ('Ford', 'Ferrari', 'BMW', 'Audi', 'Bentley', 'Chevrolet', 'Porche', 'Cadillac', 'Porche')

**FINDING A SPECIFIC ELEMENT IN A TUPLE:**
- print(Cars.index('BMW'))  # Output: Index of 'BMW'
- print(Cars[1:3])          # Output: Slice from index 1 to 2
- print(Cars[-8:-6])        # Output: Slice using negative indices
- print(Cars[1:])           # Output: Elements from index 1 onwards

**NUMBER OF TIMES A CERTAIN ELEMENT HAS APPEARED IN THE TUPLE:**
- print(Cars.count('Porche'))  # Output: 2

**THE LENGTH OF THE TUPLE:**
- print(len(Cars))  # Output: 9

**TUPLE SORTED IN ASCENDING ORDER:**
- print(sorted(Cars))  

**THE MINIMUM AND MAXIMUM ELEMENTS IN THE TUPLE:**
- print(min(Cars))  # Output: 'Audi'
- print(max(Cars))  # Output: 'Porche'

**CONVERT AN ITERABLE OBJECTS INTO A RUPLE:**
- Brands = list(Cars)
- print(Brands)  # Output: Converted tuple to list
- Cars = tuple(Brands)
- print(Cars)    # Output: Converted list back to tuple

**JOINING TUPLES:**
- Brands = ('Toyota', 'Honda', 'Nissan')
- Cars += Brands
- print(Cars)  # Output: Concatenated tuple

**COMPARING TUPLES:**
- print(Brands < Cars)  # Output: Boolean comparison

**ADD AND DELETE AN ITEM IN A TUPLE:**
- tupletolist = list(Cars)
- print(tupletolist)           # Output: Tuple converted to list
- print(tupletolist.pop())     # Output: Remove last element
- tupletolist.append('Prado')  # Add 'Prado'
- print(tupletolist)           # Output: Updated list
- tupletolist.remove('Honda')  # Remove 'Honda'
- print(tupletolist)           # Output: List after removal
