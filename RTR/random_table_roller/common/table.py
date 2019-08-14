from exceptions import UnclearTableNameException

class Table:

    def __init__(self, raw_table):
        self.name = raw_table[0]
        self.raw_content = raw_table[1:]

        #Check if name follows naming convention
        unclear_name_exception = UnclearTableNameException(self.name 
                                                            + " does not follow table naming conventions. \n"
                                                            + "Tables must either start/end with </> for <Tables> \n"
                                                            + "or start/end with <</>> for <<Subtables>>."
                                                          )
        if self.name[:2] == "<<":
            if self.name[-2:] != ">>":
                raise unclear_name_exception
        elif self.name[0] == "<":
            if self.name[-1:] != ">" or self.name[-2:] == ">>":
                raise unclear_name_exception
        else:
            raise unclear_name_exception

        print(self.name)


test1 = []
test2 = []
test3 = []
test4 = []
test5 = []
test1.append("<Test1>")
test2.append("<<Test2>>")
test3.append("<Test3>>")
test4.append("<<Test4>")
test5.append("Test5")
Table(test2)
