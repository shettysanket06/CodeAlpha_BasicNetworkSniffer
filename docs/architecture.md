# Basic Network Sniffer — System Architecture

## 1. Overview

The Basic Network Sniffer is a Python-based application developed using Scapy. It captures live network packets from a selected interface, extracts packet metadata, applies capture filters and records metadata in CSV format.

On Windows, Npcap provides the packet capture support used by Scapy.

## 2. System Architecture

The application consists of the following components:

1. Command-Line Interface
2. Network Interface Selection
3. Packet Capture Engine
4. BPF Filtering
5. Packet Analyzer
6. CSV Logging Module
7. Protocol Statistics Module

## 3. Application Workflow

### 3.1 Command-Line Interface

The application accepts user-configured parameters through Python argparse.

Supported arguments:

- Interface index
- Packet capture count
- Capture timeout
- Protocol filter
- IPv4 address filter
- CSV output path

The interface index is mandatory.

### 3.2 Network Interface Selection

Scapy's interface configuration is used to retrieve the selected network interface.

The application uses the selected interface for live packet capture.

### 3.3 Packet Capture Engine

Scapy's sniff() function captures packets from the selected interface.

Important parameters:

- iface: selected network interface
- filter: optional BPF capture filter
- prn: packet-processing callback
- count: maximum packet count
- timeout: maximum capture duration
- store=False: prevents retaining captured packets in Scapy's result list

### 3.4 BPF Filtering Module

The application constructs a capture filter based on user input.

Supported protocol filters:

- TCP
- UDP
- ICMP
- ARP
- IGMP

IPv4 address filtering uses the host expression.

When both filters are supplied, the application combines them using the AND operator.

Example:

    icmp and host 1.1.1.1

### 3.5 Packet Analyzer

The process_packet() function extracts packet metadata.

Supported information:

- Timestamp
- Protocol
- Source IPv4 address
- Destination IPv4 address
- Source port
- Destination port
- TCP flags
- Source MAC address
- Destination MAC address

The analyzer handles TCP, UDP, ICMP, ARP and IGMP identification.

Port information is not applicable to ARP or ICMP packets.

### 3.6 Display Module

The display_packet() function prints extracted metadata to the terminal.

No packet payload contents are displayed.

### 3.7 CSV Logging Module

The application uses Python's csv.DictWriter to save metadata records.

The logging module:

- Creates the output directory when required.
- Creates the CSV header for a new file.
- Appends records to an existing CSV file.
- Flushes records to the file during capture.

Packet payload contents are not stored.

### 3.8 Protocol Statistics Module

Python's collections.Counter maintains packet counts by protocol.

A capture summary is displayed after capture completion.

## 4. Technology Stack

- Python 3.11
- Scapy 2.8.0
- Npcap
- argparse
- csv
- pathlib
- collections.Counter
- Git and GitHub
- Windows 11

## 5. Data Flow

The user provides capture parameters through the command-line interface.

The application identifies the selected network interface and constructs the appropriate BPF filter.

Scapy captures matching packets and passes each packet to the callback function.

The packet analyzer extracts available metadata.

The display module prints the extracted information.

The CSV logging module saves the metadata.

The statistics module updates protocol counts and generates the final capture summary.

## 6. Security and Privacy Considerations

- Capture only traffic for which authorization has been granted.
- Packet payload contents are not displayed or stored by default.
- Packet logs may contain sensitive IP and MAC addresses.
- Local logs are excluded from Git version control.
- The interface must be explicitly selected.
- Capture errors and invalid command-line arguments should be handled safely.

## 7. Current Implementation Status

| Component | Status |
|---|---|
| Command-line interface | Implemented |
| Network interface selection | Implemented |
| Live packet capture | Implemented |
| BPF protocol filtering | Implemented |
| IPv4 address filtering | Implemented |
| Packet metadata extraction | Implemented |
| Terminal output | Implemented |
| CSV metadata logging | Implemented |
| Protocol statistics | Implemented |
| Manual functional testing | Performed |
| Automated unit testing | Pending |

## 8. Known Limitations

- The current packet analyzer focuses on IPv4 traffic and Ethernet metadata.
- The interface index may change between system configurations.
- The application does not decrypt HTTPS traffic.
- Automated unit tests and additional edge-case tests are pending.

## 9. Conclusion

The current implementation demonstrates practical packet capture, protocol identification, metadata extraction, filtering, CSV logging and basic traffic statistics using Python and Scapy.