from ipaddress import IPv4Address, IPv6Address, ip_address


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        try:
            ip = ip_address(queryIP)
            if isinstance(ip, IPv4Address):
                return "IPv4"
            elif isinstance(ip, IPv6Address):
                isIpv6 = "IPv6"
                for x in queryIP.split(":"):
                    if not 1 <= len(x) <= 4:
                        isIpv6 = "Neither"
                return isIpv6
        except ValueError:
            return "Neither"
