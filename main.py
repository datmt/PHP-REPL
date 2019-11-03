import sys
import time
import logging
import watchdog
from selenium import webdriver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
from selenium.webdriver.firefox.options import Options


driver_path = 'C:/Users/MYN/bin/geckodriver.exe'
driver = None
my_url = 'http://localhost:9000'

def reload_browser():
    global driver
    if (driver == None):
        driver = webdriver.Firefox(options=Options(), executable_path=driver_path)
    driver.get(my_url)



class MyHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        print ("index file changed")
        #reload the browser here
        reload_browser()

if __name__ == "__main__":

    path = 'C:/Users/MYN/Desktop/lab/learn-php/'

    patterns = ['*.php']
    event_handler = MyHandler(patterns=patterns)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
