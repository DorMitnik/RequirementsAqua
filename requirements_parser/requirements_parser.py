class RequirementsParser:

    def open_requirements(self, path):
        """
        adding to dict all the dependencies

        Parameters:
        file (str): requirements.txt file location / requirements.txt file name

        Returns:
        out_dict(dict): contains all the dependencies

        """
        output_dict = set()
        with open(path, "r") as requirements:
            listed_file = [line.strip() for line in requirements if not line == "\n"]

        for line in listed_file:
            if "-r" in line:
                line = line.removeprefix('-r ')
                output_dict.update(self.open_requirements(line))
                print(output_dict)
            else:
                output_dict.add(line)
        return output_dict

    def create_final_requirements_filename(self, path):
        """
        create the output file

        Parameters:
        result_list (str): contains all the dependencies

        Returns:
        None

        """
        output_dict = self.open_requirements(path)
        with open("requirements.txt", "w") as file:
            file.write("\n".join(output_dict))
