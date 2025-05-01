# Windows Event Log Parser for Threat Detection

This Python script parses and analyzes Windows Event Logs to assist in threat detection and system monitoring. The tool helps identify potential security threats by extracting and analyzing relevant event log entries. It supports custom filters, and allows you to easily search and classify events based on various attributes like event IDs, sources, and levels.

## Features
- Parses Windows Event Logs (`.evtx` files)
- Supports searching by Event ID, Event Level, and Source
- Flexible filtering options for better analysis
- Option to save output as CSV or JSON for easier reporting

## Requirements

- Python 3.x
- `Evtx`, `pandas` (Install dependencies using `pip install -r requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PaxtonTabat/windows-event-log-parser.git

2. Navigate to the project directory:
   cd windows-event-log-parser

3. Install the dependencies:
   pip install -r requirements.txt

4. Run the script:
   python main.py

## Usage

1. Export Windows Event Logs (`.evtx` files) from the Windows Event Viewer.

2. You can parse an Event Log file with a command like:
```bash
python main.py --input "path_to_event_log.evtx" --output "output.csv"

3. Run the script:
    ```bash
    python3 log_parser.py path_to_log_file.evtx
    ```

## Threat Detection

The script detects the following suspicious events:
- **4625**: Failed login attempts.
- **4647**: User logoff.

## License

This project is licensed under the MIT License.
