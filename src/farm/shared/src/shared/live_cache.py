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
        self._items: Deque[T] = deque()

    def add(self, item: T) -> None:
        """Add timestamped object to deque"""

        self._items.append(item)
        self._cleanup()

    @property
    def items(self) -> List[T]:
        """Clean the cache and return remaining items as a list."""
        
        self._cleanup()
        return list(self._items)

    def get_group(self, group_id_value: Any) -> Optional[List[T]]:
        """ Get all items where group_id_attr == group_id_value """
        
        self._cleanup()
        return [item for item in self._items if getattr(item, self.group_id_attr) == group_id_value]

    def _cleanup(self) -> None:
        """Remove items outside of the time window"""

        cutoff_timestamp = (datetime.now() - self.time_window_minutes).timestamp()
        while self._items and getattr(self._items[0], self.timestamp_attr) < cutoff_timestamp:
            self._items.popleft()    

    def clear(self):
        """Empty the cache"""

        self._items.clear()
