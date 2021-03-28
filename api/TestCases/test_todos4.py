# Standard library imports...
from unittest import skipIf

# Local imports...
from constants import SKIP_REAL
# Local imports...
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/maximilianhues/Documents/CODE/stock-checker/api')

from services import get_todos, get_uncompleted_todos
# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal, assert_true


@skipIf(SKIP_REAL, 'Skipping tests that hit the real API server.')
def test_integration_contract():
    # Call the service to hit the actual API.
    actual = get_todos()
    actual_keys = actual.json().keys()

    # Call the service to hit the mocked API.
    with patch('services.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{
            'defaultKeyStatistics': "",
            'financialsTemplate': "",
            'price': "",
            'financialData': "",
            'quoteType': "",
            'calendarEvents': "",
            'summaryDetail': "",
            'symbol': "",
            'pageViews': "",
            'quoteData': "",
            'mktmData': ""
        }]

        mocked = get_todos()
        mocked_keys = mocked.json().pop().keys()

    # An object from the actual API and an object from the mocked API should have
    # the same data structure.
    assert_list_equal(list(actual_keys), list(mocked_keys))


test_integration_contract()