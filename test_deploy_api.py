import requests


def main():
    url = "https://deploy_api-1-e0877474.deta.app"
    data = {"x": 3, "y": 4}
    res = requests.post(url, json=data)
    print(res.json())


if __name__ == "__main__":
    main()
