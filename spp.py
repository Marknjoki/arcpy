import arcpy
import os

# Set the workspace to the directory containing your data
arcpy.env.workspace = r"C:\Users\Dell\Downloads\PROGRAMMING FOR GIS\kenyadata\KRBRoads.shp"

# Input feature class (roads data)
roads_fc = "KRBRoads.shp"

# Specify the area of interest
area_of_interest = "mombasa.shp"

# Create a feature layer for the roads
arcpy.MakeFeatureLayer_management(roads_fc, "roads_layer")

# Select roads within the area of interest
arcpy.SelectLayerByLocation_management("roads_layer", "WITHIN", area_of_interest)

# Create a new folder for the selected roads
output_folder = r"C:\Users\Dell\Downloads\PROGRAMMING FOR GIS\mombasa"
selected_roads_fc = "mombasa_roads.shp"
selected_roads_path = arcpy.CreateUniqueName(os.path.join(output_folder, selected_roads_fc))

# Copy the selected features to the new feature class
arcpy.CopyFeatures_management("roads_layer", selected_roads_path)

print("Selected roads successfull saved")
