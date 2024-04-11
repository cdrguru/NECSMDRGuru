import pandas as pd

class DataStructuringAgent:
    def __init__(self, parsed_data, field_descriptions):
        """
        Initializes the Data Structuring Agent with parsed NEC SMDR data and field descriptions.

        :param parsed_data: DataFrame, the parsed NEC SMDR data to be structured for Power BI.
        :param field_descriptions: dict, descriptions of the fields for each NEC SMDR record type.
        """
        self.parsed_data = parsed_data
        self.field_descriptions = field_descriptions

    def structure_for_power_bi(self):
        """
        Structures the parsed NEC SMDR data into a format suitable for Power BI analysis.

        :return: DataFrame, data structured for Power BI.
        """
        # Standardize the structure by ensuring all columns from field_descriptions exist in the data
        standardized_data = self._standardize_structure(self.parsed_data)

        # Apply specific transformations or structuring needed for Power BI
        for column in standardized_data.columns:
            if column in ['Start Time', 'End Time']:
                standardized_data[column] = pd.to_datetime(standardized_data[column], errors='coerce')
            elif column == 'Duration':
                standardized_data[column] = pd.to_timedelta(standardized_data[column], unit='s')
            elif column in ['Calling Number', 'Called Number', 'Account Code']:
                standardized_data[column] = standardized_data[column].astype(str)
            elif column in ['Route Number', 'Trunk Number', 'Attendant Console Number']:
                standardized_data[column] = pd.to_numeric(standardized_data[column], errors='coerce')

        # Rename columns to more user-friendly names for Power BI
        column_mapping = {
            'Start Time': 'Call Start Time',
            'End Time': 'Call End Time',
            'Calling Number': 'Caller',
            'Called Number': 'Callee',
            'Account Code': 'Account',
            'Condition Code': 'Call Condition',
            'Route Number': 'Route',
            'Trunk Number': 'Trunk',
            'Attendant Console Number': 'Attendant Console'
        }
        standardized_data.rename(columns=column_mapping, inplace=True)

        return standardized_data

    def _standardize_structure(self, data):
        """
        Ensures that the data structure is consistent and standardized for all NEC SMDR record types.

        :param data: DataFrame, the NEC SMDR data to be standardized.
        :return: DataFrame, standardized NEC SMDR data.
        """
        # Identify all columns from field_descriptions and ensure they exist in the data
        all_columns = set().union(*(d.values() for d in self.field_descriptions.values()))
        missing_columns = all_columns - set(data.columns)
        for column in missing_columns:
            data[column] = None
        return data

# Example usage:
# parsed_data = pd.read_csv('parsed_nec_smdr_data.csv')
# field_descriptions = {...}  # Load this from NEC_SMDR_Field_Descriptions.json
# structuring_agent = DataStructuringAgent(parsed_data, field_descriptions)
# power_bi_ready_data = structuring_agent.structure_for_power_bi()