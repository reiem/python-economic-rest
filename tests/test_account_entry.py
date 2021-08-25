

import logging
import pprint
from typing import Iterable

from economic.account_entries import AccountEntry


class TestAccountEntry:
    def test_filter(self, auth):
        result = AccountEntry.filter(auth, year=2021)
        assert isinstance(result, Iterable)
        for entry in result:
            logging.debug(pprint.pformat(entry))
            assert isinstance(entry, AccountEntry)
