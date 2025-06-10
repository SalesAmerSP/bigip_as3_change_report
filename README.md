/*************  ✨ Windsurf Command ⭐  *************/
# AS3 Change Report

This script generates a report of changes made to an AS3 configuration on a BIG-IP.

## Usage

1. Clone the repository
2. Install the required Python packages with `pip install -r requirements.txt`
3. Run the script with `python as3_change_report.py`

## Options

* `-h, --help` - Show this help message and exit
* `-u USER, --username USER` - BIG-IP username
* `-p PASSWORD, --password PASSWORD` - BIG-IP password
* `-H HOSTNAME, --hostname HOSTNAME` - BIG-IP hostname or IP address

## Output

The script will output a report in Markdown format to the console. The report will include the following information:

* The AS3 declaration(s) that were changed
* The specific lines that were changed
* The old and new values of the changed lines

## Example Output


/*******  776e8d94-cb0d-428f-b8c6-fc358f9649ff  *******/