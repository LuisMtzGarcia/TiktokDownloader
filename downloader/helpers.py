import os

def generate_file(file_name):
    """Generates a blank .txt file."""
    file_path = get_file_path(file_name)

    with open(file_path, 'x') as f:
            f.write('')

def get_storage_path():
    """Returns the complete path for the Storage directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'storage'))

def get_file_path(file_name):
     """Returns the complete path for the storage file."""
     storage_path = get_storage_path()
     return os.path.join(storage_path, f'{file_name}.txt')