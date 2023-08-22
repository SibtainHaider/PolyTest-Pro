from pytest_bdd import scenario


@scenario('../features/desktop_app_testing.feature', 'Testing the Desktop Application')
def test_desktop_app():
    pass
