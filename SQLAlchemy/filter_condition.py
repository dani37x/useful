"""
This is a very useful trick to unpack parameters and values in the Flask Sqlalchemy ORM
"""

def show_row(self, column, value):
        filter_condition = {column: value}
        return self.query.filter_by(**filter_condition).first()
      
      
      
