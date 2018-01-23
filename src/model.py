from abc import ABC, abstractmethod
from typing import Tuple, List
from numpy.random import RandomState


class Model(ABC):

    @abstractmethod
    def run(self) -> Tuple[List[float], List[float]]:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_population_size(self) -> int:
        pass


class AltMongooseModel(Model):

    def __init__(self, initial_population_size: int, a: float,
                 start: int, stop: int):
        self.__population_size = initial_population_size
        self.__a = a
        self.__start = start
        self.__stop = stop

    def run(self) -> Tuple[List[float], List[float]]:
        timeline = [self.__start]
        numbers_of_individuals = [round(self.__population_size)]
        for i in range(self.__start + 1, self.__stop + 1):
            timeline.append(i)
            new_population_size = self.__population_size - self.__a
            self.__population_size = new_population_size
            numbers_of_individuals.append(round(self.__population_size))
        return timeline, numbers_of_individuals

    def get_name(self) -> str:
        return 'Mongoose population dynamics'

    def get_population_size(self) -> int:
        return self.__population_size




class MongooseModel(Model):

    CAPACITY_GENERATOR_SEED = 47

    def __init__(self, initial_population_size: int,
                 r: float, h: float, k: float,
                 start: int, stop: int):
        self.__population_size = initial_population_size
        self.__capacity_generator = RandomState(MongooseModel.CAPACITY_GENERATOR_SEED)
        self.__r = r
        self.__h = h
        self.__k = k
        self.__start = start
        self.__stop = stop

    def run(self) -> Tuple[List[float], List[float]]:
        timeline = [self.__start]
        numbers_of_individuals = [round(self.__population_size)]
        for i in range(self.__start + 1, self.__stop + 1):
            timeline.append(i)
            l = self.__population_size * self.__r / self.__k
            capacity = self.__capacity_generator.binomial(self.__population_size, l)
            delta = (self.__r - self.__h) * self.__population_size - capacity
            new_population_size = self.__population_size + delta
            self.__population_size = new_population_size
            numbers_of_individuals.append(round(self.__population_size))
        return timeline, numbers_of_individuals

    def get_name(self) -> str:
        return 'Mongoose population dynamics'

    def get_population_size(self) -> int:
        return self.__population_size
