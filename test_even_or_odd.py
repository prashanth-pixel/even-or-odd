import unittest
import subprocess

class TestEvenOrOdd(unittest.TestCase):

    def run_script(self, input_value):
        process = subprocess.Popen(
            ['python', 'Even or odd'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=str(input_value))
        return stdout.strip(), stderr.strip()

    def test_even_number(self):
        stdout, stderr = self.run_script(4)
        self.assertEqual(stdout, "Enter a number: 4 is an even number")
        self.assertEqual(stderr, "")

    def test_odd_number(self):
        stdout, stderr = self.run_script(3)
        self.assertEqual(stdout, "Enter a number: 3 is an odd number")
        self.assertEqual(stderr, "")

if __name__ == '__main__':
    unittest.main()
