class FootballTeamMember():
    def __init__(self, id: int, name: str, last_name: str, age: int):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age

    def focus(self):
        print(f"{self.name} está concentrándose para ejecutar sus labores.")
    
    def travel(self):
        print(f"{self.name} se encuentra en un vuelo con el equipo hacia el próximo partido.")

class Coach(FootballTeamMember):
    def __init__(self, id: int, name: str, last_name: str, age: int, id_federation: str):
        super().__init__(id, name, last_name, age)
        self.id_federation = id_federation

    def manage_match(self):
        print(f"{self.name} está dirigiendo el partido actual.")

    def lead_training(self):
        print(f"{self.name} está liderando el entrenamiento del equipo.")

class FootballPlayer(FootballTeamMember):
    def __init__(self, id: int, name: str, last_name: str, age: int, 
                shirt_number: int, demarcation: str):
        super().__init__(id, name, last_name, age)
        self.shirt_number = shirt_number
        self.demarcation = demarcation

    def play_match(self):
        print(f"¡{self.name} se encuentra jugando un partido justo ahora!")

    def do_training(self):
        print(f"{self.name} está entrenando para su próximo partido")

class MassageTherapist(FootballTeamMember):
    def __init__(self, id: int, name: str, last_name: str, age: int, 
                qualification: str, years_experience: int):
        super().__init__(id, name, last_name, age)
        self.qualification = qualification
        self.years_experience = years_experience

    def give_massage(self):
        print(f"{self.name} se encuentra dando un masaje a un miembro del equipo.")
