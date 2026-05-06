import json
import os
data_file = "habit.json"
default_profile = {
    "name":"",
    "level":1,
    "xp":0,
    "tasks":{}}

def pre_profile():
    if not os.path.exists (data_file):
        return default_profile.copy()
    try:
        with open(data_file,"r") as file:
            return json.load(file)
    except(json.JSONDecodeError, PermissionError):
        return default_profile.copy()



player=pre_profile()
if player["name"] =="":
    player["name"]=input("Entre your name:- ").strip().title()
    try:
        with open(data_file,"w") as file:
            json.dump(player,file,indent=4)
    except IOError :
      print("could not found saved file ")
    print("\n ========SOLO==LEVELING==HABIT==TRACKER=========")
    print("          welcome:PLAYER",(player["name"]))
    print(" ===============================================")

else:
    

    print("\n========SOLO==LEVELING==HABIT==TRACKER=========")
    print("          welcome:PLAYER",(player["name"]))
    print(" ================================================")
def add_tasks():
        print("================ADD==TASKS================")
        tasks_name= input("Entre tasks name :- ").title().strip()
        priority = input("Entre priority(High / Medium / Low ):- ").title().strip()
        no_tasks = f"Tasks{len(player['tasks'])+1}"
        player["tasks"][no_tasks]={
            "tasks name":tasks_name,
            "priority":priority,
            "status":"Pending"
        }
        try:
          
          with open(data_file,"w") as file:
              json.dump(player,file,indent=4)
          print(f"\n Task is '{tasks_name}'scuuessfully added to the file")
        except IOError:
            print("could not save tasks to your file")    
def complete_task():
    print("\n============= COMPLETED QUEST =============")
    pending_tasks={}
    for tid , tinfo in player["tasks"].items():
        if tinfo["status"] == "Pending":
               pending_tasks[tid] = tinfo
               print(f"[{tid}]{tinfo['tasks name']} | Priority: {tinfo['priority']}")
    if not pending_tasks:
        print("no quest available")
        return
    choice = input("\nEntre the ID of completed quest (eg:- Tasks1): ").strip()
    if choice in pending_tasks:
        task = player["tasks"][choice]
        task["status"] = "Completed"
        add_xp = 0
        if task["priority"] == "High":
            add_xp = 50
        elif task["priority"] == "Medium":
            add_xp =30
        else:
            add_xp = 10
        player["xp"] += add_xp
        print(f"Tasks completd you have gained +{add_xp} XP!")
        if player["xp"] >= 100:
            player["level"] +=1
            player["xp"] -= 100
            print(f"Level UP! now you are at {player['level']} ")
        try:
                   with open(data_file,"w") as file:
                    json.dump(player,file,indent =4)
        except IOError:
                print("Could not save progress to the file ")
    else:
        print("Invalid tasks ID!")
while True:
     print(f"\n-----Player:{player['name']} | Level:{player['level']} | Xp:{player['xp']}/100-----")
     print("1. View List Tasks")
     print("2. Add New Tasks")
     print("3. To Complete Tasks")
     print("4. Exit")
     choice = input("Type an option 1--4:----> ").strip()
     if choice == "1":
          print("\n ================ TASK'S LIST ================ ")
          if not player["tasks"]:
               print("There are no tasks ")
          else:
               for tid,tinfo in player["tasks"].items():
                    print(f"[{tid}]{tinfo['tasks name']} | priority: {tinfo['priority']} | Status: {tinfo['status']}")
     elif choice == "2":
          add_tasks()
     elif choice == "3":
          complete_task()
     elif choice == "4":
          
          pending_exit = []
          for itd, tinfo in player["tasks"].items():
               if tinfo["status"] == "Pending":
                    pending_exit.append(f"[{tid}] {tinfo['tasks name']} | Priority: {tinfo['priority']}")
          if pending_exit:
              for tasks_line in pending_exit:
                print(tasks_line)
                print("\nDon't forget to complete those tasks")
          else:
             print("======YOU HAVE COMPLETED TODAY'S TASKS=====")
             print("======E_X_I_T======")
                              
             break
     else:
          print("Invalid choice: please type a number between 1 to 4")
          

                
