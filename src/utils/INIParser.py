from configparser import ConfigParser


class INIParser:
    def __init__(self, filename):
        self.filename = filename

        self.parser = ConfigParser()

        self.parser.read(self.filename)

    def add_section(self, section):
        self.parser.add_section(section)

        with open(self.filename, "w") as file:
            self.parser.write(file)

    def add_value(self, section, option, value):
        self.parser.set(section, option, value)

        with open(self.filename, "w") as file:
            self.parser.write(file)

    def get_value(self, section, option):
        return self.parser.get(section, option)

    def update_value(self, section, option, value):
        old_value = self.parser.get(section, option)
        new_value = old_value.replace(old_value, value)

        self.parser.set(section, option, new_value)

        with open(self.filename, "w") as file:
            self.parser.write(file)
