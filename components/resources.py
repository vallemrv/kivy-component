# @Author: Manuel Rodriguez <valle>
# @Date:   08-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-19T02:23:20+02:00
# @License: Apache license vesion 2.0

try:
    unichr(0xf090)
except:
    unichr = chr
import os


class Path():
    PATH_RES = os.path.join(os.path.dirname(__file__), "res")
    PATH_FONT = os.path.join(PATH_RES, "fonts")
    PATH_ICON = os.path.join(PATH_RES, "icon")
    PATH_IMG = os.path.join(PATH_RES, "img")
    FONT_AWESOME = os.path.join(PATH_FONT, "fa-solid-900.ttf")
    IMG_SHADOW = os.path.join(PATH_IMG, 'shadow.png')
    IMG_SHADOW_REC = os.path.join(PATH_IMG, 'shadow_rec.png')

class Res():
    #-- Start with A ---
    FA_ANGLE_RIGHT = unichr(0xf105)
    FA_ANGLE_LEFT = unichr(0xf104)


    #-- Start with B ---
    FA_BOOKS = unichr(0xf02d)
    FA_BAN = unichr(0xf05e)

    #-- Start with C ---
    FA_CUBE = unichr(0xf1b2)
    FA_CUBES = unichr(0xf1b3)
    FA_CHART = unichr(0xf080)
    FA_CHECK = unichr(0xf00c)
    FA_COGS = unichr(0xf085)
    FA_CREDIT_CARD = unichr(0xf09d)
    FA_CHEVRON_LEFT = unichr(0xf053)
    FA_CHEVRON_RIGHT = unichr(0xf054)
    FA_CHEVRON_UP = unichr(0xf077)
    FA_CHEVRON_DOWN = unichr(0xf078)
    FA_CUTLERY = unichr(0xf0f5)
    FA_CIRCLE = unichr(0xf1ce)


    #-- Start with D ---
    FA_DATABSE = unichr(0xf1c0)

    #-- Start with E ---
    FA_ENTER = unichr(0xf090)
    FA_EDIT = unichr(0xf303)
    FA_EXIT = unichr(0xf2f5)
    FA_ELLIPSE_V = unichr(0xf142) #Los tres puntitos
    FA_ELLIPSE_H = unichr(0xf141) #Los tres puntitos
    FA_EUR = unichr(0xf153)
    FA_EYE_SLASH = unichr(0xf070)
    FA_EYE = unichr(0xf06e)
    FA_ENVELOPE = unichr(0xf0e0)

    #-- Start with F ---
    FA_FOLDER = unichr(0xf07b)

    #-- Start with H ---
    FA_HANDSHAK_O = unichr(0xf2b5)
    FA_HEART = unichr(0xf004)


    #-- Start with L ---
    FA_LIST = unichr(0xf03a)
    FA_LEMON = unichr(0xf094)

    #-- Start with M --
    FA_MINUS = unichr(0xf068)

    #-- Start with N --
    FA_NETWORK = unichr(0xf6ff)

    #-- Start with P ---
    FA_PLUS = unichr(0xf067)

    #-- Start with Q ---
    FA_QUESTION = unichr(0xf128)

    #-- Start with R ---
    FA_REFRESH = unichr(0xf021)

    #-- Start with S ---
    FA_SPINNER = unichr(0xf110)
    FA_SEARCH = unichr(0xf002)

    #-- Start with T ---
    FA_TRUCK = unichr(0xf0d1)
    FA_TABLE = unichr(0xf0ce)
    FA_TRASH = unichr(0xf1f8)


    #-- Start with U ---
    FA_UNIVERSITY = unichr(0xf19c)
    FA_USERS = unichr(0xf0c0)

    #--- Start with P ---
    FA_PLANE = unichr(0xf1d8)



def hex_to_icon(hex):
    return unichr(hex)

def get_kv(name):
    name = name if "kv" in name else name+".kv"
    return os.path.join(Path.PATH_RES, 'kvs', name)
