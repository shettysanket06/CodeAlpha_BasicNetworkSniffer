\# Basic Network Sniffer - System Architecture



\## 1. Overview



The Basic Network Sniffer is a Python-based application that captures and analyzes network packets using the Scapy library. On Windows, Npcap provides the packet capture support required by Scapy.



\## 2. System Workflow



The application follows this processing flow:



1\. Network Interface Selection

2\. Packet Capture using Scapy

3\. Packet Dissection and Analysis

4\. Protocol and IP Filtering

5\. Terminal Output

6\. Metadata Logging

7\. Packet Statistics



\## 3. Main Components



\### 3.1 Network Interface



The user selects the network interface from which authorized traffic will be captured.



\### 3.2 Packet Capture Engine



Scapy captures packets from the selected interface. The capture engine receives packets and passes them to the packet processing function.



\### 3.3 Packet Analyzer



The analyzer examines each captured packet and extracts relevant information:



\- Source IP address

\- Destination IP address

\- Protocol

\- Source port

\- Destination port

\- TCP flags



Not every packet contains every field. For example, ICMP packets do not have TCP or UDP ports.



\### 3.4 Filtering Module



The filtering module allows users to narrow packet output based on supported criteria, such as protocol and IP address.



\### 3.5 Output and Logging



The application displays packet metadata in the terminal and saves relevant metadata to a log file.



Packet payload contents will not be stored by default.



\### 3.6 Statistics Module



The statistics module maintains packet counts and summarizes captured traffic by protocol.



\## 4. Technology Stack



\- Programming Language: Python 3.11

\- Packet Manipulation and Capture: Scapy

\- Windows Packet Capture Support: Npcap

\- Development Environment: Windows 11

\- Version Control: Git and GitHub



\## 5. Data Flow



The user selects an interface and starts packet capture. Scapy receives packets through the supported capture mechanism. The packet analyzer extracts available metadata, applies configured filters, and sends the results to terminal output and the logging module. The statistics module maintains counts for the captured packets.



\## 6. Security Considerations



\- Capture only traffic for which authorization has been obtained.

\- Avoid collecting packet payload contents by default.

\- Do not publish sensitive traffic data.

\- Validate user-provided filtering options.

\- Handle capture errors and unavailable interfaces safely.



\## 7. Current Implementation Status



Architecture documentation: Initial design



Packet capture engine: Not implemented



Packet analyzer: Not implemented



Filtering: Not implemented



Logging: Not implemented



Statistics: Not implemented

