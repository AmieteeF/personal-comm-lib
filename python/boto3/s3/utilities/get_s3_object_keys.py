from typing import Any

def get_s3_object_keys(s3_client: Any, bucket_name: str, prefix: str) -> list[str]:
    """
    Returns all the s3 object keys listed under the given prefix.
    
    :param s3_client (Any): The s3 Client.
    :param bucket_name (str): The s3 bucket name.
    :param prefix (str): The "folder" where the objects are located.
    :return: A list of the s3 object file keys.
    """
    object_keys = []

    resp = s3_client.list_objects_v2(Bucket = bucket_name, Prefix = prefix)
    for obj in resp.get("Contents", []):
        key = obj["Key"]
        if key == prefix or key.endswith("/"):
            # This is the folder marker; skip it
            continue
        # collect input file keys
        object_keys.append(key)
    
    return object_keys
