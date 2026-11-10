\# Basic Network Sniffer — Research



\## 1. Introduction



\### What is a network sniffer?

A network sniffer is a tool that captures and analyzes network packets transmitted through a network interface. It helps users inspect communication between devices and understand network activity.



\### Why is packet analysis useful in cybersecurity?

Packet analysis helps security professionals investigate suspicious network connections, identify communication patterns, troubleshoot network problems, and detect potentially malicious activity.



\## 2. Network Packet Structure



Network communication is organized into layers:



\- \*\*Data Link Layer:\*\* Handles communication over the local network. Ethernet is a commonly used technology at this layer.

\- \*\*Network Layer:\*\* Handles logical addressing and routing. IP is the primary protocol discussed in this project.

\- \*\*Transport Layer:\*\* Manages communication between applications using protocols such as TCP and UDP.

\- \*\*Application Layer:\*\* Contains protocols that provide network services to applications, such as HTTP, DNS and SSH.



Each layer adds its own information to data as it is prepared for transmission. This process is called encapsulation.



\## 3. Ethernet



\### What is Ethernet?

Ethernet is a family of networking technologies used for communication within wired local area networks. It defines Ethernet frames and related communication rules.



\### What is a MAC address?

A Media Access Control (MAC) address is typically a 48-bit address used to identify a network interface at the Ethernet layer. It is commonly represented in hexadecimal notation.



MAC addresses can sometimes be changed or randomized by software, so they should not always be treated as permanent hardware identifiers.



\### What is EtherType?

EtherType is a field in an Ethernet frame that identifies the protocol carried inside the frame.



Examples:

\- IPv4: 0x0800

\- IPv6: 0x86DD

\- ARP: 0x0806



\## 4. IPv4



\### What is IPv4?

Internet Protocol version 4 (IPv4) is a network-layer protocol that uses 32-bit addresses to identify source and destination devices.



\### Source IP

The IP address assigned to the sender of the packet.



\### Destination IP

The IP address to which the packet is being sent.



\### TTL (Time To Live)

TTL is a field in an IPv4 packet that limits how long the packet can travel through a network. Routers decrement the TTL value when forwarding a packet. When it reaches zero, the packet is discarded.



Note: The destination IP identifies the packet's intended destination, while the destination MAC address identifies the next-hop receiver on the local Ethernet link.



\## 5. TCP



\### What is TCP?

Transmission Control Protocol (TCP) is a connection-oriented transport-layer protocol. It provides reliable, ordered delivery of data through mechanisms such as acknowledgements and retransmissions.



\### What are ports?

Port numbers identify the application or service associated with network communication.



Examples:

\- HTTP: TCP port 80

\- HTTPS: TCP port 443

\- SSH: TCP port 22

\- DNS: commonly UDP port 53, but TCP port 53 is also used



\### TCP Three-Way Handshake

TCP establishes a connection through three main steps:



1\. SYN: The client requests a connection.

2\. SYN-ACK: The server acknowledges the request and responds with its own SYN.

3\. ACK: The client acknowledges the server's response.



\### Common TCP Flags

\- SYN: Initiates a connection.

\- ACK: Acknowledges received data or connection information.

\- FIN: Indicates that a side intends to close its connection.

\- RST: Resets or abruptly terminates a connection.

\- PSH: Requests that buffered data be pushed to the receiving application.

\- URG: Indicates that the urgent pointer field is significant.



\## 6. UDP



\### What is UDP?

User Datagram Protocol (UDP) is a connectionless transport-layer protocol. It sends datagrams without establishing a connection through a handshake.



UDP does not inherently guarantee delivery, ordering or retransmission of lost packets.



\### Common use cases

\- DNS queries

\- Voice and video communication

\- Online gaming

\- Live streaming



UDP is useful when low communication overhead and speed are important.



\## 7. ICMP



\### What is ICMP?

Internet Control Message Protocol (ICMP) is used by network devices to communicate error information and diagnostic messages.



\### What is ping?

Ping is a network diagnostic utility that commonly uses ICMP Echo Request and Echo Reply messages to test whether a destination responds.



Example:



&#x20;   ping 8.8.8.8



A failed ping does not always mean a device is offline. A firewall or network configuration may block ICMP traffic.



\## 8. Scapy



\### What is Scapy?

Scapy is a Python-based packet manipulation tool and library. It can create, send, capture, decode and analyze network packets.



\### How will we use Scapy in this project?

We will use Scapy to:

\- Capture live packets from a selected network interface.

\- Identify packet layers and protocols.

\- Extract source and destination IP addresses.

\- Extract TCP and UDP port information.

\- Inspect TCP flags.

\- Apply packet capture filters where supported.

\- Process packets for terminal output and metadata logging.



\## 9. Npcap



\### What is Npcap?

Npcap is a packet capture library and driver for Windows. It allows supported applications, including Wireshark and Scapy, to capture network traffic from supported interfaces.



\### Why is it needed on Windows?

Scapy uses packet capture mechanisms provided by Npcap on Windows to access network packets. Without a suitable capture driver, live packet capture may not work correctly.



\## 10. Project Scope



The Basic Network Sniffer will implement the following features:



1\. Live packet capture from a selected network interface.

2\. Source and destination IP extraction.

3\. Protocol identification, including TCP, UDP and ICMP.

4\. Source and destination port extraction when applicable.

5\. TCP flag identification.

6\. Protocol and IP-based filtering.

7\. Configurable packet capture limit.

8\. Metadata logging to a file.

9\. Summary statistics, including packet counts by protocol.



\### Security and Privacy Considerations

\- Capture only traffic on systems and networks for which permission has been granted.

\- Avoid storing packet payload contents by default.

\- Store only the metadata needed for the project's analysis.

\- Do not expose sensitive network information in screenshots or public repositories.



\## 11. Conclusion



This project will demonstrate how network packets can be captured and analyzed using Python and Scapy. It will provide practical experience with networking protocols, packet inspection, filtering and basic network security monitoring.

