import pandas as pd

class DataCleaningAgent:
    def __init__(self, data):
        """
        Initializes the Data Cleaning Agent with the NEC SMDR data to be cleaned and preprocessed.

        :param data: DataFrame, the NEC SMDR data to be cleaned and preprocessed.
        """
        self.data = data

    def clean_data(self):
        """
        Cleans the NEC SMDR data by removing irrelevant or corrupt records and handling missing values.

        :return: DataFrame, cleaned NEC SMDR data.
        """
        # Remove records with missing essential fields (e.g., call start time, call duration)
        essential_fields = ['Start Time', 'Duration']
        cleaned_data = self.data.dropna(subset=essential_fields)

        # Remove duplicate records based on unique identifiers (e.g., call ID, start time, and duration)
        cleaned_data = cleaned_data.drop_duplicates(subset=['Call ID', 'Start Time', 'Duration'])

        # Filter out records with invalid or inconsistent data (e.g., negative call duration)
        cleaned_data = cleaned_data[cleaned_data['Duration'] >= 0]

        return cleaned_data

    def preprocess_data(self, cleaned_data):
        """
        Preprocesses the cleaned NEC SMDR data to ensure consistency and normalize data formats.

        :param cleaned_data: DataFrame, NEC SMDR data that has been cleaned.
        :return: DataFrame, preprocessed NEC SMDR data.
        """
        # Convert date and time fields to a consistent format (e.g., ISO 8601)
        cleaned_data['Start Time'] = pd.to_datetime(cleaned_data['Start Time'], format='%Y%m%d%H%M%S')
        cleaned_data['End Time'] = pd.to_datetime(cleaned_data['End Time'], format='%Y%m%d%H%M%S')

        # Normalize text fields (e.g., convert to lowercase, remove leading/trailing whitespace)
        text_fields = ['Calling Number', 'Called Number', 'Account Code']
        for field in text_fields:
            cleaned_data[field] = cleaned_data[field].str.lower().str.strip()

        # Convert call duration from seconds to a more readable format (e.g., HH:MM:SS)
        cleaned_data['Duration'] = pd.to_timedelta(cleaned_data['Duration'], unit='s')

        # Map condition codes to their corresponding descriptions
        condition_code_mapping = {
            '0': 'No Condition',
            '1': 'Call Transferred',
            '2': 'Billing Continued',
            '3': 'Call Transferred & Billing Continued',
            '4': 'Call Transferred to Last Called Party'
        }
        cleaned_data['Condition Code'] = cleaned_data['Condition Code'].map(condition_code_mapping)

        return cleaned_data

# Example usage:
# smdr_data = pd.read_csv('nec_smdr_data.csv')
# cleaning_agent = DataCleaningAgent(smdr_data)
# cleaned_data = cleaning_agent.clean_data()
# preprocessed_data = cleaning_agent.preprocess_data(cleaned_data)
