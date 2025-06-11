import yaml
from pathlib import Path


class MCPConfig:
    """Minimal handler for Model Context Protocol config files."""

    def __init__(self, path: str):
        self.path = Path(path)
        self.docs = []
        self.meta = {}
        self.load()

    def load(self):
        if not self.path.exists():
            return
        data = yaml.safe_load(self.path.read_text()) or {}
        self.docs = data.get("docs", [])
        self.meta = data.get("meta", {})

    def read_documents(self):
        contents = {}
        for doc in self.docs:
            p = Path(doc)
            if p.exists():
                contents[str(p)] = p.read_text()
        return contents
