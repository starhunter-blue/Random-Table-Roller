class RandomTableRollerException(Exception):
    pass

class GUIException(RandomTableRollerException):
    pass

class UserInputException(GUIException):
    pass

class NoRandomizerLoadedException(UserInputException):
    """Raised when user attempts to Randomize with no randomizer loaded"""

class FileEmptyException(UserInputException):
    pass

class FaultyRandomizerException(UserInputException):
    pass

class FaultyTableException(FaultyRandomizerException):
    pass

class InvalidEntryNumberingException(FaultyTableException):
    pass

class DuplicateEntryException(FaultyTableException):
    """Raised when a table contains the same entry number more than once"""

class EntryMissingException(FaultyTableException):
    pass

class UnclearTableNameException(FaultyTableException):
    pass

class EmptyTableException(FaultyTableException):
    pass

class UnclearSubEntryException(FaultyTableException):
    """Raised when the value after a --> in a Table Entry is unclear, usually because wrong [] use"""

class TableNotYetParsedException(RandomTableRollerException):
    """Raised when an operation is performed on a table that requires content that isn't parsed yet"""

class MissingTableException(FaultyTableException):
    """Raised when a subtable calls for a table taht isn't found in the randomizer"""