@dashboard
Feature: Dashboard

  Scenario: User dashboard
    Given User is on the "dashboard" page on "dashboard testFile"
    Then User is verified with "name user" located on "testFile"
    Then User Click on "time sheet" on "dashboard testFile"
