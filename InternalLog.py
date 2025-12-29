import datetime

class InternalLog:
    def __init__(self):
        self._storage = []  # Här sparas alla logg-rader

    def add(self, message, level="INFO"):
        """Lägger till ett nytt meddelande i det interna minnet."""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }
        self._storage.append(entry)

    def get_all(self):
        """Hämtar alla loggar formaterade som strängar."""
        return [f"[{log['timestamp']}] [{log['level']}] {log['message']}" for log in self._storage]
    
    def get_level(self, level):
        """Hämtar alla loggar av en specifik nivå."""
        return [f"[{log['timestamp']}] [{log['level']}] {log['message']}" for log in self._storage if log['level'] == level]

    def get_latest(self):
        """Hämtar endast det senaste meddelandet."""
        if self._storage:
            log = self._storage[-1]
            return f"[{log['timestamp']}] [{log['level']}] {log['message']}"
        return "Inga loggar tillgängliga."

    def clear(self):
        """Rensar alla loggar från minnet."""
        self._storage = []
