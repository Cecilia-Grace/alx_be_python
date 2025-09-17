goal_saving = 5000
month = 1
saving = 0
monthly_saving = 0

while int(saving) < goal_saving:
    monthly_saving = int(input(f"Month {month} saving: "))
    saving += monthly_saving
    month +=1
  
    if saving < goal_saving:
        print(f"You total is: {saving}")
    else:
        print(f"!!!GOAL OF $5000 REACHED. YOUR SAVINGS IS: ${saving}!!!")
        break    

