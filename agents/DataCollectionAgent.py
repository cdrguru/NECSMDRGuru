import os
import pandas as pd

def parse_fixed_width_smdr(line, field_descriptions):
    """
    Parses a single line of NEC SMDR data based on fixed-width field descriptions.

    :param line: str, a single line from an NEC SMDR data file.
    :param field_descriptions: list, a list of dictionaries containing field width information for the specific record type.
    :return: dict, parsed data fields.
    """
    parsed_data = {}
    for field in field_descriptions:
        start_pos = int(field["Character"].split('~')[0])
        end_pos = int(field["Character"].split('~')[-1]) + 1
        parsed_data[field["Name & Description"]] = line[start_pos:end_pos].strip()
    return parsed_data

def data_collection_agent(smdr_directory, field_descriptions, file_format='txt'):
    """
    Collects raw NEC SMDR files from a specified directory and validates their format and integrity.

    :param smdr_directory: str, the path to the directory containing NEC SMDR files.
    :param field_descriptions: dict, field descriptions for each NEC SMDR record type (e.g., KA, KE).
    :param file_format: str, the expected format of the NEC SMDR files (default is 'txt').
    :return: list of dicts, each dict contains the content of a valid NEC SMDR record.
    """
    smdr_data = []
    for filename in os.listdir(smdr_directory):
        if filename.endswith(file_format):
            file_path = os.path.join(smdr_directory, filename)
            with open(file_path, 'r') as smdr_file:
                for line in smdr_file:
                    record_type = line[3:5]  # Extract the NEC SMDR record type (e.g., KA, KE)
                    if record_type in field_descriptions:
                        parsed_line = parse_fixed_width_smdr(line, field_descriptions[record_type])
                        smdr_data.append(parsed_line)
                    else:
                        print(f"Unknown record type {record_type} in file {filename}")
    return smdr_data

# Load field descriptions from the JSON file (assuming it's loaded into a variable `field_descriptions_json`)
# field_descriptions_json = ...

# Example usage:
# smdr_directory = 'path/to/nec/smdr/files'
# collected_data = data_collection_agent(smdr_directory, field_descriptions_json)