from pytest_bdd import scenario


@scenario('../features/sapphire_checkout.feature', "Checking the purchase feature")
def test_sapphire():
    pass
