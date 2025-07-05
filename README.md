# ensphere

## Overview

`ensphere` is a Python command-line tool that performs encryption and decryption using a substitution cipher. It relies on a customizable character mapping defined in codebook.json.
The tool is case-insensitive: all input is converted to lowercase before processing.
Any character not defined in the codebook will be replaced with an asterisk `*`.

## Getting Started

### 1. Install

```bash
git clone https://github.com/nefleia/ensphere.git
cd ensphere
poetry install
```

### 2. Add codebook

Place your `codebook.json` file in the **project root directory** (the same directory as this README).
This file defines the character mapping used for encryption and decryption.

```json
{
  "a": 1,
  "b": 2,
  "c": 3,
  "...": "...",
  " ": 68
}
```

> **Note:**
> Do **not** use `*` as a key in your codebook file.
> The `*` character is reserved to represent any character not defined in the codebook.

### 3. Run

#### Encrypt

```bash
ensphere encrypt 'Hello, World!'
```

#### Encrypt from a .txt file

```bash
ensphere encrypt --file path/to/input.txt
```

- **Only `.txt` files are allowed for the `--file` option. If a non-txt file is specified, an error will occur.**

#### Decrypt

```bash
ensphere decrypt '8 5 12 12 15 38 68 23 15 18 12 4 40'
```

#### Options

- `-f`, `--file FILE` File path of the text to be encrypted (only .txt files are allowed)

#### Example

```bash
$ ensphere encrypt 'Hello, World!'
8 5 12 12 15 38 68 23 15 18 12 4 40

$ ensphere encrypt --file test.txt
8 5 12 12 15 38 68 23 15 18 12 4 40

$ ensphere decrypt '8 5 12 12 15 38 68 23 15 18 12 4 40'
hello, world!
```
