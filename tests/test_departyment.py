import logging
import pprint
from typing import Iterable

from economic.departments import Department


class TestDepartment:
    def test_all(self, auth):
        result = Department.all(auth)
        assert isinstance(result, Iterable)
        for entry in result:
            logging.debug(pprint.pformat(entry))
            assert isinstance(entry, Department)
