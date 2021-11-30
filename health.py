class Doctor: 
    
    #we have to write the self when defining __init__() functioninside a class which will hold the object which has called for this function
    
    def __init__(self):#One is initialization function , which is called when the object is created
        print("This is class Doctor")
        
      # A function which will get the wt &ht as parameter,calculate theBMI and print the BMI on console
    def BMI(weight, height): 
        bmi = weight/(height*height)
        print("Your BMI is "+str(bmi)) 
        
      # a function to check the heart  
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Great your heart rate is normal") 
        else:
            print("Your heart rate does not seem normal, please visit the clinic")
                
class Patient(Doctor): 
    
    def __init__(self, name, weight, height, heart_rates):
        self.patient_name = name
        self.patient_weight = weight
        self.patient_height = height
        self.patient_heart_rates = heart_rates
        
    def healthCheck(self):
        print("\n Paitent Name: "+ self.patient_name)
        Doctor.BMI(self.patient_weight, self.patient_height)
        Doctor.heart_rate(self.patient_heart_rates)
   
patient1  = Patient("Michael", 30, 0.9144, 80) 
patient1 .healthCheck()

patient2 = Patient("Jessica",  40, 1, 120) 
patient2.healthCheck()  


