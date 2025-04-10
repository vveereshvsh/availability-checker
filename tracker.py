from collections import defaultdict

class AvailabilityTracker:
    def __init__(self):
        self._history = defaultdict(list)

    def update(self, domain, is_available):
        self._history[domain].append(is_available)

    def get(self, domain):
        history = self._history.get(domain, [])
        if not history:
            return 0.0
        return sum(history) / len(history)

    def get_all(self):
        return {domain: self.get(domain) for domain in self._history}
