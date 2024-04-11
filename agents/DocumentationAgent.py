class DocumentationAgent:
    def __init__(self, tool_name, field_descriptions):
        """
        Initializes the Documentation Agent with the tool's name and field descriptions of the NEC SMDR data.

        :param tool_name: str, the name of the tool.
        :param field_descriptions: dict, the descriptions of the NEC SMDR data fields being processed by the tool.
        """
        self.tool_name = tool_name
        self.field_descriptions = field_descriptions

    def create_documentation(self):
        """
        Creates the documentation for the tool, incorporating NEC SMDR field descriptions.

        :return: str, the documentation text.
        """
        documentation = f"Documentation for {self.tool_name}\n"
        documentation += "---------------------------------\n"
        documentation += "Overview:\n"
        documentation += f"This tool is designed to process NEC SMDR data, specifically by parsing, structuring, and preparing it for Power BI analysis. The data is processed based on the NEC SMDR fixed-width format specifications.\n\n"
        
        documentation += "NEC SMDR Field Descriptions:\n"
        for record_type, fields in self.field_descriptions.items():
            documentation += f"\nRecord Type: {record_type}\n"
            for field in fields:
                documentation += f"- {field['Name & Description']}: {field.get('Comments', 'No description available')}\n"

        documentation += "\nUsage Instructions:\n"
        documentation += "1. Ensure your raw NEC SMDR data files are available in the correct fixed-width format.\n"
        documentation += "2. Configure the tool with the appropriate NEC SMDR field descriptions for each record type.\n"
        documentation += "3. Run the tool to parse and structure the NEC SMDR data according to the provided field descriptions.\n"
        documentation += "4. Export the structured data to Power BI for further analysis and reporting.\n\n"

        documentation += "Data Interpretation in Power BI:\n"
        documentation += "The structured NEC SMDR data can be used in Power BI to create insightful reports and dashboards. When interpreting the data, consider the specific meanings and implications of each field as described in the NEC SMDR specifications.\n"
        documentation += "- Ensure data types are correctly recognized in Power BI based on the NEC SMDR field definitions.\n"
        documentation += "- Use filters and groupings based on relevant NEC SMDR fields like call types, routes, trunks, and condition codes to analyze call patterns.\n"
        documentation += "- Pay attention to call durations, start and end times, and other key metrics for comprehensive analysis of the NEC SMDR data.\n"

        return documentation

    def create_user_instructions(self):
        """
        Creates user instructions for the tool, focusing on the NEC SMDR data context.

        :return: str, the user instruction text.
        """
        instructions = f"User Instructions for {self.tool_name}\n"
        instructions += "---------------------------------\n"
        instructions += "Step 1: Ensure your NEC SMDR data files are formatted according to the NEC SMDR fixed-width specifications.\n"
        instructions += "Step 2: Provide the tool with the necessary NEC SMDR field descriptions for each record type.\n"
        instructions += "Step 3: Run the tool to parse and structure the NEC SMDR data based on the provided field descriptions.\n"
        instructions += "Step 4: Import the structured NEC SMDR data into Power BI and utilize it for creating reports and dashboards.\n"
        instructions += "For more detailed usage and NEC SMDR field explanations, refer to the full documentation."

        return instructions

# Example usage:
# field_descriptions = {...}  # This would be loaded from NEC_SMDR_Field_Descriptions.json
# doc_agent = DocumentationAgent(tool_name="NEC SMDR Data Processor", field_descriptions=field_descriptions)
# documentation = doc_agent.create_documentation()
# user_instructions = doc_agent.create_user_instructions()

# The generated documentation and instructions can then be saved to a file, printed, or displayed in an application.
