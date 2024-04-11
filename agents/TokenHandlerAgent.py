import os
import shutil
import zipfile
from datetime import datetime

def token_handler(files, user_triggers, rename_prefix=None):
    """
    Manages NEC SMDR file operations based on user triggers, ensuring data is effectively archived,
    organized, or modified as needed.

    :param files: list, the NEC SMDR files to be managed.
    :param user_triggers: str, specific user actions triggering file operations.
    :param rename_prefix: str, optional prefix for renaming files for better identification.
    :return: str, a message indicating completion and status of file operations.
    """

    def organize_file(file):
        """
        Custom function to organize an NEC SMDR file based on its content and metadata.
        """
        # Extract relevant information from the NEC SMDR file
        with open(file, 'r') as f:
            smdr_data = f.read()

        # Parse the SMDR data to extract relevant fields (e.g., call start time, call type)
        call_start_time = datetime.strptime(smdr_data[20:29], '%m%d%H%M%S')
        call_type = smdr_data[4]

        # Create a directory structure based on the extracted information
        target_directory = os.path.join(target_directory_path, call_start_time.strftime('%Y-%m'), call_type)
        os.makedirs(target_directory, exist_ok=True)

        # Move the file to the appropriate directory
        shutil.move(file, os.path.join(target_directory, os.path.basename(file)))

    target_directory_path = '/mnt/data/'

    for file in files:
        try:
            file_basename = os.path.basename(file)
            target_path = os.path.join(target_directory_path, file_basename)

            if user_triggers == "archive":
                shutil.move(file, target_path)

            elif user_triggers == "copy":
                shutil.copy(file, target_path)

            elif user_triggers == "organize":
                organize_file(file)

            elif user_triggers == "delete":
                os.remove(file)

            elif user_triggers == "rename":
                new_name = rename_prefix + file_basename if rename_prefix else 'new_' + file_basename
                os.rename(file, os.path.join(os.path.dirname(file), new_name))

            elif user_triggers == "compress":
                zip_path = os.path.join(target_directory_path, file_basename + '.zip')
                with zipfile.ZipFile(zip_path, 'w') as zipf:
                    zipf.write(file, file_basename)

            elif user_triggers == "change_permission":
                os.chmod(file, 0o644)  # Adjust permissions as needed for security

        except FileNotFoundError:
            print(f"File not found: {file}")
        except PermissionError:
            print(f"Permission denied: {file}")
        except OSError as e:
            print(f"OS error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error handling NEC SMDR file {file}: {e}")

    return f"File operations for '{user_triggers}' completed successfully for NEC SMDR files."

# Example usage
smdr_files = ['/path/to/smdr_file1.txt', '/path/to/smdr_file2.txt', '/path/to/smdr_file3.txt']
user_trigger = 'organize'  # Other triggers: 'archive', 'copy', 'delete', 'compress', etc.
rename_prefix = 'processed_'  # Used if the trigger is 'rename'
result = token_handler(smdr_files, user_trigger, rename_prefix)
print(result)