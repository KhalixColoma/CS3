class lab:
    def __init__(self, room_number):
        self.room_number=room_number

class technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None

    def assign_lab(self, lab_obj):
        self.lab_obj = lab_obj


chem_lab = lab("302")
mr_cruz = technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)
print(mr_cruz.lab_obj.room_number)
