# Basic Network Sniffer - Testing Report

**Project:** Basic Network Sniffer
**Testing period:** November 11–13, 2026
**Environment:** Windows 11, Python 3.11.9, Scapy 2.8.0, Npcap

## 1. Testing Overview

The application was tested through live network captures, controlled network traffic, CSV inspection, command-line validation and automated unit tests.

Testing covered packet capture, protocol identification, metadata extraction, filtering, logging, statistics, invalid inputs and exception handling.

## 2. Live Functional Testing

| Test ID | Test Description | Actual Result | Status |
|---|---|---|---|
| T01 | Live packet capture | Approximately 1,455 packets processed in an initial capture | PASS |
| T02 | Packet-count limit | Exactly 20 packets processed | PASS |
| T03 | TCP identification | TCP correctly identified | PASS |
| T04 | UDP identification | UDP correctly identified | PASS |
| T05 | ICMP identification | Echo Request and Echo Reply identified | PASS |
| T06 | ARP identification | ARP traffic observed and identified | PASS |
| T07 | Port extraction | TCP and UDP ports extracted | PASS |
| T08 | TCP flag extraction | Flags such as A, PA and S identified | PASS |
| T09 | CSV logging | Metadata successfully written to CSV | PASS |
| T10 | TCP filtering | 10 TCP packets captured | PASS |
| T11 | UDP filtering | 16 UDP packets captured | PASS |
| T12 | Combined ICMP and IP filtering | 10 matching ICMP packets involving 1.1.1.1 | PASS |
| T13 | Final TCP regression | Exactly five TCP packets processed | PASS |

## 3. CSV Logging Verification

The following CSV outputs were inspected:

- General capture: 30 records
- TCP capture: 10 records
- ICMP capture: 10 records
- UDP capture: 16 records

The CSV files contained timestamp, protocol, source IP, destination IP, source port, destination port, TCP flags, source MAC and destination MAC.

The ICMP CSV validation found zero records unrelated to the specified IPv4 address.

### Day 4 CSV Verification

| CSV File | Records Verified | Result |
|---|---:|---|
| `day4_integration_test.csv` | 10 TCP records | PASS |
| `day4_icmp_filter_test.csv` | 8 ICMP records | PASS |
| `day4_timeout_verified.csv` | 379 records | PASS |
| `day4_append_test.csv` | 5 records across two captures | PASS |

Additional CSV validation:

- Verified all nine expected metadata columns in the general capture CSV.
- Confirmed that no payload column was present.
- Confirmed that all eight filtered ICMP records involved 1.1.1.1.
- Found zero unexpected IP records in the filtered CSV.
- Confirmed that the timeout capture summary and CSV both contained 379 records.
- Verified that two consecutive captures produced five records with one CSV header.
- Confirmed that CSV logging uses append mode and does not duplicate the header.

## 4. Automated Unit Testing

Automated tests were implemented in `tests/test_sniffer.py` using Python's `unittest` framework.

| Test ID | Test Description | Result |
|---|---|---|
| U01 | TCP packet metadata extraction | PASS |
| U02 | UDP packet metadata extraction | PASS |
| U03 | ICMP packet metadata extraction | PASS |
| U04 | ARP packet metadata extraction | PASS |
| U05 | IGMP identification | PASS |
| U06 | Payload absence from extracted metadata | PASS |

**Final automated test result: 6/6 PASSED**

The six tests were executed again after the network interface error-handling correction. All six passed.

## 5. Error Handling and Input Validation

| Test ID | Scenario | Expected Behaviour | Result |
|---|---|---|---|
| E01 | Missing interface argument | Reject command with exit code 2 | PASS |
| E02 | Negative packet count | Reject invalid value with exit code 2 | PASS |
| E03 | Count and timeout both zero | Reject unlimited capture with exit code 2 | PASS |
| E04 | Unknown interface index | Display clean error with exit code 2 | PASS |
| E05 | Invalid CSV output destination | Display capture error with exit code 1 | PASS |
| E06 | Unsupported protocol GRE | Reject unsupported protocol | PASS |
| E07 | Invalid IPv4 address | Reject invalid address | PASS |

The unknown interface test initially exposed an unhandled `ValueError` from Scapy's interface lookup. This was corrected by catching the exception and reporting a clean command-line error.

The corrected implementation was retested successfully.

## 6. Privacy and Security Checks

- Packet payload contents are not intentionally displayed or written to the CSV logs. The application records packet metadata only.
- Extracted metadata is written to CSV.
- Local packet capture logs are excluded from Git version control.
- Screenshots containing actual network addresses should be redacted before public release.

The automated payload test verifies that the metadata returned by `process_packet()` does not contain a payload field or the synthetic test payload string.

## 7. Additional Tests Recommended

The following tests remain recommended:

- Dedicated automated tests for ARP filtering.
- Additional output-file and directory permission scenarios.
- Interface availability and capture initialization failure scenarios.
- Dedicated automated unit tests for CSV writer behaviour.
- Broader regression testing of all supported capture options.

## 8. Day 4 Integration Testing

Additional manual integration testing was performed on November 13, 2026, using the MediaTek Wi-Fi 6 MT7921 wireless adapter.

| Test ID | Test Description | Actual Result | Status |
|---|---|---|---|
| T14 | Live capture with a 10-packet limit | Exactly 10 TCP packets captured | PASS |
| T15 | General capture CSV integrity | 10 records, nine metadata columns, no payload column | PASS |
| T16 | Combined ICMP and IPv4 BPF filtering | Exactly 8 matching ICMP packets captured | PASS |
| T17 | Filtered CSV validation | 8 ICMP records, all involving 1.1.1.1, zero unrelated IP records | PASS |
| T18 | Five-second timeout capture | 379 packets processed with count limit disabled | PASS |
| T19 | Timeout CSV and timestamp verification | 379 CSV records; observed timestamp span of 5.0 seconds | PASS |
| T20 | CSV append-mode verification | Two captures produced 5 records with one header | PASS |

### Timeout Testing Details

The timeout test was executed using:

```powershell
python src/sniffer.py --iface-index 19 --count 0 --timeout 5 --log-file logs/day4_timeout_verified.csv
```

The packet-count limit was disabled so that the timeout was the automatic stopping condition.

Results:

- Total packets processed: 379
- TCP: 371
- UDP: 6
- ARP: 2
- CSV records: 379
- First packet timestamp: 15:34:30
- Last packet timestamp: 15:34:35
- Observed timestamp span: 5.0 seconds

Note: Packet timestamps are recorded at one-second precision. The observed timestamp span is therefore an approximate validation of the configured timeout, not a millisecond-precision measurement of the capture duration.

### CSV Append-Mode Testing

Two consecutive captures were performed using the same output file:

- First capture: 2 packets.
- Second capture: 3 packets.
- Final CSV data records: 5.
- Header rows: 1.

The test confirmed that the application appends new packet metadata to an existing CSV file without duplicating its header.

## 9. Conclusion

The Basic Network Sniffer has successfully demonstrated live network packet capture, protocol identification, metadata extraction, protocol and IPv4 filtering, CSV logging and protocol statistics.

Six automated packet-analysis tests passed. Seven error-handling and input-validation scenarios were verified. Additional manual integration tests on November 13, 2026, verified live capture limits, combined filtering, CSV integrity, timeout-based capture and CSV append behaviour.

The application has passed its current functional and initial quality-assurance tests. Additional automated regression and edge-case testing is recommended before final project submission.
