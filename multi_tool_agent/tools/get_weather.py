import httpx


def get_weather(city: str) -> dict:
    print(f"get_weather called with city: {city}")
    # if city.lower() == "大阪":
    #     return {
    #         "status": "success",
    #         "report": (
    #             "The weather in Osaka is sunny with a temperature of 25 degrees"
    #             " Celsius (41 degrees Fahrenheit)."
    #         ),
    #     }
    # else:
    #     return {
    #         "status": "error",
    #         "error_message": f"Weather information for '{city}' is not available.",
    #     }
    try:
        response: dict = httpx.get("https://www.jma.go.jp/bosai/common/const/area.json").json()
        offices = response["offices"]
        searched = {
            offices[key]["name"]: key
            for key in offices
            if city in offices[key]["name"] or city in offices[key]["enName"]
        }
        result = dict()
        for code in searched.values():
            response: list = httpx.get(f"https://www.jma.go.jp/bosai/forecast/data/forecast/{code}.json").json()
            for it in response:
                time_series: list = it["timeSeries"]
                for it in time_series:
                    areas: list = it["areas"]
                    for it in areas:
                        area = it["area"]["name"]
                        weathers = it.get("weathers", None)
                        if weathers is not None:
                            result[area] = weathers
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"An error occurred while fetching weather data: {str(e)}",
        }


if __name__ == '__main__':
    city = "東京"
    weather_info = get_weather(city)
    print(weather_info)
