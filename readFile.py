def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file at {file_path}.")

# Example usage
file_path = 'example.txt'  # Replace with your file path
read_file(file_path)
