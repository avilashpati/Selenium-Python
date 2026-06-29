

def read_properties_values(file_path):
    properties = {}
    with open(file_path,"r") as lines:
        for line in lines:
            line = line.strip()

            if not line or line.startswith("["):
                continue

            key, value = line.split("=",1)
            properties[key.strip()] = value.strip()

    return properties
