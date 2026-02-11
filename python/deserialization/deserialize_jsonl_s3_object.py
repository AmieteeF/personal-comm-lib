from io import TextIOWrapper
from typing import Any
import json
from pprint import pprint

def deserialize_jsonl_s3_object(s3_client: Any, bucket_name: str, key: str) -> list[dict[str, Any]]:
    """
    Deserializes a .jsonl S3 object by streaming in the file and desrializing each line 
    into a python dictionary.
    
    :param s3_client: The S3 Client.
    :param bucket_name (str): The bucket name where the .jsonl S3 objects are stored.
    :param key (str): They S3 object's key.
    :return: A list of deserialized .json records as python dictionaries.
    """
    if not key.endswith(".jsonl"):
        print(f"S3 object is not a .jsonl file: {key}")
        return []
    else:
        # get object from s3
        print(f"Getting S3 object with key: {key}")
        resp = s3_client.get_object(Bucket = bucket_name, Key = key)
        body = resp["Body"]  # botocore.response.StreamingBody

        data = []

        # wrap the byte stream as text; ensure the correct encoding (usually UTF-8)
        text_stream = TextIOWrapper(body, encoding = "utf-8")

        for line in text_stream:
            line = line.strip()
            if not line:
                continue  # skip blank lines
            record = json.loads(line)
            # add record to list
            print("Appending record:")
            pprint(record)
            data.append(record)
        
        return data
