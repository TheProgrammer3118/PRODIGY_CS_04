# Simple Keylogger 🖥️

A simple keylogger implemented in Python using the `pynput` library. This tool captures keystrokes and logs them to a specified file with timestamps. 📜

## Author

Dharmpreet Singh 👤

## Features

- Logs each keystroke, including special keys. ⌨️
- Configurable log file name and logging level via command-line arguments. ⚙️
- Timestamps included in log entries. 🕒

## Requirements

- Python 3.x 🐍
- `pynput` library (install via pip) 📦

### Installation

To install the required library, run:

pip install pynput
Usage
You can run the keylogger from the command line with optional arguments:

python keylogger.py [OPTIONS]

Options
--logfile <filename>: Specify the name of the log file (default: keylogging.txt). 📂
--loglevel <level>: Set the logging level. Available levels are:
DEBUG
INFO (default)
WARNING
ERROR
CRITICAL ⚠️

Here's the README.md file with emojis added for a more engaging presentation:

markdown
# Simple Keylogger 🖥️

A simple keylogger implemented in Python using the `pynput` library. This tool captures keystrokes and logs them to a specified file with timestamps. 📜

## Author

Dharmpreet Singh 👤

## Features

- Logs each keystroke, including special keys. ⌨️
- Configurable log file name and logging level via command-line arguments. ⚙️
- Timestamps included in log entries. 🕒

## Requirements

- Python 3.x 🐍
- `pynput` library (install via pip) 📦

### Installation

To install the required library, run:

pip install pynput
Usage
You can run the keylogger from the command line with optional arguments:


python keylogger.py [OPTIONS]
Options
--logfile <filename>: Specify the name of the log file (default: keylogging.txt). 📂
--loglevel <level>: Set the logging level. Available levels are:
DEBUG
INFO (default)
WARNING
ERROR
CRITICAL ⚠️
Example
To run the keylogger and save logs to my_log.txt with DEBUG level, use

python keylogger.py --logfile=my_log.txt --loglevel=DEBUG
Logging Format
Each log entry will include a timestamp and the key that was pressed, formatted as follows:

Important Notes
Ethical Use: Ensure you have permission to log keystrokes and comply with all applicable laws and regulations. ⚖️
Data Security: Be mindful of how the logged data is stored and accessed to prevent misuse. 🔒
