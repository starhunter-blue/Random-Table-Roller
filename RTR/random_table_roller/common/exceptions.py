class RandomTableRollerException(Exception):
    pass

class GUIException(RandomTableRollerException):
    pass

class UserInputException(GUIException):
    pass

class FileEmptyException(UserInputException):
    pass

class FaultyRandomizerException(UserInputException):
    pass

class FaultyTableException(FaultyRandomizerException):
    pass

class InvalidEntryNumberingException(FaultyTableException):
    pass

class DuplicateEntryException(FaultyTableException):
    pass

class EntryMissingException(FaultyTableException):
    pass

class UnclearTableNameException(FaultyTableException):
    pass

class EmptyTableException(FaultyTableException):
    pass

class TableNotYetParsedException(RandomTableRollerException):
    pass