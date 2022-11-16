import datetime  
print("Hi, welcome to the world clock")

while (True):
  ## get the name of the city from the user
  city = input("Enter city Name: ")

  ## get the current time 
  current_time = datetime.datetime.now()
  
  #print(current_time) # this prints our current time

  ## save hours, minutes and second of the current time 
  ## in their corresponding variables 
  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second
  
  ## check for case 1: the learner has typed Boston
  if city == "Boston":
    hour = hour - 4 

  ## check for case 2: the learner has typed Tokyo
  elif city == "Tokyo":
    hour = hour + 9

  ## check for case 3: the learner has typed Chicago
  elif city == "Chicago":
    hour = hour - 5 

  ## check for case 4: the learner has typed Seattle
  elif city == "Seattle":
    hour = hour - 7
    
   ##elif for case 5: the learner has typed Houston
  elif city =="Houston":
      hour = hour
   
   ##elif for case 6: the learner has typed Houston 
  elif city == "Kolkata":
    hour = hour + 5
    minutes = minutes + 30

  ##elif for case 7: the learner has typed Houston
  elif city == "Karachi":
    hour = hour + 5

  ##elif for case 8: the learner has typed Houston
  elif city == "Cairo":
    hour = hour + 2

  ##elif for case 9: the learner has typed Houston
  elif city == "Shanghai":
    hour = hour + 8
  
  ## check for case 10: the learner has typed exit
  elif city == "exit": 
    break

  ## if all cases fail, show the time for GMT    
  else:
    print(city, "is not added")
    city = "GMT" 

  # print the name of the city and the its corresponding time
  print(city, str(hour) + ":" + str(minute) + ":" + str(second))