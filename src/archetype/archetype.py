import argparse
import os
import os.path
import shutil


class Archetype:
    """
    Base class of the python archetype
    """

    def __init__(self):
        """
        Constructor of the archetype class
        """
        self.placeholders = {
            "projectnameplaceholder" : {
                "prefix": "",
                "value": "",
                "postfix" : ""
            },
            "pythonversionplaceholder" : {
                "prefix": "python",
                "value": "",
                "postfix" : ""
            }
        }

    def replace_placeholder(
        self, filepath: str
    ) -> None:
        """
        Method for replacing the project placeholder in the given file

        :param filepath: file where placeholder should be replaced
        :return: None
        """
        # read input file
        with open(filepath, "rt") as fin:
            # read file contents to string
            data = fin.read()
            # replace all occurrences of the required string
            for placeholder_key, placeholder_value in self.placeholders.items():

                prefix = placeholder_value["prefix"]
                value = placeholder_value["value"]
                postfix = placeholder_value["postfix"]
                data = data.replace(placeholder_key, prefix + value + postfix)
        with open(filepath, "wt") as fin:
            # overrite the input file with the resulting data
            fin.write(data)

    def copy_all_files(self, src_folder: str, dest_folder: str) -> None:
        """
        Method for copying all files of a given base folder to a source folder

        :param src_folder: source folder to be copied
        :param dest_folder: destination folder to which files are copied
        :param projectname: projectname used to replace placeholder
        :param pythonversion: python version used for the created project
        :return: None
        """
        src_files = os.listdir(src_folder)
        for file_name in src_files:
            full_file_name = os.path.join(src_folder, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest_folder)
                if not file_name.endswith(".png"):
                    self.replace_placeholder(
                        os.path.join(dest_folder, file_name)
                    )
            elif os.path.isdir(full_file_name):
                if file_name == "__pycache__":
                    return
                elif file_name == "projectnameplaceholder":
                    name = self.placeholders["projectnameplaceholder"]["value"]
                else:
                    name = file_name
                folder = os.path.join(dest_folder, name)
                os.makedirs(folder, 0o775)
                self.copy_all_files(
                    os.path.join(src_folder, file_name),
                    os.path.join(dest_folder, name)
                )

    def create(
        self,
        projectname: str,
        pythonversion: str,
        targetfolder: str,
        delete_if_exist: bool = False,
        templatefolder: str = os.path.join(os.getcwd(), "template"),
    ) -> str:
        """
        Creates the project based on the given project name

        :param projectname: name of the project
        :param pythonversion: Python version used for the generated project
        :param targetfolder: Target folder where the generated project should be saved
        :param delete_if_exist: Flag that signals if an overlapping project should be deleted
        :param templatefolder: source folder of the project template
        :return: returns the path where the project was created
        """
        if projectname.isalnum():
            # get directory paths
            projectfolder = os.path.join(targetfolder, projectname)

            print(delete_if_exist)
            if delete_if_exist and os.path.exists(projectfolder):
                print("Deleting old project.")
                shutil.rmtree(projectfolder)

            # create target base folder and move all basic elements like Readme.md
            os.makedirs(projectfolder, 0o775)
            self.placeholders["projectnameplaceholder"]["value"] = projectname
            self.placeholders["pythonversionplaceholder"]["value"] = pythonversion
            self.copy_all_files(templatefolder, projectfolder)
            return projectfolder

        else:
            print("Projectname contains invalid symbols!")
            return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creating a tox compatible project")
    parser.add_argument(
        "-p",
        dest="projectname",
        help="The target name of the project. Special symbols are not allowed.",
    )
    parser.add_argument(
        "-v", dest="pythonversion", help="Targeted Python version (e.g. 3.7 or 3.9)."
    )
    parser.add_argument(
        "-t", dest="targetfolder", help="Targeted Base folder for the created project."
    )
    parser.add_argument(
        "-D", dest="deleteifexist", action='store_true', help="If there is a project with the same name in the target folder, delete it."
    )

    args = parser.parse_args()
    if args.projectname:
        projectname = args.projectname
    else:
        projectname = input(
            "What is the project`s name? Special symbols are not allowed in the "
            "name only alphanumeric characters!   "
        ).strip()

    if len(projectname) == 0:
        print("Project name must not be empty")
        exit(-1)

    if args.pythonversion:
        pythonversion = args.pythonversion
    else:
        pythonversion = input(
            "Which python version should be used (e.g. 3.9)?  "
        ).strip()

    if len(pythonversion) == 0:
        print("Python version must not be empty")
        exit(-1)

    if args.targetfolder:
        targetfolder = args.targetfolder
    else:
        targetfolder = input(
            "What is the target base folder for the created project?   "
        ).strip()

    if len(targetfolder) == 0:
        print("Target folder must not be empty")
        exit(-1)

    archetype = Archetype()
    res = archetype.create(projectname, pythonversion, targetfolder, args.deleteifexist)
    if res != "":
        print(f"Project successfully created: {res}")
    else:
        print("Some unknown error occurred")
