@checkout
Feature: Khaadi checkout

  Scenario: Checking the purchase feature
    Given User is on the "khaadi page" page on "khaadi"
    Then User Click on "country select" on "khaadi"
    Then User Click on "country choice" on "khaadi"
    Then User Click on "enter btn" on "khaadi"
    Given User is on the "pakistan page" page on "khaadi"
    Then User Click on "shop now" on "khaadi"
    Then The browser switches windows
    Given User is on the "shop now page" page on "khaadi"
    Then User Click on "add bag" on "khaadi"
    Then User Click on "choose size" on "khaadi"
    Then User Click on "add cart" on "khaadi"
    Then User Click on "check out" on "khaadi"
    Given User is on the "check out page" page on "khaadi"
    Then User enter "email" in "email box" on "khaadi"
    Then User enter "fname" in "fname box" on "khaadi"
    Then User enter "lname" in "lname box" on "khaadi"
    Then User enter "mobile number" in "mobile.box" on "khaadi"
    Then User enter "address" in "address.box" on "khaadi"
    Then User selects "province" on "province select" from "khaadi"
    Then User selects "city" on "city select" from "khaadi"
    Then User Click on "proceed payment" on "khaadi"

