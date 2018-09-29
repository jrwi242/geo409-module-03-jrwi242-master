# Python 3
# -----Find Arches by elevaton -----#
# by joyrwGIS for GEO 409. Uky
# Fall 2018
# ------ ------#

# Import site package for ArcGIS
import arcpy

# Set ArcGIS evironment
arcpy.env.workspace = r"C:\GIS\geology.gdb"
arcpy.env.overwriteOutput = True

# Assign variables
input_layer = "us_arches"
output_path = r"C:\GIS"

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
whereClause = "state_alpha"+"base_elevation_ft >= " + str(elevationNumber) 

# Use the TableToTable arcpy function extract by SQL query
arcpy.TableToTable_conversion (input_layer, output_path, "arches_by_elev.csv", whereClause)