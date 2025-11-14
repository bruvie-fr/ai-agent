import os
from functions.config import *
from google.genai import types
def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    os.makedirs(os.path.dirname(abs_file_path), mode=0o777, exist_ok=True)
    
    if os.path.isdir(abs_file_path):
        return "Error: Path points to a directory, not a file"
    try:
         
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: {e}"



    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a file within the specified working directory, creating any missing folders as needed. Prevents writing outside the working directory for safety.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path of the file to write within the working directory (e.g., 'notes/output.txt').",
            ),

            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file."
            ),
        },
    ),
)



    
 
