# NateDhaliwal-Package
This is a package that allows Python functions to be used better, with less lines of code.
<br>
<hr>

## Installation
To install this package, enter this command line:
`pip install natedhaliwal`
<br><br>
This package allows you to type in colour by specifying the name of the colour as one of its many functions.
<br>
The program displays the text in the specified colour, which is red, in this case. At the end of the line, the program removes any effects that may continue onto the next line.
<br><br>
With `natedhaliwal`, you can also open, create, read, overwrite and add data to and from the file.
<br><br>
You can allow the program to wait a specified number of seconds, clear the console or output, generate a random number in the specified range, pick a random item from the specified list, and even scrape websites as well!
<br><br>
In addition, you may convert JSON data, and vice-versa. Perfect for dealing with large JSON files!
<hr>


## Examples of code
### Functions

- `display(text, colour,typewriter)`: Displays text in the output, with an optional color or effect feature, or a typewriter-style display. If the colour field is left empty, it acts like a normal `print()` statement.
  #### The list of colours/effects are:
  - Bold
  - Italic
  - Underline
  - Red
  - Pink
  - Yellow
  - Green
  - Blue
  - Purple
  - Grey
<br>
The typewriter must be specified when using it, setting it to True. It's off by default.
- `clear()`: Clears the output screen.
- `randnum(start, end)`: Gets a random number from the range given.
- `randomlist(listName)`: Picks a random value from a provided list.
- `wait(seconds)`: Pauses the program for the specified number of seconds.
- `scrape(website_url)`: Scrapes the given website and returns the data in JSON format.
- `jsontodict(json_data)`: Converts JSON data to a dictionary.
- `dicttojson(dict_data)`: Converts a dictionary to JSON.
- `overwritefile(filename, data)`: Writes the data to the specified file and removes previous data.
- `writefile(filename, data)`: Adds the data to the specified file.
- `createfile(filename)`: Creates a new file with the specified name.
- `readfile(filename)`: Reads the specified file and returns the data.
<hr>

## More coming soon!