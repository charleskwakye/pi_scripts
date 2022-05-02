 #!/usr/bin/env python3
from textwrap import fill
import time
import busio
import digitalio
import board
import adafruit_pcd8544
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
#Initialize display
dc = digitalio.DigitalInOut(board. D23) # data/command
cs1 = digitalio.DigitalInOut(board.CE1) #chip select CE1 for display
reset = digitalio.DigitalInOut(board.D24) # reset
display = adafruit_pcd8544.PCD8544 (spi, dc, cs1, reset, baudrate= 1000000)
display.bias = 4
display.contrast = 60
display.invert = True

# Clear the display. Always call show after changing pixels to make the display update visible!
display.fill(0)
display.show()

#Load default font
font = ImageFont.load_default()
#font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 10)

#Get drawing object to draw on image 
image = Image.new('1',(display.width, display.height))
draw = ImageDraw.Draw(image)

#Draw a white filled box to clear the image
draw.rectangle((0,0, display.width,display.height),outline=255, fill=255)

#write some text
nummer = 4
draw.text((1,0),'Thomas More!', font=font)
draw.text((1,8),'IT factory',font=font)
draw.text((1,16),'Campus Geel', font=font)
draw.text((1,25),'Kleinhoefstr', font=font)
draw.text((1,32),(str(nummer)), font=font)
display.image(image)
display.show

