# CryptMyRepl
CryptMyRepl is a command-line tool to make your [repl](https://replit.com/~) private.
Any user that want to see files of the repl will be blocked by the cryption.
> by BlueRed
> made with
> 
> ![](https://skillicons.dev/icons?i=py,vscode)

## Previews
> usage
![](https://cdn.discordapp.com/attachments/976509056774705252/1015652943682359367/code.png)

> setup
![](https://cdn.discordapp.com/attachments/976509056774705252/1015653266941558824/code.png)

> final file
![](https://cdn.discordapp.com/attachments/976509056774705252/1015651929138921523/code.png)

## Usage

### Setup
To setup **CryptMyRepl**, you need to lauch **setup.py** as administrator in a command line. Make shure that the directory printed is in your Python modules path.
```batch
python "./setup.py"
```

### Create a private repl
Execute this command
```batch
python -m CryptMyRepl "./path/to/your-py-file.py"
```
This will create a new directory nammed **repl** on your current path and print a key and a value that you have to place it on the repl environ
```
╔> curernt dir ./
║    ╔> repl
║    ║   main.py // your obfuscated code
║    ║   key.txt // the cryption key
```
KEY NAME: `CRYPTIONKEY`
