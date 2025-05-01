# Windows Event Log Parser for Threat Detection

This Python script parses Windows Event Logs (`.evtx` files) and detects potential threats based on event IDs and data.

## Requirements

- Python 3.x
- `Evtx`, `pandas` (Install dependencies using `pip install -r requirements.txt`)

## Setup

1. Clone this repository.
    ```bash
    git clone https://github.com/your-username/windows-event-log-parser.git
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Export Windows Event Logs (`.evtx` files) from the Windows Event Viewer.
2. Run the script:
    ```bash
    python3 log_parser.py path_to_log_file.evtx
    ```

## Threat Detection

The script detects the following suspicious events:
- **4625**: Failed login attempts.
- **4647**: User logoff.

## License

This project is licensed under the MIT License.
