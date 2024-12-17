Feature: REST API Testing with Behave

Scenario: Creating an item successfully
  Given I set the FastAPI REST API endpoint
  When I send a POST request to "/items/" with the following data:
    | name        | value      |
    | name        | Laptop     |
    | description | A great PC |
    | price       | 1200.00    |
    | tax         | 23.00      |
  Then the response should contain:
    | key     | value                     |
    | message | Item created successfully |
  And the response code should be 200