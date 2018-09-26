# Lab 03: Basic Python data structures and conditional execution

This two-part lab will quiz your ability to recognize/solve programming errors and build geoprocessing scripts.

## Table of Contents

<!-- TOC -->

- [Lab 03: Basic Python data structures and conditional execution](#lab-03-basic-python-data-structures-and-conditional-execution)
    - [Table of Contents](#table-of-contents)
    - [Part I: Quiz (4 pts)](#part-i-quiz-4-pts)
        - [Problem 1](#problem-1)
        - [Problem 2](#problem-2)
    - [Part II: Arches of the US report (6 pts)](#part-ii-arches-of-the-us-report-6-pts)
    - [Submission](#submission)

<!-- /TOC -->

## Part I: Quiz (4 pts)

Copy the below code to a new Python file called "quiz-03.py" in this lab folder. Find and remove the errors in the below problems.

### Problem 1
```python
# Problem 1: "variable names and operators"
# Print the output of 7 multipled by 56
0neNumber = 7
TwoNumber = 56
print("7 multiplied by 56 is:')
print(0neNumber x TwoNumber)
```

### Problem 2
```python
# Problem 2 "conditional execution and comparison"
# This should run for any number entered.
x = input("What is your height in feet: "))
if x = 1:
    print(\"For real?\")
else:
    y = (250/x)*100 
    print("You are "  y  "% the height of POT!")

```

## Part II: Arches of the US report (6 pts)

The data for this section is located in the lab folder and called, *geology.gdb". It contains a single layer for named arches in the US. Consider the following Python code:

```python
# Python 3
# ----- Find Arches by elevation ----- #
# by TastyFreeze for GEO 409, UKy
# Fall, 2018
# ----- ------------------------ ----- #

# Import site package for ArcGIS
import arcpy

# Set ArcGIS evironment
arcpy.env.workspace = r"Z:\BoydsGIS\data\geology.gdb"
arcpy.env.overwriteOutput = True

# Assign variables
input_layer = "us_arches"
output_path = r"Z:\BoydsGIS\data"

# Prompt for user input
print("This program returns all arches as .csv file at or above the minimum elevation.")
elevation = input("Enter minimum elevation: ")

# Try converting to integer. Exit if not integer
try:
    elevationNumber = int(elevation)
except:
    print("Whoops! Try using a number.")
    exit()

# Build the where clause, aka the SQL statement to select features
whereClause = "base_elevation_ft >= " + str(elevationNumber)

# Use the TableToTable arcpy function extract by SQL query
arcpy.TableToTable_conversion (input_layer, output_path, "arches_by_elev.csv", whereClause)
```

Add two additional `input()` functions that
>1. select by state and elevation. How would a user get all arches in Kentucky with an elevation over 1,000 ft? A user should be able to select any state and any elevation.
>2. allow the user to save it an arbitrary CSV file, e.g.,*ky_arches_over1000ft.csv*.

Save this as a Python file called "extract_us_arches.py" and place in this lab folder.

## Submission

Paste URL link to this repo within the Canvas Assignment 3 by the due date. e.g., *https://github.com/UKy-GIS/geo409-module-03-username*.

