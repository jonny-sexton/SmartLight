from flask import Flask, render_template
from markupsafe import escape
from colour import Colour

lightStrip = Colour()

app = Flask(__name__)

# landing page for controller
@app.route('/joker')
def joker():
    lightStrip.startFunction(lightStrip.colour([0,0,0]))
    return render_template('index.html')

# for solid colour setting
@app.route('/lightStrip/<rgbString>')
def blockColour(rgbString):
    rgbString = rgbString[4:-1]
    rgbList = rgbString.split(',')
    rgbList = list(map(int,rgbList))
    lightStrip.stopFunction()
    lightStrip.startFunction(lightStrip.colour(rgbList))
    return 'Colour %s' % escape(rgbString)
    
# ambient1
@app.route('/ambient1')
def ambient1():
    lightStrip.stopFunction()
    lightStrip.startFunction(lightStrip.ambient1)
    return 'ambient1'
    
# ambient2
@app.route('/ambient2')
def ambient2():
    lightStrip.stopFunction()
    lightStrip.startFunction(lightStrip.ambient2)
    return 'ambient2'

# strobe
@app.route('/strobe')
def strobe():
    lightStrip.stopFunction()
    lightStrip.startFunction(lightStrip.strobe)
    return 'Strobe'
# off
@app.route('/off')
def off():
    lightStrip.stopFunction()
    lightStrip.startFunction(lightStrip.off())
    return 'off'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')

