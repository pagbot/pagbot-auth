from abc import ABCMeta, abstractmethod


class IAuth(metaclass=ABCMeta):

    @abstractmethod
    async def create(self):
        pass
