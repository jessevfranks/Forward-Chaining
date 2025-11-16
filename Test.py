import unittest

from jesse_franks_q3 import forward_chain


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        rules_input = ["A & B => C", "C => D"]
        facts_input = {"A", "B"}
        response = set(forward_chain(rules_input, facts_input))
        answer = {"A", "B", "C", "D"}
        self.assertEqual(answer, response)

    def test_advanced(self):
        rules_input = [
            "A&B => C", # Testing spacing
            "C => D",
            "D | E => F",  # Added an OR rule
            "F & G => H",
            "AX => Z"  # Added a rule to test substring
        ]

        facts_input = {"A", "B", "E", "G"}
        response = set(forward_chain(rules_input, facts_input))
        answer = {"A", "B", "C", "D", "E", "F", "G", "H"}
        self.assertEqual(answer, response)


if __name__ == '__main__':
    unittest.main()
