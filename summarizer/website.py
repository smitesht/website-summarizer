import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:

    def __init__(self, url):
        
        try:
            self.url = url
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content,"html.parser")
                self.title = soup.title.string if soup.title else "No title"

                for tag in soup.body(["script","style","img","input"]):
                    tag.decompose()
                
                self.text = soup.body.get_text(separator="\n", strip=True)
                #print(self.text)
            else:
                print(f"Website is not accessible: {url}")
        except Exception as e:
            print(f"An exception occurred during Website initialization: {e}")
        
        
       

        

            

        