class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last


class Supervisor(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password


class Chefs(Employees):
    def leave_request(self, days):
        return f"May I take a leave for {str(days)}"


adrian = Supervisor('Adrian', 'A', 'password123')

emily = Chefs('Emily', 'E')
juno = Chefs('Juno', 'J')

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)
