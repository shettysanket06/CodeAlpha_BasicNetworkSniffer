# Development Log — Basic Network Sniffer

## Day 1 — November 10, 2026

### Objectives
- Configure the Python development environment.
- Install and verify Scapy.
- Understand network packet fundamentals.
- Research packet capture and networking protocols.
- Document the project architecture.
- Initialize GitHub version control.

### Completed
- [x] Verified Python 3.11.9.
- [x] Created and activated Python virtual environment.
- [x] Installed Scapy 2.8.0.
- [x] Verified required Scapy imports.
- [x] Created project directory structure.
- [x] Prepared network research documentation.
- [x] Created initial system architecture documentation.
- [x] Initialized local Git repository.
- [x] Created `.gitignore` and excluded `.venv/`.
- [x] Created GitHub repository.
- [x] Committed and pushed initial research documentation.

### Challenges
- Python launcher (`py`) unavailable; used `python` successfully.
- Project initially created in Windows System32; relocated to Documents.
- Markdown formatting and encoding issues encountered while using Notepad; resolved by editing in VS Code.

### Technical Learning
- Ethernet and IPv4 packet structure.
- TCP, UDP and ICMP fundamentals.
- Scapy packet capture capabilities.
- Npcap's role in Windows packet capture.
- Basic Git initialization, staging, committing and pushing.

### Pending
- Final review and commit of architecture documentation.
- Implement live packet capture engine.
- Implement packet analysis and display.
- Implement filtering, logging and statistics.

### Next Session — November 11
- Finalize and push Day 1 documentation.
- Implement the initial Scapy capture engine.
- Test packet capture on an authorized network interface.

### Status
Environment setup: Complete
Research documentation: Committed and pushed
Architecture documentation: Draft created, pending review and commit
GitHub repository: Created and connected
Packet capture engine: Not started



---

## Day 2 — November 11, 2026

### Objectives
- Identify the active network interface.
- Verify live packet capture using Scapy and Npcap.
- Implement the packet capture engine.
- Extract packet metadata.
- Implement protocol and IPv4 filtering.
- Implement CSV logging and protocol statistics.
- Perform functional testing.

### Completed

- [x] Verified Python virtual environment and Scapy installation.
- [x] Verified Npcap service was running.
- [x] Identified the active MediaTek Wi-Fi interface.
- [x] Successfully captured live network packets.
- [x] Implemented the Scapy-based packet capture engine.
- [x] Extracted source and destination IP addresses.
- [x] Identified TCP, UDP, ICMP, ARP and IGMP traffic.
- [x] Extracted TCP/UDP port information.
- [x] Implemented TCP flag identification.
- [x] Implemented configurable packet-count and timeout controls.
- [x] Implemented protocol-based filtering.
- [x] Implemented IPv4 address-based filtering.
- [x] Implemented CSV metadata logging.
- [x] Implemented protocol distribution statistics.
- [x] Added command-line input validation.
- [x] Added an explicit interface-selection requirement.
- [x] Excluded local packet logs from Git version control.

### Testing Performed

- Captured more than 1,400 live packets in an initial capture session.
- Verified a 20-packet capture limit.
- Verified ICMP Echo Request and Echo Reply identification.
- Verified CSV logging with 30 packet records.
- Verified TCP filtering with 10 TCP records.
- Verified combined ICMP and IPv4 filtering with 10 matching records.
- Verified that zero unrelated IP records were present in the ICMP CSV.
- Verified UDP filtering with 16 UDP records.
- Verified rejection of an unsupported protocol.
- Verified rejection of an invalid IPv4 address.
- Verified a final TCP regression capture with five packets.

### Problems Encountered

- VS Code initially opened Command Prompt instead of PowerShell.
- The Python virtual environment was not initially active in the terminal.
- Encountered Windows file permission issues while creating the source file.
- Identified and corrected the Markdown editing workflow by switching from Notepad to VS Code.
- Discovered that the network interface index should be explicitly selected rather than assumed.

### Skills and Knowledge Acquired

- Practical use of Scapy's `sniff()` function.
- Network interface discovery and selection.
- Packet processing using Scapy layers.
- TCP, UDP, ICMP, ARP and IGMP identification.
- Berkeley Packet Filter (BPF) capture filters.
- Python CSV logging.
- Command-line argument validation using argparse.
- Protocol statistics using collections.Counter.
- Git staging, commits and repository hygiene.

### Evidence Produced

- Live packet capture output.
- Successful 20-packet capture test.
- ICMP request/reply capture output.
- TCP filtering output.
- UDP filtering output.
- CSV metadata files.
- Verified CSV records and protocol distributions.
- Invalid protocol and IPv4 input validation output.
- Final regression test output.

### Pending

- Automated unit tests for packet analysis.
- Further edge-case and error-handling tests.
- Final README and architecture documentation review.
- Redacted evidence organization.
- Day 2 GitHub commit and push.

### Next Session — November 12

- Implement automated packet-analysis tests.
- Validate error handling and edge cases.
- Review source code.
- Finalize technical documentation.
- Organize project evidence and prepare the next development milestone.

### Status

Environment: Verified

Live packet capture: Implemented and tested

Packet analysis: Implemented and manually tested

Filtering: Implemented and manually tested

CSV logging: Implemented and tested

Statistics: Implemented and observed in tests

Automated testing: Pending

GitHub Day 2 submission: Pending

Focused work duration: To be recorded accurately at session close
---

## Day 3 - November 12, 2026

### Objectives
- Implement automated unit tests for packet analysis.
- Validate application error handling.
- Identify and fix issues in network interface selection.
- Perform regression testing after code corrections.
- Improve application reliability.

### Completed

- [x] Inspected the GitHub repository and verified tracked project files.
- [x] Created the automated test suite at tests/test_sniffer.py.
- [x] Implemented six automated unit tests using Python unittest.
- [x] Tested TCP packet analysis.
- [x] Tested UDP packet analysis.
- [x] Tested ICMP packet analysis.
- [x] Tested ARP packet analysis.
- [x] Tested IGMP identification.
- [x] Tested that packet payload contents are not included in extracted metadata.
- [x] Successfully executed all six automated tests.
- [x] Tested rejection of a missing network interface argument.
- [x] Tested rejection of negative packet counts.
- [x] Tested rejection of unlimited capture when both count and timeout are zero.
- [x] Identified an unhandled ValueError when an invalid network interface index was supplied.
- [x] Corrected invalid network interface handling.
- [x] Verified that an invalid interface now produces a clean command-line error.
- [x] Tested invalid CSV output destination handling.
- [x] Verified non-zero exit codes for application errors.
- [x] Re-ran all six automated unit tests after the source-code correction.
- [x] Performed a five-packet TCP regression capture.
- [x] Verified Python syntax compilation.

### Testing Results

Automated unit tests: 6/6 PASSED

Error-handling scenarios: 5/5 PASSED

Updated-source regression capture: PASSED

Python compilation: PASSED

### Problems Encountered

- Scapy raised a ValueError when an unknown network interface index was supplied instead of returning a missing interface object.
- The original implementation did not handle this exception, resulting in an unhandled traceback.
- Corrected the issue by catching ValueError and reporting the invalid interface through argparse.
- Initial testing demonstrated the importance of checking application exit codes and verifying error handling separately from normal packet capture.

### Skills and Knowledge Acquired

- Learned to create automated unit tests using Python's unittest framework.
- Practised constructing synthetic network packets using Scapy.
- Improved understanding of TCP, UDP, ICMP, ARP and IGMP packet structures.
- Learned to use assertions to validate extracted packet metadata.
- Understood the difference between unit testing and live network integration testing.
- Improved exception handling in Python applications.
- Learned to handle Scapy network interface lookup errors.
- Practised validating command-line application exit codes.
- Performed regression testing after modifying application source code.
- Improved debugging and software quality-assurance skills.

### Evidence Produced

- Created tests/test_sniffer.py containing six automated unit tests.
- Successfully executed all six tests with Python unittest.
- Recorded successful TCP, UDP, ICMP, ARP and IGMP packet analysis tests.
- Recorded successful payload metadata privacy test.
- Captured invalid interface error output after correcting the exception handling.
- Verified rejection of missing interface, negative packet count and unlimited capture arguments.
- Verified invalid CSV output destination handling with exit code 1.
- Verified invalid interface handling with exit code 2.
- Successfully compiled the updated sniffer.py file.
- Successfully performed a final TCP capture processing exactly five packets.

### Pending

- Additional regression testing for ARP filtering and CSV edge cases.
- Final source-code review.
- Final documentation and README review.
- Organize and redact project evidence screenshots.
- Commit and push the latest Day 3 source code, automated tests and documentation updates.
- Prepare the CodeAlpha project demonstration and submission.

### Next Session

- Complete remaining regression tests.
- Review source-code quality and edge cases.
- Finalize project documentation.
- Verify the GitHub repository and submission evidence.

### Status

Automated unit testing: Complete - 6/6 passed

Error handling: Complete - 5/5 scenarios passed

Invalid interface handling: Corrected and verified

Regression testing: Partially complete

Documentation: Updated work pending verification

GitHub Day 3 commit: Pending

Focused working hours: To be recorded from the actual timesheet.


---

# Day 4 — November 13, 2026

## Objectives

- Perform live integration testing of the Basic Network Sniffer.
- Verify CSV output integrity.
- Validate combined protocol and IPv4 filtering.
- Test timeout-based capture.
- Inspect CSV append-mode behaviour.
- Improve project documentation.

## Completed

- [x] Verified Python 3.11.9 and the active virtual environment.
- [x] Verified that the Git working tree was clean at the beginning of Day 4.
- [x] Re-executed all six automated unit tests successfully.
- [x] Verified the Scapy network interface list.
- [x] Identified the MediaTek Wi-Fi 6 MT7921 adapter at interface index 19.
- [x] Captured exactly 10 packets in a live capture.
- [x] Verified the general capture CSV contained exactly 10 records.
- [x] Verified the nine expected CSV metadata columns.
- [x] Confirmed that the CSV did not contain a payload column.
- [x] Captured eight ICMP packets using combined ICMP and IPv4 filtering.
- [x] Verified that all eight filtered CSV records involved 1.1.1.1.
- [x] Confirmed zero unexpected IP records in the filtered CSV.
- [x] Performed a corrected five-second timeout capture with the packet-count limit disabled.
- [x] Captured 379 packets during the timeout test.
- [x] Verified the protocol distribution: 371 TCP, 6 UDP and 2 ARP.
- [x] Confirmed that the timeout CSV contained 379 records.
- [x] Verified an observed timestamp span of 5.0 seconds.
- [x] Inspected the CSV logging implementation and confirmed append mode.
- [x] Verified that the CSV header is written only when the file is empty.
- [x] Performed two consecutive captures using the same CSV file: 2 packets followed by 3 packets.
- [x] Verified five final CSV records and exactly one header.
- [x] Updated the README project structure.
- [x] Documented CSV append behaviour and manual versus automated testing.
- [x] Reviewed the README changes using git diff and git diff --check.

## Testing Results

Automated unit tests: 6/6 PASSED

Live 10-packet capture: PASSED

General CSV integrity: PASSED

Combined ICMP and IPv4 filtering: PASSED

Filtered CSV verification: PASSED

Five-second timeout capture: PASSED

Timeout CSV verification: PASSED

CSV append-mode and header verification: PASSED

## Problems Encountered

- The initial timeout command omitted the explicit --count 0 argument, leaving the default packet-count limit active.
- A previous CSV file contained records from multiple capture runs because the application uses append mode.
- The timeout test was corrected by disabling the packet-count limit and using a fresh CSV filename.
- Source-code inspection confirmed that append mode and conditional header creation were intentional and functioning correctly.
- No source-code changes were required during Day 4.

## Skills and Knowledge Acquired

- Practised live packet capture and integration testing.
- Verified packet metadata through independent CSV inspection.
- Tested combined Berkeley Packet Filter expressions.
- Understood the interaction between packet-count limits and capture timeouts.
- Learned how to validate capture duration using packet timestamps.
- Inspected Python CSV append-mode behaviour.
- Verified conditional CSV header creation.
- Improved understanding of manual integration testing versus automated unit testing.
- Improved technical documentation and test-report writing.

## Evidence Produced

- logs/day4_integration_test.csv
- logs/day4_icmp_filter_test.csv
- logs/day4_timeout_verified.csv
- logs/day4_append_test.csv
- Updated README.md
- Updated docs/testing_report.md

All generated CSV files contain real network metadata and remain local. They must not be uploaded publicly without appropriate redaction.

## Pending

- Final source-code review.
- Final documentation review.
- Organize and redact demonstration screenshots.
- Inspect the final Git diff.
- Commit and push the Day 4 documentation updates.
- Prepare the CodeAlpha project demonstration and submission.

## Working Hours

Start time: To be recorded
End time: To be recorded
Break duration: To be recorded
Actual focused working hours: To be calculated from the actual timesheet.

## Status

Day 4 integration testing: Complete

CSV verification: Complete

Timeout testing: Complete

CSV append-mode verification: Complete

README update: Completed locally

Testing report and daily log: Updated locally; pending final verification and GitHub push.
