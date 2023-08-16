@checkout
Feature: Sapphire checkout

  Scenario: Checking the purchase feature
    Given User is on the "sapphire page" page on "sapphire"
    When User Click on "men btn" on "sapphire"
    And User Click on "add bag" on "sapphire"
#    Then User Click on "choose size" on "sapphire"
    Then User Click on "add cart" on "sapphire"
    Then User Click on "check out" on "sapphire"
    Then User enter "email" in "email box" on "sapphire"
    Then User enter "fname" in "fname box" on "sapphire"
    Then User enter "lname" in "lname box" on "sapphire"
    Then User enter "address" in "address box" on "sapphire"
    Then User enter "city" in "city box" on "sapphire"
    Then User enter "zipcode" in "zip box" on "sapphire"
    Then User enter "phonenum" in "num box" on "sapphire"
    Then User Click on "continue btn" on "sapphire"