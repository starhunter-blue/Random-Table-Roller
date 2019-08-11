class RandomTableRollerException(Exception):
    pass

class GUIException(RandomTableRollerException):
    pass

class UserInputException(GUIException):
    pass

class FileEmptyException(UserInputException):
    pass