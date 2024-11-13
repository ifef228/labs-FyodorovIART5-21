from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    @abstractmethod
    def square(self):
        """площадь"""

    @abstractmethod
    def __repr__(self):
        """параметры"""
