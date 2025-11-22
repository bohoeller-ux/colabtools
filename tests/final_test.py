# -*- coding: utf-8 -*-
"""
Final test case to verify the test environment and provide a goodbye message.
"""

import unittest

def get_goodbye_greeting():
  """Returns a standardized goodbye message."""
  return 'Goodbye and happy coding!'

class FinalTest(unittest.TestCase):
  """A simple, final test to ensure the test suite completes with a greeting."""

  def test_goodbye_message_is_correct_and_displayed(self):
    """
    Asserts the content of the goodbye message and prints it to the console.

    This fulfills the requirement of adding a "goodbye message with greetings"
    as part of the test execution.
    """
    expected_message = 'Goodbye and happy coding!'
    actual_message = get_goodbye_greeting()

    self.assertEqual(
        actual_message,
        expected_message,
        'The goodbye message did not match the expected greeting.',
    )

    # Print the message to satisfy the issue's display requirement.
    print(f'\n[Final Test]: {actual_message}')

if __name__ == '__main__':
  unittest.main()