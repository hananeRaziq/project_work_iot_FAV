from PIL import Image
import requests
from io import BytesIO
import os
from  datetime import datetime
import logging # Logging: https://docs.python.org/3/howto/logging.html

# Setuo logging to file
#logging.basicConfig(filename=os.path.join("logs","app.log"),level=logging.INFO')
logging.basicConfig(level=logging.INFO)


def get_log_image():
    res = False
    image = None
    try:
        url='https://frenzy86.s3.eu-west-2.amazonaws.com/fav/logo.png'
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        res = True
        logging.debug("Image logo successfly pulled")
    except Exception as  e:
        logging.warning("Unable to get Image logo: %s",e)        
    return res,image


def get_current_date():
    return datetime.now().strftime("%d:%m:%Y")