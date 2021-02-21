Feature: today-rooms
  Scenario: today free rooms
    Given an English speaking user
     When the user says "Tell me what rooms are free today"
     Then "test-skill" should reply with "The answer to all questions is 42."

Feature: events
  Scenario: events on friday
    Given an English speaking user
     When the user says "Tell me what events are coming up this friday"
     Then "test-skill" should reply with "The event happening on friday is Philipps Birthday."

  Scenario: events next week
    Given an English speaking user
     When the user says "Tell me what events are coming up next week"
     Then "test-skill" should reply with "The event happening on next week is Philipps Birthday."