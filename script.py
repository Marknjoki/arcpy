import arcpy

# Set the workspace to the directory containing your data
arcpy.env.workspace= r"C:\Users\Dell\Downloads\PROGRAMMING FOR GIS\KAJIADO\kajiado_roads.shp"

#input feature class
roads_fc="kajiado_roads.shp"
 
# Project the roads to a projected coordinate system
projected_fc = r"C:\Users\Dell\Downloads\PROGRAMMING FOR GIS\KAJIADO\projected_roads.shp"
arcpy.management.Project(roads_fc, projected_fc, 21097)

#creating output table for length by surface type
output_surf_table = "SurfaceLengthSummary.dbf"
 
# Output table for length by road condition
output_cond_table = "ConditionLengthSummary.dbf"

# Output table for length by road class
output_class_table = "ClassLengthSummary.dbf"

#add field of lenght in km as an attribute to the data
length_field = "Length_km"
arcpy.AddField_management(roads_fc,length_field, "DOUBLE")

#using field calculator tool to calculate length field
arcpy.CalculateField_management(roads_fc,length_field, "!Shape.length@Kilometers!", "PYTHON")


# Using the Summary Statistics tool to calculate length by surface type
arcpy.analysis.Statistics(
in_table=projected_fc,
out_table=output_surf_table,
statistics_fields=[["Length_km", "SUM"]],
case_field="surftype"
 )

# Using the Summary Statistics tool to calculate length by road condition
arcpy.analysis.Statistics(
in_table=projected_fc,
out_table=output_cond_table,
statistics_fields=[["Length_km", "SUM"]],
case_field="surfcond"
)

# Using the Summary Statistics tool to calculate length by road class
arcpy.analysis.Statistics(
in_table=projected_fc,
out_table=output_class_table,
statistics_fields=[["Length_km", "SUM"]],
case_field="roadclass"
 )
 
# Print a summary message
print("Summary tables created successfully .")
