# Python Practice 🚀🐍

This repository contains my small Python practice scripts as I learn and improve my programming skills.  
Each script is focused on a specific concept such as loops, conditionals, functions, and more.  

## 🎯 Purpose
- To track my learning journey in Python.  
- To practice writing clean and working code.  
- To build a foundation for larger projects in the future.  

## 🛠️ Topics Covered
- Introduction
- Variables
- Receiving Input
- Type Conversion
- Strings
- Formatted Strings
- String Methods
- Arithmetic Operations
- Operator Precedence
- Math Functions
- If Statements
- Logical Operators
- Comparison Operators 
- While Loops
- For loops
- Nested loops
- Functions
- Parameters
- Keyword Arguments 
- Return Statement

**Still addding on the topic I've covered**

## ✅ Example
**savings_goal.py**  
A small script that uses a `while` loop to help save money until a goal is reached.  

```python
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
```

## 🌱 Next Steps
I will keep adding more scripts as I continue learning.  
Stay tuned for projects that bring these concepts together!  
