from src import utils
from collections import Counter

logs = utils.AnalyzerLogs('logs.txt')
searches = logs.get_searches()
better_searches = dict(sorted(Counter(searches).items(), key=lambda x: x[1], reverse=True))

print('\n\t\t[ Pesquisa do google que mais trazem internautas ]\n')
for key, value in better_searches.items():
    print(f'{key}: {value}')
