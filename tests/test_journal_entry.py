import logging
from typing import Iterable

from economic.journal_entries import JournalEntry


class TestJournalEntry:
    def test_filter(self, auth):
        result = JournalEntry.filter(auth, journal_number=1)
        assert isinstance(result, Iterable)
        for entry in result:
            logging.debug(entry)
            assert isinstance(entry, JournalEntry)
