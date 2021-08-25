
from economic.journal_entries import JournalEntry
import logging
import pprint
from typing import Iterable

from economic.journals import Journal


class TestJournal:
    def test_all(self, auth):
        result = Journal.all(auth)
        assert isinstance(result, Iterable)
        for entry in result:
            logging.debug(pprint.pformat(entry))
            assert isinstance(entry, Journal)

    def test_get_journal_entries(self, auth):
        result = list(Journal.all(auth, limit=1))
        assert len(result) == 1
        for journal in result:
            entries = journal.get_journal_entries()
            for entry in entries:
                logging.debug(entry)
                assert isinstance(entry, JournalEntry)

