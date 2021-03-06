from jolokia import JolokiaClient
from .fixtures.responses import mock_valid_attribute_request


def test_valid_request():

    jc = JolokiaClient()

    setattr(jc.session, 'request', mock_valid_attribute_request)

    resp_json = jc.get_attribute(base_url='localhost:8080/jolokia', domain='java.lang', mbean='Memory')

    print(resp_json)

    assert resp_json['status'] == 200
    assert type(resp_json['value']) is int
