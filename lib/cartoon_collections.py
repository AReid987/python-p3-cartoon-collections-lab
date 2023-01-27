def roll_call_dwarves(names):
    for i, name in enumerate(names):
      print(f"{i + 1}. {name}")

def summon_captain_planet(calls):
    excited_calls = [f"{call.capitalize()}!" for call in calls]
    return excited_calls

def long_planeteer_calls(calls):

    result = False
    for call in calls: 
        if len(call) > 4: 
            result = True
            break;

    return result

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    result = None
    for cheese in cheeses: 
        if cheese in snacks:
          result = cheese
          break;

    return result