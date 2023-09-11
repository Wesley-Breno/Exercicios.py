from collections import Counter
from utils import read_logs, get_sites

if __name__ == '__main__':
    data_logs = read_logs('logs.txt')
    urls_blockeds = dict(sorted(Counter(get_sites(data_logs)).items(), key=lambda x: x[1], reverse=True))

    print('\nMost users blocked in websites:')
    for key, value in urls_blockeds.items():
        print(f'Site: {key}\n'
              f'Users blocked: {value}\n')
