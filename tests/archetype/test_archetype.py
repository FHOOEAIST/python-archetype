import os
import shutil
import unittest

from archetype.archetype import Archetype


class TestArchetype(unittest.TestCase):
    @staticmethod
    def cleanup():
        """
        Clean up the directory

        :return:
        """
        current_directory = os.getcwd()
        test_folder = current_directory + os.path.sep + "test"
        pycache_folder = current_directory + os.path.sep + "__pycache__"
        if os.path.exists(test_folder) and os.path.isdir(test_folder):
            shutil.rmtree(test_folder)

        if os.path.exists(pycache_folder) and os.path.isdir(pycache_folder):
            shutil.rmtree(pycache_folder)

    def test_archetype(self):
        """
        Tests Archetype.create()

        :return:
        """
        # given
        self.cleanup()
        archetype = Archetype()
        path = os.path.join(os.getcwd().replace("tests", "src"), "template")

        # when
        result = archetype.create("test", path)

        # then
        self.assertEqual(result, os.path.join(os.getcwd(), "test"))

        if os.path.exists(result) and os.path.isdir(result):
            shutil.rmtree(result)
