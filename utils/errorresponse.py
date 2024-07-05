from flask import render_template
def errorresponse(errorMag):
   return render_template( 'error.html',errorMsg=errorMag)
