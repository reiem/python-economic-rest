import logging
from typing import Iterable

from economic.account_entries import AccountEntry


class TestAccountEntry:
    def test_filter(self, auth):
        result = list(AccountEntry.filter(auth, year=2021))
        assert isinstance(result, Iterable)
        for entry in result:
            logging.debug(entry)
            assert isinstance(entry, AccountEntry)
