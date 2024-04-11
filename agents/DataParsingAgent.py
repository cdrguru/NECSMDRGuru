import json
from datetime import datetime


def parse_date_time(date_time_str):
    year = "20" + date_time_str[:2]
    month = date_time_str[2:4]
    day = date_time_str[4:6]
    hour = date_time_str[6:8]
    minute = date_time_str[8:10]
    second = date_time_str[10:12]
    millisecond = date_time_str[12:15]
    return f"{year}-{month}-{day} {hour}:{minute}:{second}.{millisecond}"


def find_record_start(record):
    for i in range(len(record)):
        if record[i] == "K":
            return i
    return -1


def parse_smdr_record(record):
    start_pos = find_record_start(record)
    if start_pos == -1:
        return {"Error": "Invalid record format"}

    record_type = record[start_pos:start_pos+2]
    parsed_record = {"Record Type": record_type}

    # Extracting common fields across KK, KM, KL, KE, KH, KJ, and KA records
    if record_type in ["KK", "KM", "KL", "KE", "KH", "KJ", "KA"]:
        parsed_record["Call Start Date and Time"] = parse_date_time(
            record[start_pos+30:start_pos+45])
        parsed_record["Call End Date and Time"] = parse_date_time(
            record[start_pos+45:start_pos+60])

        # Additional parsing based on record type
        if record_type == "KK":
            parsed_record["Description"] = "Outgoing Flexible Format"
            parsed_record["Calling Party Number"] = {
                "Kind of Data": record[start_pos+0],
                "Length of Data": record[start_pos+3:start_pos+5],
                "Fusion Point Code": record[start_pos+5:start_pos+8],
                "User Group Number": record[start_pos+8:start_pos+11],
                "Calling Party Number": record[start_pos+11:start_pos+27].strip()
            }
            parsed_record["Condition Codes"] = {
                "Kind of Data": record[start_pos+65:start_pos+67],
                "Length of Data": record[start_pos+67:start_pos+69],
                "Condition Code One": record[start_pos+69],
                "Condition Code Two": record[start_pos+70],
                "Condition Code Three": record[start_pos+71]
            }
            parsed_record["Alternate Routing Information"] = {
                "Kind of Data": record[start_pos+72:start_pos+74],
                "Length of Data": record[start_pos+74:start_pos+76],
                "Fusion Point Code Used": record[start_pos+76:start_pos+79],
                "Physical Route Number Used": record[start_pos+79:start_pos+82],
                "Logical Route Number Used": record[start_pos+82:start_pos+85],
                "Fusion Point Code First Selected": record[start_pos+85:start_pos+88],
                "Physical Route Number First Selected": record[start_pos+88:start_pos+91],
                "Logical Route Number First Selected": record[start_pos+91:start_pos+94]
            }
            parsed_record["Dialed Number"] = {
                "Kind of Data": record[start_pos+94:start_pos+96],
                "Length of Data": record[start_pos+96:start_pos+98],
                "Dialed Number": record[start_pos+98:start_pos+130].strip()
            }
            parsed_record["Call Metering Info"] = {
                "Kind of Data": record[start_pos+130:start_pos+132],
                "Length of Data": record[start_pos+132:start_pos+134],
                "Charge Information": record[start_pos+134]
            }

        elif record_type == "KM":
            parsed_record["Description"] = "Station-to-Station Flexible Format"
            parsed_record["Calling Party Information"] = {
                "Calling Party Identification": record[start_pos+11],
                "Tenant": record[start_pos+12:start_pos+15],
                "Calling Number": record[start_pos+14:start_pos+20].strip()
            }
            parsed_record["Account Code"] = record[start_pos+40:start_pos+50].strip()

        elif record_type == "KL":
            parsed_record["Description"] = "Incoming Flexible Format"
            parsed_record["Incoming Trunk Information"] = {
                "Kind of Data": record[start_pos+1:start_pos+3],
                "Length of Data": record[start_pos+3:start_pos+5],
                "Fusion Point Code": record[start_pos+5:start_pos+8],
                "Physical Route Number": record[start_pos+8:start_pos+11],
                "Trunk Number": record[start_pos+11:start_pos+14],
                "Logical Route Number": record[start_pos+14:start_pos+17]
            }
            parsed_record["Called Party Information"] = {
                "Kind of Data": record[start_pos+17:start_pos+19],
                "Length of Data": record[start_pos+19:start_pos+21],
                "Called Party Identification": record[start_pos+21],
                "Tenant": record[start_pos+22:start_pos+25],
                "Called Number": record[start_pos+25:start_pos+31].strip()
            }

        elif record_type == "KE":
            parsed_record["Description"] = "Incoming Standard Format"
            parsed_record["Incoming Route and Trunk Information"] = {
                "Route Number": record[start_pos+5:start_pos+8],
                "Trunk Number": record[start_pos+8:start_pos+11]
            }
            parsed_record["Called Party Identification"] = record[start_pos+11]
            parsed_record["Tenant"] = record[start_pos+12:start_pos+14]
            parsed_record["Called Number"] = record[start_pos+14:start_pos+20].strip()
            parsed_record["Account Code"] = record[start_pos+40:start_pos+50].strip()
            parsed_record["Authorization Code"] = record[start_pos+50:start_pos+66].strip()
            parsed_record["Called Party Number"] = record[start_pos+66:start_pos+82].strip()
            parsed_record["Metering Pulses"] = record[start_pos+82:start_pos+87].strip()
            parsed_record["ISDN Charge Information"] = record[start_pos+87:start_pos+131].strip()

        elif record_type == "KH":
            parsed_record["Description"] = "Incoming Standard Format"
            parsed_record["Incoming Route and Trunk Information"] = {
                "Route Number": record[start_pos+5:start_pos+8],
                "Trunk Number": record[start_pos+8:start_pos+11]
            }
            parsed_record["Called Party Identification"] = record[start_pos+11]
            parsed_record["Tenant"] = record[start_pos+12:start_pos+14]
            parsed_record["Called Number"] = record[start_pos+14:start_pos+20].strip()
            parsed_record["Account Code"] = record[start_pos+40:start_pos+50].strip()
            parsed_record["Authorization Code"] = record[start_pos+50:start_pos+66].strip()
            parsed_record["Called Party Number"] = record[start_pos+66:start_pos+82].strip()
            parsed_record["Metering Pulses"] = record[start_pos+82:start_pos+87].strip()
            parsed_record["ISDN Charge Information"] = record[start_pos+87:start_pos+131].strip()

        elif record_type == "KJ":
            parsed_record["Description"] = "Station-to-Station Extended Format"
            parsed_record["Calling Party Identification"] = record[start_pos+11]
            parsed_record["Tenant"] = record[start_pos+12:start_pos+14]
            parsed_record["Calling Number"] = record[start_pos+14:start_pos+20].strip()
            parsed_record["Called Party Identification"] = record[start_pos+20]
            parsed_record["Called Number"] = record[start_pos+21:start_pos+27].strip()
            parsed_record["Account Code"] = record[start_pos+40:start_pos+50].strip()

        elif record_type == "KA":
            parsed_record["Description"] = "Outgoing Normal Format"
            parsed_record["Outgoing Route and Trunk Information"] = {
                "Route Number": record[start_pos+5:start_pos+8],
                "Trunk Number": record[start_pos+8:start_pos+11]
            }
            parsed_record["Calling Party Identification"] = record[start_pos+11]
            parsed_record["Tenant"] = record[start_pos+12:start_pos+14]
            parsed_record["Calling Number"] = record[start_pos+14:start_pos+20].strip()
            parsed_record["Account Code"] = record[start_pos+40:start_pos+50].strip()
            parsed_record["Authorization Code"] = record[start_pos+50:start_pos+66].strip()
            parsed_record["Called Party Number"] = record[start_pos+66:start_pos+82].strip()
            parsed_record["Metering Pulses"] = record[start_pos+82:start_pos+87].strip()
            parsed_record["ISDN Charge Information"] = record[start_pos+87:start_pos+131].strip()

    else:
        return {"Error": "Unsupported record type"}

    return parsed_record


def human_readable_smdr(parsed_record):
    human_readable = f"""
    Record Type: {parsed_record["Record Type"]}
    Description: {parsed_record["Description"]}
    Call Start: {parsed_record["Call Start Date and Time"]}
    Call End: {parsed_record["Call End Date and Time"]}
    """

    if "Calling Party Number" in parsed_record:
        human_readable += f"""
        Calling Party Number: {parsed_record["Calling Party Number"]["Calling Party Number"]}
        """

    if "Condition Codes" in parsed_record:
        human_readable += f"""
        Condition Codes:
            - Condition Code One: {parsed_record["Condition Codes"]["Condition Code One"]}
            - Condition Code Two: {parsed_record["Condition Codes"]["Condition Code Two"]}
            - Condition Code Three: {parsed_record["Condition Codes"]["Condition Code Three"]}
        """

    if "Dialed Number" in parsed_record:
        human_readable += f"""
        Dialed Number: {parsed_record["Dialed Number"]["Dialed Number"]}
        """

    if "Call Metering Info" in parsed_record:
        human_readable += f"""
        Charge Information: {parsed_record["Call Metering Info"]["Charge Information"]}
        """

    if "Calling Party Information" in parsed_record:
        human_readable += f"""
        Calling Party Identification: {parsed_record["Calling Party Information"]["Calling Party Identification"]}
        Tenant: {parsed_record["Calling Party Information"]["Tenant"]}
        Calling Number: {parsed_record["Calling Party Information"]["Calling Number"]}
        """

    if "Account Code" in parsed_record:
        human_readable += f"""
        Account Code: {parsed_record["Account Code"]}
        """

    if "Incoming Trunk Information" in parsed_record:
        human_readable += f"""
        Incoming Trunk Information:
            - Fusion Point Code: {parsed_record["Incoming Trunk Information"]["Fusion Point Code"]}
            - Physical Route Number: {parsed_record["Incoming Trunk Information"]["Physical Route Number"]}
            - Trunk Number: {parsed_record["Incoming Trunk Information"]["Trunk Number"]}
            - Logical Route Number: {parsed_record["Incoming Trunk Information"]["Logical Route Number"]}
        """

    if "Called Party Information" in parsed_record:
        human_readable += f"""
        Called Party Information:
            - Called Party Identification: {parsed_record["Called Party Information"]["Called Party Identification"]}
            - Tenant: {parsed_record["Called Party Information"]["Tenant"]}
            - Called Number: {parsed_record["Called Party Information"]["Called Number"]}
        """

    if "Incoming Route and Trunk Information" in parsed_record:
        human_readable += f"""
        Incoming Route and Trunk Information:
            - Route Number: {parsed_record["Incoming Route and Trunk Information"]["Route Number"]}
            - Trunk Number: {parsed_record["Incoming Route and Trunk Information"]["Trunk Number"]}
        """

    if "Called Party Identification" in parsed_record:
        human_readable += f"""
        Called Party Identification: {parsed_record["Called Party Identification"]}
        """

    if "Tenant" in parsed_record:
        human_readable += f"""
        Tenant: {parsed_record["Tenant"]}
        """

    if "Called Number" in parsed_record:
        human_readable += f"""
        Called Number: {parsed_record["Called Number"]}
        """

    if "Authorization Code" in parsed_record:
        human_readable += f"""
        Authorization Code: {parsed_record["Authorization Code"]}
        """

    if "Called Party Number" in parsed_record:
        human_readable += f"""
        Called Party Number: {parsed_record["Called Party Number"]}
        """

    if "Metering Pulses" in parsed_record:
        human_readable += f"""
        Metering Pulses: {parsed_record["Metering Pulses"]}
        """

    if "ISDN Charge Information" in parsed_record:
        human_readable += f"""
        ISDN Charge Information: {parsed_record["ISDN Charge Information"]}
        """

    return human_readable.strip()



# Placeholder for example usage
# Note: Replace the placeholder below with actual SMDR data loading logic.
# For instance, you can load SMDR records from a file 'necsmdr.txt' like this:
# with open('necsmdr.txt', 'r') as file:
#     smdr_records = [line.strip() for line in file.readlines() if line.strip()]

# Example loading and processing SMDR records from a list (populate this list with actual data)
smdr_records = [
    # "KK2021030512000054023000021000013396...",  # Example record, replace with actual data
    # Add more records here
]

for smdr_record in smdr_records:
    parsed_record = parse_smdr_record(smdr_record)
    print("Parsed SMDR Record:")
    print(json.dumps(parsed_record, indent=2))
    print("\nHuman Readable SMDR:")
    print(human_readable_smdr(parsed_record))
    print("-" * 80)