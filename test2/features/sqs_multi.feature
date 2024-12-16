Feature: Testowanie kolejki SQS

  Scenario: Wysłanie, odbiór i usunięcie wiadomości z SQS
    Given istnieje kolejka SQS
    When wysyłam wiadomości do kolejki
    Then powinienem odebrać maksymalnie 10 wiadomości
    And usunąć wszystkie wiadomości z kolejki