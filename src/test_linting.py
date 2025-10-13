# Databricks notebook source
# MAGIC %md
# MAGIC # Test Notebook - Linting Issues
# MAGIC
# MAGIC This notebook intentionally contains linting issues to test Black and Flake8.
# MAGIC These issues should be detected by the PR validation pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Import Issues

# COMMAND ----------

# BLACK ISSUE: Imports should be sorted and grouped
import sys
import pandas as pd
from pyspark.sql.functions import col
import os
from pyspark.sql import SparkSession
import numpy as np
from datetime import datetime

# FLAKE8 ISSUE: Unused imports
from typing import Dict, List, Optional, Tuple  # F401: imported but unused
import json  # F401: imported but unused

# COMMAND ----------

# MAGIC %md
# MAGIC ## Formatting Issues

# COMMAND ----------

# BLACK ISSUE: Line too long (should be max 120 characters)
very_long_variable_name_that_exceeds_the_maximum_line_length = "This is a very long string that definitely exceeds the 120 character limit set by Black formatter and should be flagged"

# BLACK ISSUE: Inconsistent spacing
x=1+2  # Should have spaces around operators
y = 3*4  # Should have spaces
z=5 /6  # Inconsistent spacing

# BLACK ISSUE: Dictionary formatting
messy_dict = {'key1': 'value1','key2': 'value2','key3': 'value3'}

# COMMAND ----------

# MAGIC %md
# MAGIC ## Whitespace Issues

# COMMAND ----------


# BLACK ISSUE: Too many blank lines above



def function_with_bad_spacing():
    """Function with whitespace issues."""
    pass


# BLACK ISSUE: No blank line before function


def another_function():
    pass

# COMMAND ----------

# MAGIC %md
# MAGIC ## Indentation Issues

# COMMAND ----------

# BLACK/FLAKE8 ISSUE: Inconsistent indentation
def bad_indentation():
  """This function has 2-space indentation instead of 4."""
  x = 1
  if x == 1:
    print("Bad indentation")  # Should be 4 spaces per level
  return x

# COMMAND ----------

# MAGIC %md
# MAGIC ## String Formatting Issues

# COMMAND ----------

# BLACK ISSUE: Should use double quotes consistently
name = 'John Doe'
message = "Hello, World!"  # Mixed quote styles
greeting = f'Hello {name}'  # Should be double quotes

# BLACK ISSUE: String concatenation formatting
long_string = "This is a very long string " + \
              "that spans multiple lines " + \
              "with bad concatenation"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Function Definition Issues

# COMMAND ----------

# BLACK ISSUE: Function arguments not properly formatted
def badly_formatted_function(arg1,arg2,arg3="default",arg4=None):
    """Function with formatting issues."""
    return arg1+arg2

# BLACK ISSUE: Complex expression without proper line breaks
result = badly_formatted_function(arg1="value1",arg2="value2",arg3="value3",arg4="value4")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Code Quality Issues (Flake8)

# COMMAND ----------

# FLAKE8 ISSUE: F841 - Local variable assigned but never used
def unused_variable_function():
    """Function with unused variables."""
    unused_var = 42
    another_unused = "hello"
    result = 100
    return result

# FLAKE8 ISSUE: E501 - Line too long
this_is_an_extremely_long_variable_name = "This is a really long string that when combined with the variable name makes the line exceed 120 characters"

# FLAKE8 ISSUE: W503 - Line break before binary operator (deprecated but some configs still check)
total = (
    1 + 2 + 3
    + 4 + 5 + 6
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Comparison Issues

# COMMAND ----------

# FLAKE8 ISSUE: E712 - Comparison to True/False should be 'if cond:' or 'if not cond:'
is_valid = True
if is_valid == True:  # Should be: if is_valid:
    print("Valid")

if is_valid == False:  # Should be: if not is_valid:
    print("Invalid")

# FLAKE8 ISSUE: E711 - Comparison to None should be 'if cond is None:'
value = None
if value == None:  # Should be: if value is None:
    print("None value")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Trailing Whitespace and Blank Line Issues

# COMMAND ----------

# FLAKE8 ISSUE: W291 - Trailing whitespace
def function_with_trailing_spaces():  # Imagine trailing spaces here
    pass  # And here    

# FLAKE8 ISSUE: W293 - Blank line contains whitespace
# (The blank lines above should have no spaces)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lambda Expression Issues

# COMMAND ----------

# BLACK ISSUE: Lambda expression formatting
bad_lambda = lambda x,y: x+y  # Should have spaces
better_lambda = lambda x, y: x + y

# Nested lambdas (hard to read, Flake8 might complain)
complex_lambda = lambda x: (lambda y: x + y)

# COMMAND ----------

# MAGIC %md
# MAGIC ## List/Dict Comprehension Issues

# COMMAND ----------

# BLACK ISSUE: Comprehension formatting
bad_list = [x for x in range(10) if x%2==0]  # Missing spaces
bad_dict = {k:v for k,v in enumerate(range(5))}  # Missing spaces

# Better formatting
good_list = [x for x in range(10) if x % 2 == 0]
good_dict = {k: v for k, v in enumerate(range(5))}

# COMMAND ----------

# MAGIC %md
# MAGIC ## Complex Expression Issues

# COMMAND ----------

# BLACK/FLAKE8 ISSUE: Complex expression without proper formatting
complex_result = (100+200*300/400-500)+((1+2)*(3+4)/(5+6))-(7*8)+(9/10)

# FLAKE8 ISSUE: E501 - Line too long with complex expression
very_complex_calculation = (first_variable + second_variable * third_variable / fourth_variable - fifth_variable) + (sixth_variable * seventh_variable)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Missing Docstrings

# COMMAND ----------

# FLAKE8 ISSUE: D100/D103 - Missing docstrings (if pydocstyle is enabled)
def function_without_docstring(param1, param2):
    return param1 + param2

class ClassWithoutDocstring:
    def method_without_docstring(self):
        pass

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC This notebook should trigger the following linting issues:
# MAGIC
# MAGIC ### Black Issues:
# MAGIC - Line too long (>120 characters)
# MAGIC - Inconsistent spacing around operators
# MAGIC - Improper dict/list formatting
# MAGIC - Too many/too few blank lines
# MAGIC - Inconsistent quote usage
# MAGIC - Poor function argument formatting
# MAGIC
# MAGIC ### Flake8 Issues:
# MAGIC - F401: Unused imports
# MAGIC - F841: Unused variables
# MAGIC - E501: Line too long
# MAGIC - E712: Comparison to True/False
# MAGIC - E711: Comparison to None
# MAGIC - W291: Trailing whitespace
# MAGIC - W503: Line break before binary operator
# MAGIC
# MAGIC ✅ Use this to verify that your linting checks are working properly!
