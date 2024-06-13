from functionsA1 import get_todos,write_todos
while True:
   x=input("Type add,show, edit or exit:")
   if 'add' in x:
       y=x[4:] + '\n'
       todos=get_todos()
       todos.append(y)
       write_todos(todos)
   elif 'show' in x:
       todos=get_todos()
       print("Your todos:")
       for number,item in enumerate(todos,start=1):
           print(f"{number}.{item.strip()}")

   elif 'edit' in x:

       todos=get_todos()
       for number,item in enumerate(todos,start=1):
           print(f"{number}.{item.strip()}")
       num=int(x[5:])
       new_todo=input("Enter the new todo:") + "\n"
       todos[num-1]=new_todo
       write_todos(todos)
       todos=get_todos()

       for number,item in enumerate(todos,start=1):
           print(f"{number}.{item.strip()}")

   elif 'exit' in x:
       print("bye:)")
       break
   else:
        print("Command is not valid :/")
