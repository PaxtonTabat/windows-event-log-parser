import Evtx.Evtx as evtx
import xml.etree.ElementTree as ET

def parse_event_log(file_path):
    """Parse a Windows event log (.evtx) file."""
    try:
        with evtx.Evtx(file_path) as log:
            for record in log.records():
                xml_tree = ET.ElementTree(ET.fromstring(record.xml()))  # Parse each record as XML
                for event in xml_tree.iter("Event"):  # Loop through each event in the log
                    event_id = event.find("System/EventID").text  # Extract Event ID
                    event_data = event.find("EventData/Data").text  # Extract Event Data
                    print(f"Event ID: {event_id}, Data: {event_data}")
                    check_for_threats(event_id, event_data)  # Detect threats in the event log
    except Exception as e:
        print(f"Failed to parse log file: {e}")

def check_for_threats(event_id, event_data):
    """Check if the event data matches any known threat pattern."""
    # Add more threat patterns here based on your needs
    suspicious_ids = ['4625', '4647']  # For example: failed logon attempts, user logoff events
    if event_id in suspicious_ids:
        print(f"** Threat Detected! ** Event ID: {event_id}, Data: {event_data}")
        
if __name__ == "__main__":
    log_file_path = "path_to_your_evtx_file.evtx"  # Replace with the actual path to your .evtx file
    parse_event_log(log_file_path)
