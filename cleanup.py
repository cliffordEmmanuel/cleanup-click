# create a dictionary to categorize all the file types
import os
from pathlib import Path
import json
import click
import yaml
from yaml.loader import SafeLoader

# getting the folder mappings here:

def getDirectoryMapping()->dict:
    """parses the dir_mappings yml file and returns the folders with the associated file extensions as a dict.

    Returns:
        dict: contains the folder categorisations.
    """
    with open('dir_mappings.yml', 'r') as f:
        dir_mapping = yaml.load(f, Loader=SafeLoader)
        return dir_mapping


def pickDirectory(value:Path)->str:
    """Returns the category of the file based on it's extensions

    Args:
        value (Path): the path to a single file to be processed.

    Returns:
        str: returns the directory mapping to the extension of the file passed.
    """
    
    # getting the directory mappings
    directories = getDirectoryMapping()
    
    for category, extensions in directories.items():
        for extension in extensions:
            if extension == value:
                return category
    return 'MISC'

@click.command()
@click.option('--dir' ,'-d', default=os.getcwd(), help='path to messy folder if not specified it checks the current directory!')
def organizeDirectory(dir:str)->None:
    """Puts files in the specified directory(or current directory) into their specific 
    category based on their file type.

    Args:
        dir (str): the path to the directory that needs to be cleaned up
    """
    click.echo(f"Scanning this clumsy folder:{dir}......")
    click.echo(f"Creating new folders......")
    click.echo("Mapping files to the new folders......")
    for item in os.scandir(dir):
        # returns a list of all files in the current directory
        if item.is_dir(): # making sure folders are skipped
            continue
        
        filePath = Path(item) # this gets the path of each item
        filetype = filePath.suffix.lower() # isolates the extension of each file
        directory = pickDirectory(filetype) # fetch the associated extension
        directoryPath = Path(dir,directory)  # casts the directory to a file path
        
        # creates the category directory inside the <dir> specified.
        
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()

        # moves the files to the associated folders created.
        filePath.rename(Path(dir,directoryPath,filePath.name))
        
    click.echo("Done!! Enjoy some sanity!!")
        

def showMappings():
    """Returns the default directories in json format"""

    # getting the directory mappings
    directories = getDirectoryMapping()
    return json.dumps(directories, indent=2)


if __name__ == "__main__":
    organizeDirectory()
   
