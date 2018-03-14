class Person(object):
    def __init__(self, name, education, age, uniform):
        self.name = name
        self.education = education
        self.age = age
        self.uniform = uniform

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, education, age, uniform):
        super(Employee, self).__init__(name, education, age, uniform)

    def start_working(self):
        print("%s started working." % self.name)


class Programmer(Employee):
    def __init__(self, name, education, age, uniform):
        super(Programmer, self).__init__(name, education, age, uniform)

    def put_on(self):
        print("%s put on the uniform" % self.name)
