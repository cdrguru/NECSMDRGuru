import pandas as pd

class QualityAssuranceAgent:
    def __init__(self, structured_data, field_descriptions):
        """
        Initializes the Quality Assurance Agent with structured NEC SMDR data and field descriptions.

        :param structured_data: DataFrame, the structured NEC SMDR data to be validated.
        :param field_descriptions: dict, the descriptions of the NEC SMDR data fields.
        """
        self.structured_data = structured_data
        self.field_descriptions = field_descriptions

    def perform_quality_checks(self):
        """
        Performs quality checks on the structured NEC SMDR data based on field specifications.

        :return: bool, True if the data passes the quality checks, False otherwise.
        """
        if self.structured_data.isnull().any().any():
            print("Quality check failed: Null values found in the structured data.")
            return False

        # Perform field-specific validations
        for record_type, fields in self.field_descriptions.items():
            for field in fields:
                if not self._validate_field_data(field):
                    print(f"Quality check failed for field: {field['Name & Description']}")
                    return False

        print("Quality checks passed. The structured NEC SMDR data is valid.")
        return True

    def _validate_field_data(self, field):
        """
        Validates data for a specific NEC SMDR field based on its specifications.

        :param field: dict, specifications for a single field in the NEC SMDR data.
        :return: bool, True if data is valid for the field, False otherwise.
        """
        field_name = field["Name & Description"]
        field_data = self.structured_data[field_name]

        # Check if the field exists in the structured data
        if field_name not in self.structured_data.columns:
            print(f"Quality check failed: Field '{field_name}' not found in the structured data.")
            return False

        # Validate based on field length
        if "Length of Data" in field:
            length_info = field["Length of Data"]
            if "Variable" in length_info:
                min_length, max_length = map(int, length_info.split("Variable")[1].split("to"))
                if not all(field_data.astype(str).str.len().between(min_length, max_length)):
                    print(f"Quality check failed: Field '{field_name}' has invalid length.")
                    return False
            else:
                expected_length = int(length_info.split("characters")[0])
                if not all(field_data.astype(str).str.len() == expected_length):
                    print(f"Quality check failed: Field '{field_name}' has invalid length.")
                    return False

        # Validate based on specific field conditions
        if field_name == "Account Code":
            if not all(field_data.astype(str).str.match(r'^\d{1,24}$')):
                print("Quality check failed: Invalid 'Account Code' format.")
                return False
        elif field_name == "Condition Code":
            valid_condition_codes = ['0', '1', '2', '3', '4', '5', '6', '7']
            if not all(field_data.isin(valid_condition_codes)):
                print("Quality check failed: Invalid 'Condition Code' values.")
                return False
        elif field_name == "Multi-Area ID (MA-ID)":
            if not all(field_data.astype(str).str.match(r'^\d{4}$')):
                print("Quality check failed: Invalid 'Multi-Area ID (MA-ID)' format.")
                return False

        return True

# Example usage:
# structured_data = pd.read_csv('structured_nec_smdr_data.csv')
# field_descriptions = {...}  # Load this from NEC_SMDR_Field_Descriptions.json
# qa_agent = QualityAssuranceAgent(structured_data, field_descriptions)
# is_data_valid = qa_agent.perform_quality_checks()