import vcr

from service import handler


@vcr.use_cassette()
def test_query_filter_mapping(monkeypatch):
    monkeypatch.setenv("BITLY_GENERIC_ACCESS_TOKEN", "my_token")
    url = dict(url="https://arxiv.org/")
    event = dict(queryStringParameters=url)
    result_dict = handler(event, None)
    expected_dict = {'statusCode': 200, 'body': '{"id": "https://j.mp/2soOxSO"}'}
    assert result_dict == expected_dict
