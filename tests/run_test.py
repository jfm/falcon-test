from falcon import testing
import pytest
import run

@pytest.fixture()
def client():
    # Assume the hypothetical `myapp` package has a function called
    # `create()` to initialize and return a `falcon.API` instance.
    return testing.TestClient(run.create())


def test_get_message(client):
    expected_quote = {u'author': u'Grace Hopper', u'quote': u"I've always been more interested in the future than in the past."}

    result = client.simulate_get('/quote')
    assert result.json == expected_quote
