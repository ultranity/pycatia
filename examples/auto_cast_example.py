#!/usr/bin/env python3
"""
Example script demonstrating how to use the cast() method to automatically cast AnyObject instances
to their specific types based on COM type information.
"""

from pycatia import catia
from pycatia.system_interfaces.any_object import AnyObject

# Connect to CATIA
caa = catia()
print(f"Connected to CATIA: {caa}")

# Get the active document
doc = caa.active_document
print(f"Active document: {doc}, {doc.com_type}")

part = doc.Part

# Get the Parameters collection
parameters = part
print(f"Parameters collection: {parameters}")

# Create a new parameter
length_param = parameters.create_real("Length", 100.0)
print(f"Created parameter: {length_param}")

param_as_any = AnyObject.new(length_param.com_object)
print(f"load com_object into AnyObject: {param_as_any}")

# Get the parameter as an AnyObject
param_as_any = AnyObject(length_param.com_object)
print(f"Parameter as AnyObject: {param_as_any}")
print(f"Parameter COM type: {param_as_any.com_type}")

# Cast the AnyObject back to its specific type
cast_param = param_as_any.cast()
print(f"Cast parameter: {cast_param}")
print(f"Cast parameter type: {type(cast_param).__name__}")

# Verify that we can access specific methods of the cast object
print(f"Parameter value: {cast_param.value}")

# Try with a different type of object
relations = doc.relations
print(f"Relations collection: {relations}")

# Get the Relations as an AnyObject
relations_as_any = AnyObject(relations.com_object)
print(f"Relations as AnyObject: {relations_as_any}")
print(f"Relations COM type: {relations_as_any.com_type}")

# Cast the AnyObject back to its specific type
cast_relations = relations_as_any.cast()
print(f"Cast relations: {cast_relations}")
print(f"Cast relations type: {type(cast_relations).__name__}")

print("\nAuto-casting demonstration completed successfully!")
