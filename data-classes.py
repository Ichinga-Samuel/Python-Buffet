import dataclasses


@dataclasses.dataclass
class Person:
    f_name: str
    l_name: str
    age: int
    m: dataclasses.InitVar[int]
    # Country: str = 'Nigeria'

    def __post_init__(self, m: int):
        print(m, self.age)


@dataclasses.dataclass(unsafe_hash='False')
class User(Person):
    tel: float
    em: int = dataclasses.field(default_factory=list)

    def __repr__(self):
        return f'**User({self.__dict__}, {self.__dict__}, {self.__dict__}, {self.__dict__}, {self.__dict__})'


me = Person('Ichinga', 'Samuel', 24, 9)
user = User('Ichinga', 'Samuel', 24, 5.6, [1, 3],  9)
