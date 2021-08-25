from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class JournalEntrySerializer(EconomicSerializer):
    id_property_name = 'journal_entry_number'


class JournalEntry(JournalEntrySerializer, QueryMixin):

    base_url = (  # Use .filter(journal_number=1)
        "https://restapi.e-conomic.com/journals/%(journal_number)s/entries"
    )

    @classmethod
    def all(cls, auth, limit=None, page_size=1000):
        raise Exception(
            "Please use .filter() and provide "
            "journal_number as a keyword argument"
        )

    @classmethod
    def filter(cls, auth, journal_number=None, **kwargs):
        if not journal_number:
            raise Exception(
                "Please provide a journal_number argument to .filter()"
            )
        base_url = cls.base_url % {'journal_number': journal_number}

        return super(JournalEntry, cls)\
            .filter(auth, base_url=base_url, **kwargs)

    def __str__(self):
        return (
            f"Journal {self.journal['journalNumber']}: "
            f"Entry: {self.journal_entry_number} {self.date} {self.amount_default_currency}"
        )
