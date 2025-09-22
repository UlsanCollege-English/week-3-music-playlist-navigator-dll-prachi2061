class _DNode:
    __slots__ = ("title", "prev", "next")
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        """Append song to the end of the playlist."""
        new_node = _DNode(title)
        if not self.head:  # empty playlist
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        if not self.current:  # first song added
            self.current = self.head

    def play_first(self):
        """Set current to the first song."""
        self.current = self.head

    def next(self):
        """Move to next song if possible."""
        if self.current and self.current.next:
            self.current = self.current.next

    def prev(self):
        """Move to previous song if possible."""
        if self.current and self.current.prev:
            self.current = self.current.prev

    def insert_after_current(self, title):
        """Insert a new song after the current song."""
        if not self.current:
            self.add_song(title)
            return
        new_node = _DNode(title)
        new_node.prev = self.current
        new_node.next = self.current.next
        if self.current.next:
            self.current.next.prev = new_node
        self.current.next = new_node
        if self.current == self.tail:
            self.tail = new_node

    def remove_current(self):
        """Remove current song and update current pointer."""
        if not self.current:
            return
        prev_node = self.current.prev
        next_node = self.current.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
        self.current = next_node if next_node else prev_node

    def to_list(self):
        """Return playlist as a list of song titles."""
        result = []
        node = self.head
        while node:
            result.append(node.title)
            node = node.next
        return result
