while True:

    outlook, humidity, windy = [x for x in input(
        "Input outlook('sunny' or 'cloudy' or 'windy'), humidity(integer), and windy('true' or 'false'):").split()]
    humidity = int(humidity)
    if windy == "t" or windy == "true":
        windy = True
    if windy == "f" or windy == "false":
        windy = False

    if outlook == "sunny" or outlook == "cloudy" or outlook == "rainny":
        if outlook == "cloudy":
            print("Play")
        elif outlook == "rainny":
            if windy:
                print("Not Play")
            else:
                print("Play")
        elif outlook == "sunny":
            if humidity <= 75:
                print("Play")
            else:
                print("Not Play")

    else:
        print('Invalid outlook . Please try again')
