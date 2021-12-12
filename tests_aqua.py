import unittest
import requirements_parser
import os

requirements_parser = requirements_parser.RequirementsParser()


class MyTestCase(unittest.TestCase):

    def test_requirements_num(self):
        """check result if double item and the functions (with numbers) and check when requirements after test ('test_requirements.txt')"""
        dict_result = {"1", "2", "3", "4", "5", "6", "7"}

        with open('test_requirements.txt', 'w') as file:
            file.write("1\n 2\n 3\n -r test2_requirements.txt\n 4\n")

        with open('test2_requirements.txt', 'w') as file2:
            file2.write("1\n 5\n 6\n 7\n")

        output_dict = requirements_parser.open_requirements('test_requirements.txt')

        os.remove('test_requirements.txt')
        os.remove('test2_requirements.txt')

        self.assertEqual(output_dict, dict_result)

    def test_requirements_letters(self):
        """check result if double item and the functions (with letters) and check when requirements before test ('requirements_test.txt')"""

        dict_result = {"a", "b", "c", "d", "g", "j"}

        with open('requirements_test.txt', 'w') as file:
            file.write("a\n b\n c\n -r requirements_test2.txt\n d\n")

        with open('requirements_test2.txt', 'w') as file2:
            file2.write("a\n b\n g\n j\n")

        output_dict = requirements_parser.open_requirements('requirements_test.txt')

        os.remove('requirements_test.txt')
        os.remove('requirements_test2.txt')

        self.assertEqual(output_dict, dict_result)


if __name__ == '__main__':
    unittest.main()
