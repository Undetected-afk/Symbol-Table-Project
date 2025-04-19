# Symbol Table Project

## Overview

This Python program implements a **symbol table** using a hash table (Python's dictionary). It allows the user to declare variables with specific data types (int, float, str, bool) and assign values to them. The program validates the data types during declaration and updating, ensuring that the values assigned match the declared types.

Users can update the value of declared variables, and the program will print the symbol table before and after updates, providing visibility into the changes.

## Features

- Declare variables with types (`int`, `float`, `str`, `bool`).
- Update values of declared variables.
- Type validation during both declaration and update.
- Displays the symbol table before and after updates.
- Error handling for type mismatches and undeclared variables.

## Example Output

### Program Run:

=== Variable Declaration Phase === How many variables do you want to declare? 3

Enter variable declaration (format: name type value)

x int 5 Declared 'x'

Enter variable declaration (format: name type value)

pi float 3.14 Declared 'pi'

Enter variable declaration (format: name type value)

name str Alice Declared 'name'

Symbol Table after Declarations:

Variable Type Value
x int 5 pi float 3.14 name str Alice

=== Variable Update Phase === How many variables do you want to update? 2

Enter variable update (format: name new_value)

x 10 Updated 'x'

Enter variable update (format: name new_value)

pi 3.1416 Updated 'pi'

Symbol Table after Updates:

Variable Type Value
x int 10 pi float 3.1416 name str Alice


## Instructions

1. **Declare Variables**:  
   - When prompted, enter the number of variables to declare.
   - For each variable, provide the name, type, and value (e.g., `x int 5`).

2. **Update Variables**:  
   - After declaring variables, you can update them by entering the variable name and the new value (must match the original type).

3. **View Symbol Table**:  
   - The program will display the symbol table before and after updates, allowing you to see the changes.

## How to Run

Symbol-Table-Project
Run the Python program:

python symbol_table.py
