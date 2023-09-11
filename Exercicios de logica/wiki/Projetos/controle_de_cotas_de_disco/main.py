from tabulate import tabulate
from utils import read_file, convert_bytes_for_megabytes, percentage_calculation

if __name__ == '__main__':
    data_users_formated = []  # List that will contain the formatted data of the users to be presented in the table

    data_users = read_file('usuarios.txt')
    name_users = [data[0] for data in data_users]
    megabytes_users = [convert_bytes_for_megabytes(int(data[1])) for data in data_users]
    percentage_users = [percentage_calculation(sum(megabytes_users), mb_user) for mb_user in megabytes_users]

    # Add formated data in the list
    for index, data in enumerate(name_users):
        data_users_formated.append([index + 1, data, f'{megabytes_users[index]} Mb', f'{percentage_users[index]}%'])

    print('ACME Inc. | Uso do espaço em disco pelos usuários')
    print(tabulate(data_users_formated, headers=['Nr', 'Nome', 'Tot Mb', '% de uso'], tablefmt='outline'))