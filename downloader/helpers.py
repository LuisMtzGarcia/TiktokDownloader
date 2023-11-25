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

def storage_file_exists(file_name):
    """Verifies if the requested storage file exists. If it doesn't, it's generated."""
    complete_file_name = f"{file_name}.txt"

    file_path = get_file_path(complete_file_name)

    return os.path.exists(file_path)