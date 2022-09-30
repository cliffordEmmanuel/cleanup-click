# Cleanup with click

This script is aimed quickly rearranging clumsy a directory by putting the files into specific categories ie Documents, audio, images and videos. This will be a cli app built using click.

## How this works

There's a pre-configured file extension to folder category mapping done in the **dir_mappings**: update to fit your needs.

_When the script is executed it does the following:_
- If a directory path is not specified, it scans the current directory
- Using the file to folder mapping file as a lookup source, it creates folders for each categories and places the associated files inside
- Any other files not accounted for in the pre-configured folders, gets placed in the **MISC** folder.
- It skips are existing directories.

## Recreating this project

- Clone this repo to access the code.
- Create a virtual environment using the **requirements.txt** file
- Ran using this command: `python cleanup.py -d <'path of directory to be cleaned'>`
- To access the help type this: `python cleanup.py --help`


# Creating a basic click app.

Setup is pretty straight forward, do a `pip install click`

It uses the concept of python decorators to turn function into cli programs, which is really dope. A basic example from the docs looks like this:

```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
```

the `@click.command()` decorator turns the function into a cli and the `@click.command()` decorator provides an avenue to accepts arguments when the program is run.

to ran this example, the code will be: 
```cmd 
python hello.py --count=5
```

It also generates a cool help page. For instance for the above program the help page becomes:
```cmd
python hello.py --help
Usage: hello.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.
```

Read more in the docs _[here](https://palletsprojects.com/p/click/)_.