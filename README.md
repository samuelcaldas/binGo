# binGo

binGo is a Flask app that allows you to browse and view the files in your local folders using Microsoft Edge browser and Copilot.

## Features

- **List files**: You can see the list of files in any folder on your computer that match the specified file types and exclude the specified folders.
- **View files**: You can view the content of any file in the list with markdown formatting and syntax highlighting.
- **Search files**: You can use Copilot to search for files in your folder using natural language queries.

## Installation

To install binGo, you need to have Python 3.8 or higher and Flask 2.0 or higher on your computer. You can install Flask using pip:

```bash
pip install Flask
```

Then, you need to clone this repository or download the app.py file to your computer.

## Usage

To use binGo, you need to run the run_binGo.cmd file on app folder:

```bash
.\run_binGo.cmd
```

This will start a local server on port 80. You can then open Microsoft Edge browser and go to the following address:

```text
http://localhost/<path:folder>
```

where `<path:folder>` is the relative or absolute path of the folder you want to browse. For example, if you want to browse the folder C:\Users\UserName\source\repos\binGo, you can go to:

```text
http://localhost/C:/Users/UserName/source/repos/binGo
```

You will see the list of files in the folder and its subfolders that match the file types and exclude the folders defined in the app.py file. You can click on any file to view its content with markdown formatting and syntax highlighting.

You can also use Copilot to search for files in your folder using natural language queries. For example, you can ask Copilot to show you the files that contain the word "binGo" or the files that are written in Python. Copilot will try to understand your query and show you the relevant files.
