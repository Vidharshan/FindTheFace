import time
import selenium
from selenium import webdriver
#'C:\Users\Acer\Desktop\image classification project-(SportsmanWho)\chromedriver.exe'
DRIVER_PATH='./chromedriver.exe'
selenium.__file__
wd = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wd.get('https://google.com')
search_box=wd.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('Dogs')
wd.quit()
def fetch_image_urls(query: str,max_links_to_fetch: int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)
        search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
        
fetch_image_urls('Dog',30,wd)