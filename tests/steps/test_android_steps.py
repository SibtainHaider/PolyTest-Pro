from pytest_bdd import scenario


@scenario('../features/android_testing.feature', 'Testing the APPLICATION')
def test_android():
    pass


@scenario('../features/sapphire_checkout.feature', "Checking the purchase feature")
def test_sapphire():
    pass
