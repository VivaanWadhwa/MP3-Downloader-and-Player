name=input("Name")
age=int(input("Age"))
bodyTemp=int(input("Body Temperature in deg.F"))
symptoms=input("Symptoms, if any (Fever/Cold/Cough/Breathlessness/Loss of Taste or Smell) otherwise type no")
medHistory=input("Medical History, if any (Diabetes/Hypertension/Heart Diseases/Lung Diseases) otherwise type no")
contact=input("Recent contact with a person tested positive for Covid-19 please type y or n")
if contact == 'y' or bodyTemp >= 102:
    print ("You have moderate risk of infection")
elif symptoms != 'No' or symptoms != 'No' or bodyTemp >= 99.5 and bodyTemp <= 101.9 or medHistory != 'no' or medHistory != 'No' or age>=60 or age<=15:
    print ("you have low risk of infection")
else:
    print ("you are safe")   