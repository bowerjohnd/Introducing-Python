# 21-3 Map from Shapefile

# warped and bugged (as expected from the book)
# source file from: 
#   http://bit.ly/cultural-vectors --> https://www.naturalearthdata.com/downloads/110m-cultural-vectors/
#       
#       ne_110m_admin_1_states_provinces.shp

def display_shapefile(name, iwidth=500, iheight=500):
    import shapefile
    from PIL import Image, ImageDraw

    r = shapefile.Reader(name)
    mleft, mbottom, mright, mtop = r.bbox

    # map units
    mwidth = mright - mleft
    mheight = mtop - mbottom

    # scale map units to image units
    hscale = iwidth/mwidth
    vscale = iheight/mheight

    img = Image.new("RGB", (iwidth, iheight), "white")
    draw = ImageDraw.Draw(img)

    for shape in r.shapes():
        pixels = [
            (int(iwidth - ((mright - x) * hscale)), int((mtop - y) * vscale))
            for x, y in shape.points]

        if shape.shapeType == shapefile.POLYGON:
            draw.polygon(pixels, outline='black')
        elif shape.shapeType == shapefile.POLYLINE:
            draw.line(pixels, fill='black')

    img.show()

if __name__ == '__main__':
    import sys
    display_shapefile(sys.argv[1], 700, 700)