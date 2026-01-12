from collections import deque
from datetime import datetime, timedelta
import bisect
from typing import Any, Deque, Generic, List, Optional, TypeVar

T = TypeVar('T')

class LiveCache(Generic[T]):
    """
    Maintains a local memory cache of the last [time_window_minutes] minutes of items T
    """

    def __init__(self, timestamp_attr, group_id_attr, time_window_minutes=15):
        self.timestamp_attr = timestamp_attr
        self.group_id_attr = group_id_attr
        self.time_window_minutes = timedelta(minutes=time_window_minutes)
        self.items: Deque[T] = deque()

    def add(self, item: T) -> None:
        """Add timestamped object to deque"""

        self.items.append(item)
        self._cleanup()

    def get_group(self, group_id_value: Any) -> Optional[List[T]]:
        """ Get all items where group_id_attr == group_id_value """
        
        self._cleanup()
        return [item for item in self.items if item[self.group_id_attr] == group_id_value]

    def _cleanup(self) -> None:
        """Remove items outside of the time window"""

        #cutoff = datetime.now() - self.time_window_minutes
        #cutoff = datetime.now() - timedelta(minutes=self.time_window_minutes)

        #while self.items and getattr(self.items[0], self.timestamp_attr) < cutoff:
        #    self.items.popleft()

    def clear(self):
        """Empty the cache"""

        self.buffer.clear()
