from dataclasses import dataclass

@dataclass
class Person:
    name: str
    email: str
    title: str
    dept: str
    phone: str
    address: str
    city: str
    state: str

    def __str__(self):
        res = ''
        res += ("Name: " + self.name + "\n")
        res += ("Email: " + self.email + "\n")
        res += ("Title: " + self.title + "\n")
        res += ("Department: " + self.dept + "\n")
        res += ("Phone: " + self.phone + "\n")
        res += ("Address: " + self.address + "\n")
        res += ("City: " + self.city + "\n")
        res += ("State: " + self.state + "\n")
        return res

def rightstrip(person):
    person.name = person.name.rstrip()
    person.email = person.email.rstrip()
    person.title = person.title.rstrip()
    person.dept = person.dept.rstrip()
    person.phone = person.phone.rstrip()
    person.address = person.address.rstrip()
    person.city = person.city.rstrip()
    person.state = person.state.rstrip()
    return person