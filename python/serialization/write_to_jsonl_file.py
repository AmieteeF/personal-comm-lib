import json
import os
from typing import Any

def write_to_jsonl(data_list: list[dict[str, Any], file_name: str, output_folder: str = "") -> None:
    """
    Writes python dictionary objects as records in an.jsonl file to an output in the current working directory.

    In a .jsonl fie, one line corresponds to one json object/record.

    :param: data_list (list[dict[str, Any]): A list of python dictionary objects to write to the .jsonl file
    :param: file_name (str): The name of the data file produced by the process.
    :param category (str): An optional folder name within the cwd to save the file to.
    :return: None
    """
    # Define the folder path (relative or absolute)
    output_path = os.path.join(os.getcwd(), output_folder)

    # Ensure the folder exists
    os.makedirs(output_path, exist_ok = True)

    # Create the full file path
    data_file = os.path.join(output_path, file_name + ".jsonl")

    print(f"Creating data file: {data_file} with {len(data_list)} records.")
    with open(data_file, "w", encoding = "utf-8") as f:
        for data in data_list:
            json_str = json.dumps(data)
            # write data delimited by a newline character
            f.write(json_str + "\n")
