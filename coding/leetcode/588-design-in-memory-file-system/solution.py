from collections import defaultdict


# situ: this line is super sharp
Trie = lambda: defaultdict(Trie)


class FileSystem:
    def __init__(self):
        self.fs = Trie()
        self.fileinfo = defaultdict(str)  # hold all files

    def ls(self, path: str) -> List[str]:
        if path in self.fileinfo:
            return path.split('/')[-1:]
        cur = self.fs
        for dir in path.split('/'):
            if dir in cur:
                cur = cur[dir]
            elif dir:
                return []
        return sorted(cur.keys())

    def mkdir(self, path: str) -> None:
        cur = self.fs
        for dir in path.split('/'):
            if dir: cur = cur[dir]

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.fileinfo[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.fileinfo[filePath]

