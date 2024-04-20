#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.INFO)
logging.info(picdir);

try:
    logging.info("Starting clock..")
    epd = epd2in13_V4.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    # Drawing on the image
    font62 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 62)
    
    # # partial update
    logging.info("display time...")
    time_image = Image.new('1', (epd.height, epd.width), 255)
    #time_image = Image.new('RGB', (epd.height, epd.width), (255,0,0)) # This would be red if the display supports it
    time_draw = ImageDraw.Draw(time_image)
    epd.displayPartBaseImage(epd.getbuffer(time_image))
    while (True):
        time_draw.rectangle((1, 1, 250, 122), fill = 255)
        time_draw.text((5, 25), time.strftime('%H:%M:%S'), font = font62, fill = 0)
        epd.displayPartial(epd.getbuffer(time_image))
    
    logging.info("Clear...")
    epd.init()
    epd.Clear(0xFF)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    logging.info("Clear...")
    epd.init()
    epd.Clear(0xFF)
    exit()
