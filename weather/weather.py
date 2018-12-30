class Weather:
    def __init__(self, weather_json):
        self.temperature = weather_json['main']['temp']
        self.pressure = weather_json['main']['pressure']
        self.humidity = weather_json['main']['humidity']
        self.temperature_min = weather_json['main']['temp_min']
        self.temperature_max = weather_json['main']['temp_max']
        self.weather_name = weather_json['weather']['name']
        self.city = City(weather_json['name'], weather_json['id'],
                         (weather_json['coord']['lat'], weather_json['coord']['lon']))

    def __str__(self):
        return self.weather_name + ' (' + self.temperature + '°C)'

    def short_string(self):
        res = ''
        res += self.weather_name
        res += ' ('
        res += self.temperature + '°C) '
        res += ' in '
        res += self.city
        return res


class City:
    def __init__(self, name, id, coord):
        self.name = name
        self.id = id
        self.coord = coord

    def __str__(self):
        return self.name
