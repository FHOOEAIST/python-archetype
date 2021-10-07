import os
import os.path
import shutil


class Archetype(object):
    """
    Base class of the python archetype
    """

    projectnameplaceholder = "projectnameplaceholder"
    pythonversionplaceholder = "pythonversionplaceholder"

    def replace_placeholder(self, filepath: str, projectname: str, pythonversion: str) -> None:
        """
        Method for replacing the project placeholder in the given file

        :param filepath: file where placeholder should be replaced
        :param projectname: projectname used to replace placeholder
        :param pythonversion: python version used for the created project
        :return: None
        """
        # read input file
        with open(filepath, "rt") as fin:
            # read file contents to string
            data = fin.read()
            # replace all occurrences of the required string
            data = data.replace(self.projectnameplaceholder, projectname).replace(self.pythonversionplaceholder,
                                                                                  "python" + pythonversion)

        with open(filepath, "wt") as fin:
            # overrite the input file with the resulting data
            fin.write(data)

    def copy_all_files(self, src_folder: str, dest_folder: str, projectname: str, pythonversion: str) -> None:
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
                        os.path.join(dest_folder, file_name), projectname, pythonversion
                    )
            elif os.path.isdir(full_file_name):
                if file_name == "__pycache__":
                    return
                elif file_name == self.projectnameplaceholder:
                    name = projectname
                else:
                    name = file_name
                folder = os.path.join(dest_folder, name)
                os.makedirs(folder, 0o775)
                self.copy_all_files(
                    os.path.join(src_folder, file_name),
                    os.path.join(dest_folder, name),
                    projectname,
                    pythonversion
                )

    def create(
        self,
        projectname: str,
        pythonversion: str,
        targetfolder: str,
        templatefolder: str = os.path.join(os.getcwd(), "template")
    ) -> str:
        """
        Creates the project based on the given project name

        :param projectname: name of the project
        :param pythonversion: Python version used for the generated project
        :param targetfolder: Target folder where the generated project should be saved
        :param templatefolder: source folder of the project template
        :return: returns the path where the project was created
        """
        if projectname.isalnum():
            # get directory paths
            projectfolder = os.path.join(targetfolder, projectname)

            # create target base folder and move all basic elements like Readme.md
            os.makedirs(projectfolder, 0o775)
            self.copy_all_files(templatefolder, projectfolder, projectname, pythonversion)
            return projectfolder

        else:
            print("Projectname contains invalid symbols!")
            return ""


if __name__ == "__main__":
    projectname = input(
        "What is the project`s name? Special symbols are not allowed in the "
        "name only alphanumeric characters!   "
    ).strip()

    if len(projectname) == 0:
        print("Project name must not be empty")
        exit(-1)

    pythonversion = input("Which python version should be used (e.g. 3.9)?  ").strip()

    if len(pythonversion) == 0:
        print("Python version must not be empty")
        exit(-1)

    targetfolder = input("What is the target base folder for the created project?   ").strip()

    if len(targetfolder) == 0:
        print("Target folder must not be empty")
        exit(-1)

    archetype = Archetype()
    res = archetype.create(projectname, pythonversion, targetfolder)
    if res != "":
        print(f"Project successfully created: {res}")
    else:
        print("Some unknown error occurred")
