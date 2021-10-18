import os
import shutil
import unittest

from archetype.archetype import Archetype


class TestArchetype(unittest.TestCase):
    @staticmethod
    def cleanup() -> None:
        """
        Clean up the directory

        :return:
        """
        current_directory = os.getcwd()
        test_folder = os.path.join(current_directory, "template")
        pycache_folder = current_directory + os.path.sep + "__pycache__"
        if os.path.exists(test_folder) and os.path.isdir(test_folder):
            shutil.rmtree(test_folder)

        if os.path.exists(pycache_folder) and os.path.isdir(pycache_folder):
            shutil.rmtree(pycache_folder)

    def test_archetype(self) -> None:
        """
        Tests Archetype.create()

        :return:
        """
        # given
        self.cleanup()
        archetype = Archetype()
        path = os.path.join(
            os.getcwd().replace("tests", "src"), os.getcwd(), "template"
        )

        # when
        result = archetype.create(
            "test",
            "3.7",
            path,
            os.path.join(os.getcwd().replace("tests", "src"), "template"),
        )

        # then
        self.assertEqual(result, os.path.join(path, "test"))

        if os.path.exists(result) and os.path.isdir(result):
            shutil.rmtree(result)
