@login
Feature: Login

  Background: Systems Home
    Given User is on the "systems" home page

  Scenario: Login with RO valid credentials
    Given User is on the "systems" home page
    When User enter "test data" in "text box" on "testFile"
    Then User Click on "login" on "testFile"
    Then User should be successfully logged in with "name user" located on "testFile"
