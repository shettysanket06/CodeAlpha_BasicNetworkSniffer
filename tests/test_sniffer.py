import time
import unittest

from scapy.all import Ether, ARP, IP, TCP, UDP, ICMP, Raw

from src.sniffer import process_packet


def make_packet(packet):
    """Give synthetic packets a timestamp, as live captures have."""
    packet.time = time.time()
    return packet


class TestPacketAnalyzer(unittest.TestCase):

    def test_tcp_packet(self):
        packet = make_packet(
            Ether(
                src="00:11:22:33:44:55",
                dst="aa:bb:cc:dd:ee:ff"
            )
            / IP(src="192.168.1.10", dst="192.168.1.20")
            / TCP(sport=54321, dport=443, flags="PA")
        )

        result = process_packet(packet)

        self.assertEqual(result["protocol"], "TCP")
        self.assertEqual(result["source_ip"], "192.168.1.10")
        self.assertEqual(result["destination_ip"], "192.168.1.20")
        self.assertEqual(result["source_port"], 54321)
        self.assertEqual(result["destination_port"], 443)
        self.assertEqual(result["tcp_flags"], "PA")
        self.assertEqual(result["source_mac"], "00:11:22:33:44:55")

    def test_udp_packet(self):
        packet = make_packet(
            Ether()
            / IP(src="192.168.1.10", dst="8.8.8.8")
            / UDP(sport=53000, dport=53)
        )

        result = process_packet(packet)

        self.assertEqual(result["protocol"], "UDP")
        self.assertEqual(result["source_ip"], "192.168.1.10")
        self.assertEqual(result["destination_ip"], "8.8.8.8")
        self.assertEqual(result["source_port"], 53000)
        self.assertEqual(result["destination_port"], 53)

    def test_icmp_packet(self):
        packet = make_packet(
            Ether()
            / IP(src="192.168.1.10", dst="1.1.1.1")
            / ICMP()
        )

        result = process_packet(packet)

        self.assertEqual(result["protocol"], "ICMP")
        self.assertEqual(result["source_ip"], "192.168.1.10")
        self.assertEqual(result["destination_ip"], "1.1.1.1")
        self.assertEqual(result["source_port"], "N/A")
        self.assertEqual(result["destination_port"], "N/A")

    def test_arp_packet(self):
        packet = make_packet(
            Ether()
            / ARP(
                op=1,
                psrc="192.168.1.10",
                pdst="192.168.1.1"
            )
        )

        result = process_packet(packet)

        self.assertEqual(result["protocol"], "ARP")
        self.assertEqual(result["source_ip"], "192.168.1.10")
        self.assertEqual(result["destination_ip"], "192.168.1.1")
        self.assertEqual(result["source_port"], "N/A")

    def test_igmp_identification(self):
        packet = make_packet(
            Ether()
            / IP(
                src="192.168.1.10",
                dst="224.0.0.22",
                proto=2
            )
        )

        result = process_packet(packet)

        self.assertEqual(result["protocol"], "IGMP")

    def test_payload_is_not_in_metadata(self):
        secret_payload = "TEST_SECRET_PAYLOAD"

        packet = make_packet(
            Ether()
            / IP(src="192.168.1.10", dst="192.168.1.20")
            / TCP(sport=12345, dport=443)
            / Raw(load=secret_payload.encode())
        )

        result = process_packet(packet)

        self.assertNotIn("payload", result)
        self.assertNotIn(secret_payload, repr(result))


if __name__ == "__main__":
    unittest.main(verbosity=2)
