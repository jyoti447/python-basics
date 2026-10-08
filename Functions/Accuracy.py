def acc_pred(actual_pred , total_pred):
   return (actual_pred/total_pred)*100

actual_pred = float(input("enter here : "))
total_pred = float(input("enter your total here : "))

accuracy = (actual_pred/total_pred)*100
print("Accuracy ", accuracy ,'%')
