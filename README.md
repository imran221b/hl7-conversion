HL7 to JSON Format Converter
==================================

A Python package to convert HL7 v2 messages to JSON format. 

Installation from source
-------------------

Extract `hl7-conversion-{tag}.tar.gz` file in your working directory.

Change directory to project root:

    cd hl7-conversion

Create and activate python virtual env:

    python3.8 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip

Install hl7-conversion package:
    
    pip install -e .

## CLI usage

Type `--help` after commands to see full list of options

```
$ hl7 --help
Usage: hl7 [OPTIONS] COMMAND [ARGS]...

  HL7 to JSON format converter

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  tojson  Convert given HL7 message to JSON format 
```
```
$ hl7 tojson --help
Usage: hl7 tojson [OPTIONS] INPUT

  Convert given HL7 message to JSON format

Options:
  -o, --output FILENAME  Output file path
  --help                 Show this message and exit.
```
Example:

    hl7 tojson input.txt -o output.txt

In this example, the command will try to read the input HL7 message from input.txt file and write the converted JSON output to output.txt file.

## Programmatic usage

### **HL7Client**

### **HL7Client.hl7tojsonconvert**

Arguments:
- `message (str)`: Given HL7 message in string format. 
 
See `tests/test_client` for usage examples.
