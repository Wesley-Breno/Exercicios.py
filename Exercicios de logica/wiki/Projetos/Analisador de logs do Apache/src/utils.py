import re
from collections import Counter


class AnalyzerLogs:
    def __init__(self, path_log_file: str):
        self.log_path = path_log_file
        self.logs = self._get_logs()

    def _get_logs(self):
        with open(self.log_path, 'r') as file:
            logs_list = file.readlines()

        return logs_list

    def get_searches(self):
        searches = []
        for log in self.logs:
            searches.append(*re.findall(r'/search\?q=(.*?)"', log))

        return searches


__all__ = ['AnalyzerLogs']
