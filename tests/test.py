import os
import shutil
import unittest
import main


class TestFileSorter(unittest.TestCase):
    def test_sort_files(self):
        current_location = os.curdir
        main.sort_files(f"{current_location}\\TestFiles")
        predicted_list = ["jpg", "pdf", "png", "txt"]
        self.assertEqual(os.listdir(f"{current_location}\\SortedFiles"), predicted_list)
        shutil.rmtree(f"{current_location}\\SortedFiles")


if __name__ == "__main__":
    unittest.main()
