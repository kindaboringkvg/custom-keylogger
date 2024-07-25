# Custom KeyLogger

## Overview

This KeyLogger is a Python script designed to log keystrokes to a file. It captures all key presses and writes them to a log file. The script also includes functionality to clean the log file by removing unnecessary key strokes. It stops logging when the `F1` and `F2` keys are pressed together.

## Features

- Logs keystrokes to `log.txt`
- Cleans the log file to remove unnecessary key strokes
- Stops logging when `F1` and `F2` keys are pressed simultaneously

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Install the required Python packages:
   ```bash
   pip install pynput
   ```

## Usage

1. Run the script:
   ```bash
   python keylogger.py
   ```
2. The script will start logging keystrokes and writing them to `log.txt`.
3. Press `F1` and `F2` together to stop the script.

## Converting to Executable

If you are not comfortable with the command line interface (CLI), you can use `auto-py-to-exe` to convert the Python script into an executable with a user-friendly interface.

1. Install `auto-py-to-exe`:
   ```bash
   pip install auto-py-to-exe
   ```
2. Launch `auto-py-to-exe`:
   ```bash
   auto-py-to-exe
   ```
3. A graphical interface will appear, allowing you to:
   - Set the icon for your executable
   - Specify the name of the executable
   - Configure additional settings

4. Follow the instructions in the interface to create your executable file.

## Log Files

- `log.txt`: Contains the raw log of keystrokes.
- `cleaned_log.txt`: Contains the cleaned log with unnecessary key strokes removed.

## Code Explanation

- **KeyLogger Class**: Main class to handle logging functionality.
  - `append_to_log(key_strike)`: Appends keystrokes to the log file and cleans it.
  - `evaluate_keys(key)`: Processes each key press and detects if `F1` and `F2` are pressed together.
  - `clean_log(file_path)`: Cleans the log file by removing unnecessary key strokes.
  - `start()`: Starts the keylogger and listens for key presses.

## Contributing

Feel free to contribute to the project by submitting issues, suggestions, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Please use this keylogger responsibly and only for educational purposes or with explicit permission. Unauthorized use of keyloggers is illegal and unethical.
