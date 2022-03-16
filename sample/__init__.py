class Person:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """

        print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)

class Teacher(Person):
    """
    A class to represent a teacher.

    ...

    Attributes
    ----------
    name : str
        first name of the teacher
    surname : str
        family name of the teacher
    age : int
        age of the teacher

    Methods
    -------
    info(additional=""):
        Prints the Teacher's name and age.
    """

    def __init__(self, name, surname, age, branch):
        """
        Constructs all the necessary attributes for the teacher object.

        Parameters
        ----------
            name : str
                first name of the teacher
            surname : str
                family name of the teacher
            age : int
                age of the teacher
            branch: str
                branch of the teacher
        """
        super().__init__(name, surname, age)
        self.branch = branch


