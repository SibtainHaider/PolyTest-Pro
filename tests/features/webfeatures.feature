@login
Feature: Login

  Background: Systems Home
    Given User is on the "systems" page on "testFile"

  Scenario: Login with RO valid credentials
    Given User is on the "systems" page on "testFile"
    When User enter "test data" in "text box" on "testFile"
    Then User Click on "login" on "testFile"
    Then User is verified with "name user" located on "testFile"
