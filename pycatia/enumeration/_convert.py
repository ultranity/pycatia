import enumeration_types


def convert_to_camel_case(snake_str):
    """Convert snake_case to CamelCase"""
    components = snake_str.split("_")
    return "".join(x.title() for x in components)


with open("enum_items.py", "w") as out_file:
    # Write imports and header
    out_file.write("# Generated EnumItem classes\n\n")

    # Process each variable that might be an enum tuple
    for key, values in enumeration_types.__dict__.items():
        if key.startswith("__") or not isinstance(values, tuple):
            continue

        # Check if this looks like an enum tuple
        if all(isinstance(item, str) for item in values):
            # Convert snake_case to CamelCase for class name
            class_name = convert_to_camel_case(key)

            # Write the class definition
            out_file.write(f"class {class_name}(EnumItem):\n")

            # Add each enum value with its index
            for i, value in enumerate(values):
                out_file.write(f"    {value} = {i}\n")

            # Add a newline after each class
            out_file.write("\n")
for key, values in enumeration_types.__dict__.items():
    if isinstance(values, tuple):
        print(key)
