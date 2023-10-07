---

# Letter Generation Script README

This Python script is designed to generate personalized letters by merging a list of invited names with a template letter. It reads a list of names from `invited_names.txt`, replaces the `[name]` placeholder in a template letter with each name, and then saves individualized letters for each person in the `ReadyToSend` directory.

## Prerequisites

Before you run this script, ensure you have the following:

1. Python installed on your computer (Python 3.x recommended).

## Usage

1. Place the list of invited names in a file named `invited_names.txt` in the `./Input/Names/` directory. Each name should be on a separate line.

2. Customize the template letter by editing `starting_letter.txt` in the `./Input/Letters/` directory. Replace the `[name]` placeholder with the text you want to include before each name.

3. Run the script by executing the following command in your terminal:

   ```bash
   python script.py
   ```

4. After the script completes, individualized letters will be created for each name in the `./Output/ReadyToSend/` directory with filenames like `letter_for_[name].txt`.

## Example

Suppose `invited_names.txt` contains:

```
Alice
Bob
Charlie
```

And `starting_letter.txt` contains:

```
Dear [name],

We are pleased to invite you to our event.
```

After running the script, you will find three files in the `./Output/ReadyToSend/` directory:

- `letter_for_Alice.txt`:

  ```
  Dear Alice,

  We are pleased to invite you to our event.
  ```

- `letter_for_Bob.txt`:

  ```
  Dear Bob,

  We are pleased to invite you to our event.
  ```

- `letter_for_Charlie.txt`:

  ```
  Dear Charlie,

  We are pleased to invite you to our event.
  ```
