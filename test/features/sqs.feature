Feature: Testowanie kolejki SQS

  Scenario: Wysłanie i odbiór wiadomości z SQS
    Given istnieje kolejka SQS
    When wysyłam wiadomość "Witaj AWS"
    Then powinienem odebrać wiadomość "Witaj AWS"