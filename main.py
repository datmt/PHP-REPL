import sys
import time
import logging
import watchdog
import subprocess
from selenium import webdriver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
from selenium.webdriver.firefox.options import Options


driver_path = '/Users/myn/Downloads/geckodriver'
driver = None
my_url = 'http://localhost:9000'

def reload_browser():
    print('loading the URL')
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
    path = '/Users/myn/Desktop/lab/php-learn/'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    print('starting observer')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('eroror')
        observer.stop()
    observer.join()
