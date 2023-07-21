@login
Feature: Login

  Background: Systems Home
    Given I am on the "systems" home page

  Scenario: Login with RO valid credentials
    Given I am on the "systems" home page
#    When I enter "user name" in "user name textbox"
#    Then I click on the "login" button
#    Then Search for "name_cred" in "login_btn"
#    Then I should be successfully logged in with "name_user"
     When User enter "test data" in "text box" on "locators"
     Then User Click on "login" on "locators"
