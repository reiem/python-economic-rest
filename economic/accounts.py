from economic.journal_entries import JournalEntry
from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class AccountSerializer(EconomicSerializer):
    id_property_name = 'account_number'


class Account(AccountSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/accounts/"

    # def get_journal_entries(self, limit=None):
    #     # self.entries is the URL for this Journals's entries
    #     # we have to remove the query parameters from the URL first, since they are added again by _query
    #     return JournalEntry._query(self.auth, self.entries.split('?')[0], limit=limit)