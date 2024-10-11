class Solution:
    def getFolderNames(self, names: list[str]) -> list[str]:
        name_count = {}
        result = []
        for name in names:
            if name not in name_count:
                result.append(name)
                name_count[name] = 1
            else:
                k = name_count[name]
                new_name = f"{name}({k})"
                while new_name in name_count:
                    k += 1
                    new_name = f"{name}({k})"
                result.append(new_name)
                name_count[name] = k + 1
                name_count[new_name] = 1
        return result
