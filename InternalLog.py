import datetime

class InternalLog:
    def __init__(self):
        self._storage = []  # Här sparas alla logg-rader
        self._daystore = {}  # Här kan loggar sparas per dag om så önskas

# TODO Lägg till en tagg, tidstämpel och hämta ut alla som hör till den 


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
    
    def save_day(self, day):
        """Sparar loggar för en specifik dag."""
        self._daystore[day] = self._storage.copy()
        clear(self) # Tömmer den nuvarande loggen efter sparning

    def get_day(self, day):
        """Hämtar loggar för en specifik dag."""
        if day in self._daystore:
            return [f"[{log['timestamp']}] [{log['level']}] {log['message']}" for log in self._daystore[day]]
        return []

    def get_latest(self):
        """Hämtar endast det senaste meddelandet."""
        if self._storage:
            log = self._storage[-1]
            return f"[{log['timestamp']}] [{log['level']}] {log['message']}"
        return "Inga loggar tillgängliga."

    def clear(self):
        """Rensar alla loggar från minnet."""
        self._storage = []
