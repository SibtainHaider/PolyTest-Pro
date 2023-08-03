Feature: API Testing

  Scenario: Testing the API
    Given There is an API with "API"
    Then User Hit Post "API post" with "Post File"
    Then User Hit Get "API get"
    Then User Hit Put "API put" with "Update File"
    Then User Hit Delete "API delete"
