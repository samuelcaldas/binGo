# Import flask and os modules
from flask import Flask, request
import os

# Create an app instance with the name bingo
app = Flask("bingo")

# Define a function that recursively lists all .cs and .xml files in a given folder
def list_files(folder):
    # Initialize an empty list to store the file paths
    files = []
    # Loop through each item in the folder
    for item in os.listdir(folder):
        # Get the full path of the item
        path = os.path.join(folder, item)
        # If the item is a file and has .cs or .xml extension, append it to the list
        if os.path.isfile(path) and (path.endswith(".cs") or path.endswith(".xml")):
            files.append(path)
        # If the item is a directory, call the function recursively and extend the list
        elif os.path.isdir(path):
            files.extend(list_files(path))
    # Return the list of files
    return files

# Define a route that takes a folder address as a parameter
@app.route("/<path:folder>")
def show_files(folder):
    # Get the absolute path of the folder
    folder = os.path.abspath(folder)
    # Check if the folder exists
    if os.path.exists(folder) and os.path.isdir(folder):
        # Get the list of files in the folder and its subfolders
        files = list_files(folder)
        # Initialize an empty string to store the output
        output = ""
        # Loop through each file
        for file in files:
            # Get the relative path of the file
            relative_path = os.path.relpath(file, folder)
            # Append the file path to the output with markdown formatting
            output += f"- ./{relative_path}\n"
            # Open the file and read its content
            with open(file, "r") as f:
                content = f.read()
            # Append the file content to the output with markdown formatting
            output += f"```{file[-2:]}\n{content}\n```\n"
        # Return the output as a response
        return output
    # If the folder does not exist, return an error message
    else:
        return "Invalid folder address. Please enter a valid folder address."
