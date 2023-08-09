from pytest_bdd import scenario, given, when, then, parsers


@scenario('../features/android_testing.feature', 'Testing the APPLICATION')
def test_android():
    pass