import requests
import argparse
import time
from bs4 import BeautifulSoup


def recursive(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = [a.get("href") for a in soup.find_all("a", href=True)]
    links = links[1:]

    for link in links:
        if link == "README":
            print(url + link)
            response = requests.get(url + link)

            content = response.content.decode(errors="ignore")
            if "flag" in content:
                print("FIND: " + content)
                exit()
        else:
            recursive(url + link)
        time.sleep(0.002)

def main(ip):
    url = "http://" + ip + "/.hidden/"
    recursive(url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default="10.13.248.135")
    args = parser.parse_args()
    main(args.ip)
