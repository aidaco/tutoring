# Creating a new repository

## Selecting a License
- By default anything you put on github is closed
    source, meaning no one can use it without
    requesting your permission.
- Adding a license lets others use your work.
- Most of the time, a permissive license is preferred,
    except for commercial projects.
- Add a file named 'LICENSE' containing the text
    of your desired license.
- Recommended: MIT License

## README
- touch README

## Binary Prefixes
- bit : b : 0|1 : ex. boolean T|F
- byte: B : 8b : ex. character (ASCII) is 1B
- kilobyte: KB : 1024B *or* 1000B
- megabyte: MB : 1024KB *or* 1000KB : HD picture 2-3MB
- gigabyte: GB : 1024MB *or* 1000MB : HD Movie ~1GB

### Others:
- kilobit : Kb : Typically seen as Kbits/sec for networking speed
- megabit: Mb : Seen as Mbits/sec or Mb/s for networking


## Adding a .gitignore
- touch .gitignore
- Add patterns for files/folders to ignore
- Things like pycache, settings, password files

## Branching
- ### Create New Branch
- git branch BRANCH_NAME
- ### List Branches
- git branch
- ### Switch to Branch
- git checkout BRANCH_NAME