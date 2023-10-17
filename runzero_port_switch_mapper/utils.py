import csv
from typing import Dict, Union, List


def parse_inventory_items(inventory: List) -> List[Dict]:
    ret = []
    for host in inventory:
        host_attributes = host.get("attributes", None)
        hostnames = host.get("names", None)
        hostname = hostnames[0] if hostnames else None
        host_ips = host.get("addresses", None)
        host_ip = host_ips[0] if host_ips else None
        switch_port = get_switch_port(host_attributes)
        switch_ip = get_switch_ip(host_attributes)
        switch_name = get_switch_name(host_attributes)
        ret.append(
            {
                "hostname": hostname,
                "host_ip": host_ip,
                "name": switch_name,
                "ip": switch_ip,
                "port": switch_port,
            }
        )
    return ret


def get_switch_port(host: Dict) -> Union[str, None]:
    port_string = host.get("switch.port", None)
    if port_string is None:
        return None
    if "-" in port_string:
        return port_string.split("-")[-1]
    return None


def get_switch_ip(host: Dict) -> Union[str, None]:
    switch_ipaddress = host.get("switch.ip", None)
    if switch_ipaddress is None:
        return None
    return switch_ipaddress


def get_switch_name(host: Dict) -> Union[str, None]:
    switch_name = host.get("switch.name", None)
    if switch_name is None:
        return None
    return switch_name


def write_csv_output(output_file, hosts: List[Dict]):
    with open(output_file, mode="w") as csv_file:
        fieldnames = ["hostname", "host_ip", "name", "ip", "port"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for host in hosts:
            writer.writerow(host)
