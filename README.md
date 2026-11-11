# Basic Network Sniffer

A Python-based network packet sniffer developed using **Scapy** and **Npcap** as part of the CodeAlpha Cyber Security Internship.

The application captures live network traffic from a selected interface, extracts packet metadata, applies protocol and IPv4 filtering, and saves captured metadata to CSV files.

## Features

- Live packet capture through a selected network interface.
- Source and destination IPv4 address extraction.
- Protocol identification: TCP, UDP, ICMP, ARP and IGMP.
- TCP and UDP source/destination port extraction.
- TCP flag identification.
- Protocol-based packet filtering.
- IPv4 address-based packet filtering.
- Configurable packet capture count and timeout.
- CSV logging of packet metadata.
- Protocol distribution statistics.
- Command-line argument validation.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Application development |
| Scapy 2.8.0 | Packet capture and analysis |
| Npcap | Windows packet capture support |
| CSV | Packet metadata storage |
| Git and GitHub | Version control |

## Project Structure

```text
CodeAlpha_BasicNetworkSniffer/
│
├── src/
│   └── sniffer.py
│
├── docs/
│   ├── research.md
│   ├── architecture.md
│   └── testing_report.md
│
├── logs/                   # Local logs; excluded from Git
├── screenshots/            # Project evidence
├── tests/                  # Automated tests (planned)
│
├── .gitignore
├── DAILY_LOG.md
├── README.md
└── requirements.txt
```

## Installation and Setup

### Prerequisites

- Windows 10 or Windows 11
- Python 3.11
- Npcap installed and running
- Git
- Appropriate permissions to capture traffic

### 1. Clone the repository

```powershell
git clone https://github.com/shettysanket06/CodeAlpha_BasicNetworkSniffer.git
cd CodeAlpha_BasicNetworkSniffer
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

Ensure Npcap is installed separately and its packet capture service is running.

## Usage

The application requires an explicit network interface index.

### Basic packet capture

```powershell
python .\src\sniffer.py --iface-index 19 --count 20 --timeout 30
```

### Capture only TCP packets

```powershell
python .\src\sniffer.py --iface-index 19 --protocol TCP --count 20 --timeout 30
```

### Capture only UDP packets

```powershell
python .\src\sniffer.py --iface-index 19 --protocol UDP --count 20 --timeout 30
```

### Filter traffic by IPv4 address

```powershell
python .\src\sniffer.py --iface-index 19 --ip 1.1.1.1 --count 0 --timeout 15
```

### Combine protocol and IP filters

```powershell
python .\src\sniffer.py --iface-index 19 --protocol ICMP --ip 1.1.1.1 --count 0 --timeout 15
```

### Save output to a custom CSV file

```powershell
python .\src\sniffer.py --iface-index 19 --protocol TCP --count 10 --timeout 30 --log-file logs/tcp_test.csv
```

### Command-line arguments

| Argument | Description |
|---|---|
| `--iface-index` | Scapy network interface index (required) |
| `--count` | Maximum number of packets; 0 means unlimited |
| `--timeout` | Maximum capture duration in seconds; 0 means unlimited |
| `--protocol` | Filter by TCP, UDP, ICMP, ARP or IGMP |
| `--ip` | Filter by source or destination IPv4 address |
| `--log-file` | CSV output file path |

At least one capture stopping condition must be configured: packet count or timeout.

Use `--help` to view available options.

## CSV Output

The application records the following metadata:

- Timestamp
- Protocol
- Source IP
- Destination IP
- Source port
- Destination port
- TCP flags
- Source MAC
- Destination MAC

Packet payload contents are not displayed or stored by default.

## Testing and Validation

Manual functional testing performed so far includes:

| Test | Result |
|---|---|
| Live packet capture | Passed |
| TCP identification and filtering | Passed |
| UDP identification and filtering | Passed |
| ICMP identification and filtering | Passed |
| ARP identification | Observed successfully |
| Packet-count limit | Passed |
| CSV metadata logging | Passed |
| Combined ICMP and IPv4 filtering | Passed |
| Invalid protocol validation | Passed |
| Invalid IPv4 validation | Passed |
| Protocol distribution statistics | Verified in captures |

Automated unit testing is planned.

Detailed test results will be documented in `docs/testing_report.md`.

## Security and Privacy

- Capture only traffic on systems and networks where authorization has been granted.
- Packet payload contents are not stored by default.
- CSV logs may contain sensitive IP and MAC addresses.
- Local capture logs are excluded from version control.
- Do not publish sensitive network information or unredacted packet evidence.

## Project Status

This is an educational cybersecurity project developed to demonstrate practical networking, packet analysis, Python programming and basic network monitoring concepts.

## Author

Developed as part of the CodeAlpha Cyber Security Internship.

GitHub: [shettysanket06](https://github.com/shettysanket06)