from abc import ABC, abstractmethod

class BaseRule(ABC):
    """
    Abstract bases class for all medical and logic rules.
    Enforces a .check(patient) method that returns (bool, reason)
    """

    @abstractmethod
    def check(self, patient):
        """"
        Must return a tuple: (shoud_alert: bool reason: str)
        """
        pass

    def name(self):
        """
        Returns the name of the rule for logging or display.
        """
        return self.__class__.__name__
    
    def explain(self):
        """
        OptionaL Human-friendly explanation of what the rule does.
        """
        return "No explaination provided."
    