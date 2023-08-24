class DatabaseOperationException(Exception):
     def __init__(self, line:str, message = "Something went wrong during database operation") -> None:
          self.message = message
          super().__init__(f"{message} :: line[{line}]")