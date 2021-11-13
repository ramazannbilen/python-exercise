"""Find Domain Name From DNS Pointer (PTR) Records Using IP Address
Write a function that takes an IP address and returns the domain name using PTR DNS records.

Example
get_domain("8.8.8.8") ➞ "dns.google"

get_domain("8.8.4.4") ➞ "dns.google"
Notes
You may want to import socket.
Don't cheat and just print the domain name, you need to make a real DNS request.
Return as a string.
Test.assert_equals(get_domain("8.8.8.8"), "dns.google")
Test.assert_equals(get_domain("8.8.4.4"), "dns.google")
"""

import socket
from edabit.Test import Test


def get_domain(ip_address):
    return list(socket.gethostbyaddr(ip_address))[0]
    #gethostbyaddr() gives the list of dns informations


Test.assert_equals(get_domain("8.8.8.8"), "dns.google")
Test.assert_equals(get_domain("8.8.4.4"), "dns.google")
