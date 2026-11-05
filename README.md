# Internship Application Tracker

A small Python terminal app for recording internship applications. Add a company and job role, view your entries, and keep them between sessions using a CSV file.

I built this as a guided learning project while studying Python and preparing for summer 2027 internship applications. The menu, lists, and loops put my current Python knowledge into practice; CSV saving and loading introduced file handling, which I am continuing to learn.

## Features

- Add a company name and job role.
- View all recorded applications, one per line.
- Save each new application to `applications.csv`.
- Load saved applications when the program starts.
- Start with an empty list if the CSV file does not exist.
- Show a message for menu choices other than `1`, `2`, or `3`.

## Run locally

You need **Python 3**. The app uses Python's built-in `csv` module, so there are no additional packages to install.

Download or clone this repository, then open a terminal **in the folder containing `application.py`** and run:

```bash
python3 application.py
```

The menu is:

```text
1. Add application
2. View applications
3. Exit
```

Choose `1` to enter an application, `2` to view the list, or `3` to quit.

## Example

Using fictional details:

```text
Choose: 1
Type in the company name: Example Studio
Type in the job role: Software Intern

1. Add application
2. View applications
3. Exit
Choose: 2
Example Studio - Software Intern
```

## How saving works

Adding an application updates the in-memory list and appends a row to `applications.csv`. On startup, the app reads the CSV back into the list.

The CSV has two columns—company and role—with no header row:

```csv
Example Studio,Software Intern
```

The file is created after you add your first entry. It is read and written in the terminal's current folder, so run the program from the same folder each time.

Keep your real `applications.csv` on your computer rather than uploading it to the public repository. If you use Git to sync the project, add `applications.csv` to `.gitignore` first.

## Try it

1. Add a fictional company and role.
2. Choose `2` and check that the entry appears.
3. Exit with `3`, then run the program again.
4. Choose `2` before adding anything. The saved entry should still appear.

## Current scope and next steps

This first version stores a company and role for each application. It does not yet support editing or deleting entries, application statuses, or validation of empty fields and malformed CSV rows.

Next, I plan to add an empty-list message, validate input, and move repeated logic into functions. I will revisit CSV handling as I learn more about working with files.
