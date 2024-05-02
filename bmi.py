print ("ET0735 (DevOps for AIoT) - Lab 2 - Introoduction to Python")
def calculate_bmi(height, weight):
    print ("Height = " + str(height))
    print ("Weight =" + str(weight))

    bmi = weight / (height * height)
    print ("BMI = " + str(bmi) )

    if bmi < 18.5 :
        bmi_status = "Under weight"
        bmi = -1

    elif bmi >= 18.5 or bmi <= 25.0: 
        bmi_status = "Normal Weight"
        bmi = 0

    else :
        bmi_status = "Over weight"
        bmi = 1

    print (str(bmi_status))
    return (bmi)

calculate_bmi(weight=57, height=1.73)