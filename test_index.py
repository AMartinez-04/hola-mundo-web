from bs4 import BeautifulSoup

def test_h1_text():
    with open("index.html") as f:
        soup = BeautifulSoup(f, "html.parser")
        h1 = soup.find("h1")
        assert h1 is not None
        assert h1.text == "Hola Mundo"
