# Import flask and os modules
from flask import Flask, request
import os

# Create an app instance with the name bingo
app = Flask("bingo")

# Define a function that recursively lists all files in a given folder that match the given file types and exclude the given folders
def list_files(folder, file_types, exclude_folders):
    # Initialize an empty list to store the file paths
    files = []
    # Loop through each item in the folder
    for item in os.listdir(folder):
        # Get the full path of the item
        path = os.path.join(folder, item)
        # If the item is a file and has an extension that matches the file types, append it to the list
        if os.path.isfile(path) and path.endswith(tuple(file_types)):
            files.append(path)
        # If the item is a directory and is not in the exclude folders, call the function recursively and extend the list
        elif os.path.isdir(path) and item not in exclude_folders:
            files.extend(list_files(path, file_types, exclude_folders))
    # Return the list of files
    return files

# Define a route that takes a folder address as a parameter
@app.route("/<path:folder>")
def show_files(folder):
    # Get the absolute path of the folder
    folder = os.path.abspath(folder)
    # Check if the folder exists
    if os.path.exists(folder) and os.path.isdir(folder):
        # Define the file types to include
        file_types = [".cs", ".xaml", ".md", ".py", ".rst"]

        # Define the folders to exclude
        exclude_folders = [".git", ".vscode", "__pycache__", "bin", "obj", "packages", "Properties", "Resources", "Resources.Designer.cs", "Settings", "Settings.Designer.cs", "Service References"]
        
        # Get the list of files in the folder and its subfolders that match the file types and exclude the folders
        files = list_files(folder, file_types, exclude_folders)
        
        # Initialize an string to store the output
        output = "<!DOCTYPE html><html>"
        
        # CSS for syntax highlighting
        #output += "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/styles/default.min.css'>"
        # Javascript for syntax highlighting
        #output += "<script src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/highlight.min.js'></script>"

        # CSS Style for the output
        #output += "<style>body {font-family: 'Courier New';} h3 {color: #00FF00;} h4 {color: #FF0000;} p {color: #FFFFFF;}</style>"
        output += "<style>body {font-family: Courier New; background-color: #000000; color: #FFFFFF;} h3 {color: #00FF00;} h4 {color: #FF0000;} p {color: #FFFFFF;} xmp {color: #FFFFFF;}</style>"
        
        output += "<body>"
        output += f"<h3>{folder} :</h3>"
        # Loop through each file
        for file in files:
            # Get the relative path of the file
            relative_path = os.path.relpath(file, folder)
            # Append the file path to the output with markdown formatting
            output += f"<H4>.\{relative_path} :</H4>"
            # Open the file and read its content
            with open(file, "r", encoding='utf-8-sig') as f:
                content = f.read()
            extension = os.path.splitext(file)[1][1:]
            # Append the file content to the output with markdown formatting
            output += "<p>"
            output += f"```{extension}"
            output += "<xmp>"
            output += f"{content}"
            output += "</xmp>"
            output += "```"
            output += "</p>"
        output += "</body></html>"
        # Return the output as a response
        return output
    # If the folder does not exist, return an error message
    else:
        return "<H1>Invalid folder address. Please enter a valid folder address.</H1>"
# Return an error if route is blank
@app.route("/")
def error():
    return "<H1>Please enter a folder address.</H1>"