from new_project import app


def test_endpoint():
    assert app.index() == {'hello': 'world'}


def test_schedule():
    assert app.every_hour({'what': 'hello'}) is None
