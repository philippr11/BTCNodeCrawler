import os

def iterate_block_files(block_folder):
    """
    Iterates over all block files in the given folder.
    Assumption: The block files are named as <block_number>.dat
    """
    for file_name in os.listdir(block_folder):
        if file_name.endswith('.dat'):
            file_path = os.path.join(block_folder, file_name)
            with open(file_path, 'rb') as f:
                block_data = f.read()
                yield file_name, block_data
