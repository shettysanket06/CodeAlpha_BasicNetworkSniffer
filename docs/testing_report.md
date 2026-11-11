# Basic Network Sniffer — Testing Report

**Project:** Basic Network Sniffer
**Testing date:** November 11, 2026
**Environment:** Windows 11, Python 3.11.9, Scapy 2.8.0, Npcap

## 1. Testing Overview

Functional testing was performed using live network traffic on the selected Wi-Fi interface and controlled traffic generated through ping and DNS queries.

The tests focused on packet capture, protocol identification, metadata extraction, filtering, CSV logging, capture limits and command-line input validation.

## 2. Test Results

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| T01 | Live packet capture | Capture and display packets | Live packets captured successfully | PASS |
| T02 | Packet-count limit | Stop after 20 packets | Exactly 20 packets processed | PASS |
| T03 | TCP identification | Identify TCP traffic | TCP correctly identified | PASS |
| T04 | UDP identification | Identify UDP traffic | UDP correctly identified | PASS |
| T05 | ICMP identification | Identify ICMP traffic | Echo Request and Echo Reply identified | PASS |
| T06 | ARP identification | Identify ARP traffic | ARP packets observed and identified | PASS |
| T07 | Port extraction | Extract TCP/UDP ports | Port values displayed correctly | PASS |
| T08 | TCP flag extraction | Identify TCP flags | Flags such as A, PA and S displayed | PASS |
| T09 | CSV logging | Save packet metadata | CSV file created and records imported successfully | PASS |
| T10 | TCP filtering | Capture only TCP | 10 TCP packets captured | PASS |
| T11 | UDP filtering | Capture only UDP | 16 UDP packets captured | PASS |
| T12 | ICMP and IP filtering | Capture matching ICMP traffic involving 1.1.1.1 | 10 matching packets captured | PASS |
| T13 | CSV protocol verification | Confirm saved protocol values | TCP, UDP and ICMP records verified | PASS |
| T14 | Invalid protocol input | Reject unsupported protocol GRE | Argument validation rejected GRE | PASS |
| T15 | Invalid IPv4 input | Reject invalid IP address | Argument validation rejected invalid IP | PASS |
| T16 | Final TCP regression | Capture five TCP packets | Exactly five TCP packets processed | PASS |
| T17 | Explicit interface argument | Require interface selection | Help output showed interface argument as required | PASS |

## 3. CSV Logging Verification

The following CSV outputs were inspected:

- General packet capture: 30 records
- TCP-filtered capture: 10 records
- ICMP-filtered capture: 10 records
- UDP-filtered capture: 16 records

The records contained the expected metadata fields:

- Timestamp
- Protocol
- Source IP
- Destination IP
- Source port
- Destination port
- TCP flags
- Source MAC
- Destination MAC

The ICMP CSV verification found zero records unrelated to the specified IPv4 address.

## 4. Additional Observations

- An initial timed capture processed 1,455 packets.
- UDP traffic included DNS traffic on port 53 and SSDP traffic on port 1900.
- TCP traffic included connections using port 443.
- No packet payload contents were intentionally displayed or stored by the application.

## 5. Tests Pending

The following tests have not yet been completed:

- Automated unit tests for TCP, UDP, ICMP, ARP and IGMP packet analysis.
- Dedicated IGMP identification test.
- Dedicated ARP filtering test.
- Runtime capture-failure exit-code verification.
- Additional invalid interface and output-file error tests.

These are planned for the next quality-assurance session.

## 6. Conclusion

The application has successfully demonstrated live network packet capture, metadata extraction, TCP/UDP/ICMP/ARP identification, protocol and IPv4 filtering, CSV logging, protocol statistics and command-line argument validation.

Further automated testing and edge-case validation are required before final project submission.
