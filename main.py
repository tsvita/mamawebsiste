from flask import Flask, render_template
app = Flask(
  __name__,
  static_folder='static')
cookieTitle = {
  "milkchoco": "Milk Chocolate Chip Cookies with Walnuts and Sea Salt",
  "ricekrispie" : "Rice Krispie Shortbread Cookies",
  "peanutmiso" : "Peanut Butter Miso Cookies",
  "chocolate" : "Chocolate Chocolate Chip Cookies",
  "oatmeal" : "Brown Butter Oatmeal Cookies with Golden Raisins",
  "molasses" : "Dark Chocolate Chip Cookies With Sesame, Buckwheat Flour and Walnuts",
  "peanut" : "Peanut Butter Cookies",
  "chocoshort" : "Chocolate Shortbread Cookies with Chocolate Chips and Sea Salt",
  "mandel" : "Mandel Bread with Toasted Almonds and Cinnamon Sugar",
  "chococherries" : "Chocolate Chocolate Chip Cookie with Dried Cherries and Toasted Pecans"

}

cookieDescription = {
  "milkchoco" : "Milk chocolate provides notes of caramel to this classic cookie.  It is caky on the inside and crisp on the edges. The flavors are heightened by sea salt.",
  "ricekrispie" : "This is what every sugar cookie wants to be - buttery, crunchy and addictive. The richness of the cookie is balanced by a bit of salt.  Makes a wonderful ice cream sandwich!",
  "peanutmiso" : "Umami meets peanut butter in delicious partnership. A bit of coarse sugar on the exterior of the cookie adds a delicate crunch.  The coarse sugar is a lovely contrast to the mild saltiness of the miso.",
  "chocolate" : "This deeply chocolatey chip cookie includes a hint of coffee.  It is lightly crisp on the outside, tender on the inside.",
  "oatmeal" : "Butter is good - brown butter is better! This cookie’s wonderful flavor is highlighted by a bit of sea salt.",
  "molasses" : "My most recent invention! These look like classic chocolate chip cookies but they are a delightful riff on an old favorite.  Sesame paste provides an earthy base note which blends beautifully with nutty buckwheat flour and a touch of molasses.",
  "peanut" : "Robust peanut butter flavor, not too sweet, shortbread texture . . . this is a favorite cookie to enjoy with a glass of milk.",
  "chocoshort" : "Rich chocolate chocolate chip shortbread is balanced with sea salt.  I add a bit of ground decaf espresso beans for added flavor.",
  "mandel" : "These buttery cookies are crisp all the way through, studded with toasted almonds and sprinkled with cinnamon sugar.",
  "chococherries" : "This richness of this chocolate cookie is balanced by slightly tart dried cherries. Toasted pecans add a bit of nutty goodness."
  
}

cookiePrice = {
  "milkchoco" : 30,
  "ricekrispie" : 30,
  "peanutmiso" : 30,
  "chocolate" : 30,
  "oatmeal" : 30,
  "molasses" : 30,
  "peanut" : 24,
  "chocoshort" : 24,
  "mandel" : 18,
  "chococherries" : 30,
}

shouldMicrowave = ['milkchoco', 'chocolate', 'molasses', 'chococherries']

@app.route('/')
def home():
  return render_template("home.html")
  
@app.route('/about')
def about():
  return render_template("about.html")  

@app.route('/lessons')
def lessons():
  return render_template("lessons.html")  

@app.route('/catering')
def catering():
  return render_template("catering.html") 

@app.route('/cookie/<cookie>') 
def cookiePage(cookie):
    return render_template(
      "cookie.html", 
      cookieTitle=cookieTitle.get(cookie),
      cookieDescription=cookieDescription.get(cookie),
      cookiePrice=cookiePrice.get(cookie),
      cookieSrc="/static/" + cookie + ".jpg",
      shouldMicrowave= cookie in shouldMicrowave,
    )  

@app.route('/cookies')
def cookies():
  return render_template("cookies.html")   

if __name__ == '__main__':
    app.run(host='0.0.0.0')
