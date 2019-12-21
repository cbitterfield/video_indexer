'''
Created on Dec 21, 2019

A class to provide media actions on files.

@author: colinbitterfield
'''

import filetype
import os 
import sys
import magic
import hashlib

import logging
#Import Video Tools
import ffmpeg
# Import PDF Tools
from PyPDF2 import PdfFileReader as pdfR
# Image Magick Libraries
from wand.image import Image as WandImage
from wand.exceptions import WandException
from wand.image import Metadata as WandMetadata
# Python Image Library
import PIL
from PIL import Image as ImageP


class media_file():
    '''
    classdocs
    '''


    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        
    def __enter__(self,**kwargs):
        return self
    
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass    
    
    
    
    