from _datetime import datetime


class Weather:
    def __init__(self, weather_json):
        self.temperature = weather_json["main"]["temp"]
        self.pressure = weather_json["main"]["pressure"]
        self.humidity = weather_json["main"]["humidity"]
        self.temperature_min = weather_json["main"]["temp_min"]
        self.temperature_max = weather_json["main"]["temp_max"]
        try:
            self.time = weather_json["dt_txt"]
        except KeyError:
            self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conditions = []
        for condition in weather_json["weather"]:
            self.conditions.append(Condition(condition))

    def __str__(self):
        return (
            self.conditions[0].description
            + " ("
            + str(self.temperature)
            + "°C) at "
            + self.time
        )


class City:
    def __init__(self, name, id, coord):
        self.name = name
        self.id = id
        self.coord = coord

    def __str__(self):
        return self.name


class Condition:
    def __init__(self, condition_json):
        self.id = condition_json["id"]
        self.group = condition_json["main"]
        self.description = condition_json["description"].title()
        self.icon_id = condition_json["icon"]
