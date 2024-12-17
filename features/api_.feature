Feature: API Health Check

  Scenario: API responds with pong
    Given I set the API endpoint "/ping"
    When I send a GET request
    Then the response should contain "pong"
    And the response code should be 200