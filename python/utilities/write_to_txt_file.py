import os

def write_to_txt_file(file_name: str, content: str, file_dir: str, mode: str, flush: bool = False) -> str:
    """
    Writes the given content to a text file in the specified write mode to the specified directory.

        :param file_name (str): The name of the text file.
        :param content (str): The content to write to the text file.
        :param file_dir (str): The directory where the text file will be saved.
        :param mode (str): The mode in which to open the file (e.g., 'w' for write, 'a' for append).
        :param flush (bool): Whether to flush the file buffer after writing.
        :return: file_path (str): The path to the written text file.
    """
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    
    file_path = os.path.join(file_dir, file_name)
    with open(file_path, mode, encoding = 'utf-8') as txt_file:
        txt_file.write(content)
        if flush:
            txt_file.flush()
    
    return file_path
