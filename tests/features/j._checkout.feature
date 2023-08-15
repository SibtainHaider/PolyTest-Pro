@checkout
Feature: J. checkout

  Scenario: Checking the purchase feature
    Given User is on the "junaid jamshed page" page on "JJ"
    Then User selects "country" on "country select" from "JJ"
#    Then User Click on "enter btn" on "JJ"
    Then User Click on "enter btn" on "JJ"
    Then User Click on "men btn" on "JJ"
    Then User Click on "shop now" on "JJ"
    Then The browser switches window to child
    Then User Click on "add bag" on "JJ"
    Then User Click on "choose size" on "JJ"
    Then User scrolls to "choose size" on "JJ"
    Then User Click on "add cart" on "JJ"
    Then User Click on "check out" on "JJ"
    Then User scrolls to "Email word" on "JJ"
    Then User enter "email" in "email box" on "JJ"
    Then User scrolls to "email box" on "JJ"
    Then User enter "fname" in "fname box" on "JJ"
    Then User enter "lname" in "lname box" on "JJ"
    Then User scrolls to "fname box" on "JJ"
    Then User enter "address" in "address box" on "JJ"
    Then User scrolls to "address box" on "JJ"
    Then User enter "state" in "state box" on "JJ"
    Then User scrolls to "state box" on "JJ"
    Then User selects "city" on "city select" from "JJ"
    Then User enter "zipcode" in "zip box" on "JJ"
    Then User scrolls to "city select" on "JJ"
    Then User enter "phone" in "phone box" on "JJ"
    Then User scrolls to "phone box" on "JJ"
    Then User Click on "next" on "JJ"

