import unittest

class TestHolaMundo(unittest.TestCase):
    def test_html_content(self):
        with open("index.html", "r", encoding="utf-8") as f:
            contenido = f.read()
        self.assertIn("Hola Mundo", contenido)

if __name__ == "__main__":
    unittest.main()
