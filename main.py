from requirements_parser import RequirementsParser


def main():
    requirements_parser = RequirementsParser()
    path = input("Enter requirements.txt path:\n")
    requirements_parser.create_final_requirements_filename(path)


if __name__ == '__main__':
    main()
