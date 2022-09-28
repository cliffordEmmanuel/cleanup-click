# create a dictionary to categorize all the file types
import os
from pathlib import Path
import json
import click

# TODO: put this in a yaml file so it can be imported and updated with new categories
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt','.docx', '.xlsx'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    """this function returns the category of the file based on it's extensions"""
    for category, extensions in SUBDIRECTORIES.items():
        for extension in extensions:
            if extension == value:
                return category
    return 'MISC'

@click.command()
@click.option('--filepath' ,'-f', default=os.getcwd(), help='path to messy folder if not specified it checks the current directory!')
def organizeDirectory(filepath:str)->None:
    """Puts files in the specified directory(or current directory) into their specific 
    category based on their file type.

    Args:
        filepath (str): the path to the directory that needs to be cleaned up
    """
    # TODO: add an echo to show progress.
    for item in os.scandir(filepath):
        # returns a list of all files in the current directory
        if item.is_dir(): # making sure categories are skipped
            continue

        filePath = Path(item) # this gets the path of each item
        filetype = filePath.suffix.lower() # this isolates the extension of each file
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)  # casts the directory to a file path
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

# TODO: add this to a group so we can also display the contents.
def showDefaultDirectories():
    """this returns the default directories in json format"""
    return json.dumps(SUBDIRECTORIES)


if __name__ == "__main__":
    organizeDirectory()
   
