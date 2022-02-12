from requests import get


def get_location_info():
    return get("http://freegeoip.app/json/").json()


if __name__ == "__main__":
    print(get_location_info())
