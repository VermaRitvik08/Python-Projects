####### Class Patient ######## 
class Patient:
    def __init__(self,name=None,age=None,strand=None,has_condition=None,condition_name=None):
        self.name = name
        self.age = age
        self.strand = strand
        self.has_condition = has_condition
        self.condition_name = condition_name
