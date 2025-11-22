"""Final tests that should be run last."""

import unittest


class FinalTest(unittest.TestCase):
  """Final tests for the suite."""

  def test_final_check_completes(self):
    """A simple final check to ensure the test suite ran."""
    self.assertTrue(True, 'Final check should always pass.')

  def test_goodbye_message(self):
    """Prints a goodbye message upon successful completion of tests."""
    print('\nAll tests are complete. Goodbye and have a great day!')
    self.assertTrue(True)


if __name__ == '__main__':
  unittest.main()