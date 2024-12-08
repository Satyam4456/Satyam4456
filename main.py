from fpdf import FPDF

# Content to be added in the PDF
content = """
1. Introduction to Python Modules
- What is a module?
  - A module is a file containing Python definitions and statements, usually saved with a .py extension.
  - A module can contain functions, classes, variables, and runnable code.

- Why use modules?
  - To organize and reuse code.
  - To separate concerns and keep code clean.

2. Importing Modules
- The import statement is used to bring modules into the current namespace.
Example:
import math  # Imports the math module
print(math.sqrt(16))  # Using a function from the math module

- You can also import specific items from a module using from ... import:
from math import sqrt
print(sqrt(16))

3. Python's Search Path (sys.path)
- When you use the import statement, Python needs to locate the module.
- Python looks in specific locations to find modules:
  - The current directory.
  - The standard library directories.
  - The directories listed in the PYTHONPATH environment variable.
  - The directories listed in sys.path.

- sys.path: This is a list in Python that contains the directories Python searches for modules. You can view it by:
import sys
print(sys.path)

- Adding directories to sys.path:
  - You can add custom directories to sys.path to make Python search those locations for modules.
import sys
sys.path.append('/path/to/directory')  # Adds a new directory to sys.path

4. Importing from Non-Standard Locations
- If your module is not located in the default Python search path, you can manually add its path to sys.path to enable importing.
Example:
import sys
sys.path.append('/path/to/my_directory')  # Add the directory to sys.path
import my_module  # Now Python can import from this directory

5. Working with Packages
- A package is a directory containing Python modules and an __init__.py file (which marks the directory as a package).
- To import from a package:
my_package/
    __init__.py
    module1.py

import my_package.module1
my_package.module1.some_function()

6. Understanding __init__.py
- __init__.py:
  - Used to mark a directory as a Python package.
  - It can be empty or contain initialization code.
  - In Python 3.3+, it's optional to use __init__.py, but it's still good practice to use it for backward compatibility.

7. Using importlib for Dynamic Imports
- For more advanced use cases, you can dynamically import modules using the importlib module.
import importlib
my_module = importlib.import_module('my_module')  # Dynamically import a module
my_module.some_function()

8. Practical Example
Here’s an example of how this all works together:

Directory Structure:
project/
    main_script.py
    utils/
        __init__.py
        helper.py

Code in helper.py:
def greet():
    print("Hello from helper!")

Code in main_script.py:
import sys
sys.path.append('/path/to/project/utils')  # Add 'utils' folder to sys.path
import helper  # Import the 'helper' module from the 'utils' directory
helper.greet()

9. Best Practices
- Keep directory structure organized: Place related modules in packages for better code management.
- Use relative imports within packages: If you're working within a package, it's better to use relative imports to import modules.
from .module1 import some_function  # Relative import within the same package

- Avoid modifying sys.path unnecessarily in production code, as it can make the code harder to maintain.

Summary
- Python uses the import statement to bring modules into the current program.
- sys.path defines where Python looks for modules, and you can modify it to include custom directories.
- Packages are directories with modules and an __init__.py file that help organize related modules.
- Using importlib, you can dynamically import modules if needed.
"""

# Create the PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "Module Importing and Path Management in Python", ln=True, align='C')
pdf.ln(10)

# Add content to the PDF
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, content)

# Output the PDF file
pdf_output_path = "Module_Importing_and_Path_Management.pdf"
pdf.output(pdf_output_path)

print(f"PDF has been created: {pdf_output_path}")