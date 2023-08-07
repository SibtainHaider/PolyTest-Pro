from pytest_bdd import scenario, given, when, then, parsers


@scenario('../features/webfeatures.feature', "Login with RO valid credentials")
def test_web():
    pass


@scenario('../features/ess_dashboard.feature', "User dashboard")
def test_ess_dashboard():
    pass
