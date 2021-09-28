
# from economic.journal_entries import JournalEntry
import logging
import pprint
from typing import Iterable

# from economic.journals import Journal
from economic.accounts import Account


class TestAccount:
    def test_all(self, auth):
        result = Account.all(auth)
        assert isinstance(result, Iterable)
        for account in result:
            logging.debug(pprint.pformat(account))
            assert isinstance(account, Account)
