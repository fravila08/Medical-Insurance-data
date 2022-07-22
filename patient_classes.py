class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex= sex
        self.bmi= bmi
        self.child= num_of_children
        self.smoker= smoker
  #create a method to calculate the average insurance cost based on this statement 'estimated_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500'
    def estimated_insurance_cost(self):
        age_cal=250* self.age
        sex_cal= 128* self.sex
        bmi_cal=370* self.bmi
        child_cal= 425*self.child
        smoker_cal= 24000*self.smoker
        estimate_insurance_cost= age_cal - sex_cal + bmi_cal + child_cal + smoker_cal - 12500
        return f"{self.name}'s estimated insurance costs is ${estimate_insurance_cost} dollars."
  
  #method to change the age of a patient if necessary
    def update_age(self, new_age):
        self.age = new_age
        return f"{self.name} is now {self.age} years old."

  #method to update the num_of_children if necessary
    def update_children(self, children):
        self.child = children
        if self.child==1:
            return f"{self.name} has {self.child} child."
        else:
            return f"{self.name} has {self.child} children."

    def patient_profile(self):
        profile={
        "Name":self.name,
        "Age": self.age,
        "Sex": self.sex,
        "BMI": self.bmi,
        "Number of Children": self.child,
        "Smoker": self.smoker
        }
        return f"{self.name} {profile}"


#create patient1 and ensure the init is working correctly
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
#returns original estimate for insurance
print(patient1.estimated_insurance_cost())
#this changes patients age
print(patient1.update_age(26))
#returns updated insurance cost with new age
print(patient1.estimated_insurance_cost())
#updated number of children
print(patient1.update_children(1))

print(patient1.estimated_insurance_cost())

print(patient1.patient_profile())
