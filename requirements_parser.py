class RequirementsParser:

    @classmethod
    def open_requirements(cls, filename):
        """
        adding to dict all the dependencies

        Parameters:
        file (str): requirements.txt file location / requirements.txt file name

        Returns:
        output_set(set): contains all the dependencies

        """
        output_set = set()
        with open(filename, "r") as requirements:
            listed_file = requirements.readlines()

        for line in listed_file:
            line = line.strip()
            if "-r" in line:
                line = line.removeprefix('-r ')
                line = line.strip()
                if ".txt" not in line:
                    line = line + ".txt"
                output_set.update(cls.open_requirements(line))
            else:
                output_set.update(line)
        return output_set

    def create_final_requirements_file(self, filename):
        """
        create the output file

        Parameters:
        filename (str): contains all the dependencies

        Returns:
        None

        """
        result = self.open_requirements(filename)
        with open("requirements.txt", "w") as file:
            file.write("\n".join(result))
