from textfsmlab import get_cdp_data

def test_cdp_parsing():
    data = get_cdp_data()
    assert isinstance(data, list)
    assert "local_interface" in data[0]
    assert "neighbor_interface" in data[0]
