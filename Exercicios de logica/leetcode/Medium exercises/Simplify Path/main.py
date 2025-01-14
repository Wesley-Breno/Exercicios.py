import os


class Solution:
    def simplifyPath(self, path: str) -> str:
        return os.path.normpath(path)
