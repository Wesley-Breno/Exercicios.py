import re


def read_logs(file_name: str) -> list:
    with open(file_name) as file:
        data = [d.replace('\n', '') for d in file.readlines()]

    return data


def get_sites(data_logs: list) -> list:
    urls_sites = []

    for data in data_logs:
        url_site = re.findall('(www\..*?\..*?) ', data)
        urls_sites.append(*url_site)

    return urls_sites


__all__ = ['get_sites', 'read_logs']
