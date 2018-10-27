from GlyphsApp import *
import os

Height = 500
extraSpace = 1.2

myFont = Glyphs.font
selectedLayers = myFont.selectedLayers

master = myFont.masters[myFont.masterIndex]

Scale = Height / (myFont.upm * extraSpace)

offsetY = -master.descender

for thisLayer in selectedLayers:
    thisGlyph = thisLayer.parent
    if thisGlyph.unicode != None:
        name = thisGlyph.unicode
    else: 
        name = thisGlyph.name
    newPage(Height, Height)
    save()
    scale(Scale)
    offsetX = ((Height / Scale) - thisLayer.width) / 2
    translate(offsetX,offsetY)
    drawPath(thisLayer.completeBezierPath)
    restore()
    saveImage("~/Dropbox (Personnelle)/Quentin/WORK/TYPEFACES/2018-XXIX/50-JPG/%s.png" % (name)) 