
"""
Basic Network Sniffer
CodeAlpha Cyber Security Internship

Captures network packet metadata using Scapy.
Does not display or store packet payload contents.
"""

import argparse
import csv
import ipaddress
from collections import Counter
from datetime import datetime
from pathlib import Path

from scapy.all import (
    ARP,
    ICMP,
    IP,
    TCP,
    UDP,
    Ether,
    conf,
    sniff,
)


CSV_FIELDS = [
    "timestamp",
    "protocol",
    "source_ip",
    "destination_ip",
    "source_port",
    "destination_port",
    "tcp_flags",
    "source_mac",
    "destination_mac",
]

SUPPORTED_PROTOCOLS = [
    "TCP",
    "UDP",
    "ICMP",
    "ARP",
    "IGMP",
]


def non_negative_int(value):
    """Validate non-negative integer arguments."""
    try:
        number = int(value)
        if number < 0:
            raise ValueError
        return number
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Value must be a non-negative integer."
        ) from exc


def valid_ipv4(value):
    """Validate an IPv4 address."""
    try:
        return str(ipaddress.IPv4Address(value))
    except ipaddress.AddressValueError as exc:
        raise argparse.ArgumentTypeError(
            "Please enter a valid IPv4 address."
        ) from exc


def process_packet(packet):
    """Extract metadata from a captured packet."""

    timestamp = datetime.fromtimestamp(
        float(packet.time)
    ).astimezone().isoformat(timespec="seconds")

    record = {
        "timestamp": timestamp,
        "protocol": "OTHER",
        "source_ip": "N/A",
        "destination_ip": "N/A",
        "source_port": "N/A",
        "destination_port": "N/A",
        "tcp_flags": "N/A",
        "source_mac": "N/A",
        "destination_mac": "N/A",
    }

    if Ether in packet:
        record["source_mac"] = packet[Ether].src
        record["destination_mac"] = packet[Ether].dst

    if ARP in packet:
        record["protocol"] = "ARP"
        record["source_ip"] = packet[ARP].psrc
        record["destination_ip"] = packet[ARP].pdst

    elif IP in packet:
        record["source_ip"] = packet[IP].src
        record["destination_ip"] = packet[IP].dst

        if TCP in packet:
            record["protocol"] = "TCP"
            record["source_port"] = packet[TCP].sport
            record["destination_port"] = packet[TCP].dport
            record["tcp_flags"] = str(packet[TCP].flags)

        elif UDP in packet:
            record["protocol"] = "UDP"
            record["source_port"] = packet[UDP].sport
            record["destination_port"] = packet[UDP].dport

        elif ICMP in packet:
            record["protocol"] = "ICMP"

        elif int(packet[IP].proto) == 2:
            record["protocol"] = "IGMP"

        else:
            record["protocol"] = (
                f"IP protocol {packet[IP].proto}"
            )

    return record


def display_packet(record):
    """Display extracted packet metadata."""

    print(f"\n[{record['timestamp']}]")
    print(f"Protocol: {record['protocol']}")
    print(f"Source IP: {record['source_ip']}")
    print(f"Destination IP: {record['destination_ip']}")
    print(f"Source Port: {record['source_port']}")
    print(f"Destination Port: {record['destination_port']}")
    print(f"TCP Flags: {record['tcp_flags']}")
    print(f"Source MAC: {record['source_mac']}")
    print(f"Destination MAC: {record['destination_mac']}")
    print("-" * 55)


def main():

    parser = argparse.ArgumentParser(
        description="Basic Network Sniffer using Scapy"
    )

    parser.add_argument(
        "--iface-index",
        type=non_negative_int,
        required=True,
        help="Scapy network interface index",
    )

    parser.add_argument(
        "--count",
        type=non_negative_int,
        default=20,
        help="Maximum packets; 0 means unlimited",
    )

    parser.add_argument(
        "--timeout",
        type=non_negative_int,
        default=30,
        help="Capture duration in seconds; 0 means unlimited",
    )

    parser.add_argument(
        "--protocol",
        type=str.upper,
        choices=SUPPORTED_PROTOCOLS,
        help="Filter by protocol",
    )

    parser.add_argument(
        "--ip",
        type=valid_ipv4,
        help="Filter by IPv4 source or destination address",
    )

    parser.add_argument(
        "--log-file",
        default="logs/packets.csv",
        help="Path for CSV metadata log",
    )

    args = parser.parse_args()

    # Prevent an unlimited capture.
    if args.count == 0 and args.timeout == 0:
        parser.error(
            "Specify a packet count or timeout to stop capture."
        )

    # Retrieve the selected network interface safely.
    try:
        interface = conf.ifaces.dev_from_index(
            args.iface_index
        )

    except ValueError:
        parser.error(
            f"Unknown network interface index: {args.iface_index}"
        )

    if interface is None:
        parser.error(
            f"No network interface found with index {args.iface_index}."
        )

    # Construct the BPF capture filter.
    filter_parts = []

    if args.protocol:
        filter_parts.append(args.protocol.lower())

    if args.ip:
        filter_parts.append(f"host {args.ip}")

    capture_filter = " and ".join(filter_parts) or None

    log_path = Path(args.log_file)

    packet_counter = 0
    protocol_counter = Counter()

    print("=" * 55)
    print("BASIC NETWORK SNIFFER")
    print("=" * 55)
    print(f"Interface: {interface}")
    print(f"Protocol filter: {args.protocol or 'All'}")
    print(f"IP filter: {args.ip or 'All'}")
    print(f"BPF filter: {capture_filter or 'None'}")
    print(f"Packet limit: {args.count or 'Unlimited'}")
    print(f"Timeout: {args.timeout or 'Unlimited'} seconds")
    print(f"Metadata log: {log_path}")
    print("=" * 55)

    try:
        # Create the output directory if necessary.
        log_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with log_path.open(
            "a",
            newline="",
            encoding="utf-8"
        ) as log_file:

            writer = csv.DictWriter(
                log_file,
                fieldnames=CSV_FIELDS
            )

            if log_file.tell() == 0:
                writer.writeheader()

            def packet_callback(packet):
                nonlocal packet_counter

                record = process_packet(packet)

                packet_counter += 1
                protocol_counter[record["protocol"]] += 1

                display_packet(record)

                writer.writerow(record)
                log_file.flush()

                print(
                    f"Packet #{packet_counter} saved to CSV."
                )

            print("\nStarting capture... Press Ctrl+C to stop.")

            sniff(
                iface=interface,
                filter=capture_filter,
                prn=packet_callback,
                count=args.count,
                timeout=args.timeout,
                store=False,
            )

    except KeyboardInterrupt:
        print("\nCapture interrupted by user.")

    except Exception as error:
        print(f"\nCapture failed: {error}")
        raise SystemExit(1) from error

    # Display capture statistics.
    print("\n" + "=" * 55)
    print("CAPTURE SUMMARY")
    print("=" * 55)

    print(f"Total packets processed: {packet_counter}")

    print("\nProtocol Distribution:")

    if protocol_counter:
        for protocol, total in sorted(
            protocol_counter.items()
        ):
            print(f"{protocol}: {total}")
    else:
        print("No matching packets captured.")

    print("=" * 55)
    print(f"Metadata saved to: {log_path}")


if __name__ == "__main__":
    main()
