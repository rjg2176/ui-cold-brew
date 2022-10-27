from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

# Color Palette: ?

# Font Families: ?

# The dataset for the learn pages


learn_data = {

    "1": {
         "id": "1",
         "name": "First, you need a French Press!",
         "prev": "/",
         "path": "/learn/1",
         "next": "/learn/2",
         # Question type determines page placement logic in the template
         "type": "cart",
         "lesson_text": "Drag the french press into your shopping cart",
         # Our dictionary of images that we loop through to display on the page
         "images": {
             "1": ["https://de2wfhoo6xqi5.cloudfront.net/size/600/868/a80/74807c886f68ada920458f6a6ac16539f5.jpg", "Nope, that's a Keurig"],
             "2": ["https://m.media-amazon.com/images/I/71dMl1-+Z9L._AC_SL1500_.jpg","Yup, that's a French Press!"],
             "3": ["https://m.media-amazon.com/images/I/71Fzk5a1kXL.jpg", "Nope, that's a Coffee Filter"],

            #  "4": "https://www.freepnglogos.com/uploads/shopping-cart-png/shopping-cart-png-image-download-pngm-2.png",
         },
         "cart": "/static/images/shopping-cart-png-image-download-pngm-2.png",
         # The image ids that are accepted by the question's "cart"
         "accepting": ["2"],
         # The changing hints, depending on whether the user is correct or incorrect
         "reject_hint": "<b>Try again!</b> <br> A French Press has a large handle and plunger on top for pressing the coffee.",
         "accept_hint": "<b>Great Job!</b> <br> The plunger on top is for pressing the coffee.",
         "video" : ""
     },

    "2": {
         "id": "2",
         "name": "Can't have cold brew without Ground Coffee!",
         "prev": "/learn/1",
         "path": "/learn/2",
         "next": "/learn/3", 
         "type": "cart",
         "lesson_text": "Drag the coffee grounds into the shopping cart",
         "images": {
             "1": ["https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F9%2F2021%2F01%2F21%2Fhow-to-store-coffee-beans-FT-BLOG0121.jpg&q=60", "Nope, those are coffee beans!"],
             "2": ["https://www.thespruceeats.com/thmb/fddTYWjWUx4WG2tJtqN39nEYOBc=/1884x1413/smart/filters:no_upscale()/Herbal-tea-bag-582e1a743df78c6f6a29ef11.jpg", "Nope, that's tea!"],
             "3": ["https://media.istockphoto.com/photos/coffee-grind-texture-background-close-up-picture-id1220976686?k=20&m=1220976686&s=612x612&w=0&h=2P_e2Cd9InkZVpG55KfDNPmrEjLGLgbo4MOrLQnCg70=", "Yup, that's ground coffee!"],
         },
         "cart": "/static/images/shopping-cart-png-image-download-pngm-2.png",         
         "accepting": ["3"],
         "reject_hint": "<b>Try again!</b> <br> A French Press can only use ground coffee.",
         "accept_hint": "<b>Awesome!</b> <br> You can pick your favorite type of coffee to add to your cold brew (preferably coursely grounded beans).",
         "video" : ""
     },
     "3": {
         "id": "3",
         "name": "Pick Coffee Grounds",
         "prev": "/learn/2",
         "path": "/learn/3",
         "next": "/learn/4",
         "type": "cart",
         "lesson_text": "There are many types of coffee. Hover to learn more, and drag desired coffee to cart.",
         "images": {
             "1": ["https://casualblogging.com/wp-content/uploads/2017/07/light.jpg", "Light Roast - Most caffeine, acidic, rich"],
             "2": ["https://casualblogging.com/wp-content/uploads/2017/07/medium.jpg", "Medium Roast - Most body, balanced"],
             "3": ["https://casualblogging.com/wp-content/uploads/2017/07/dark.jpg", "Dark Roast - Strongest flavor, bitter, smokey"],
         },
         "cart": "/static/images/shopping-cart-png-image-download-pngm-2.png",
         "accepting": ["1","2","3"],
         "accept_hint": "<b>Nice Choice!</b> <br> As coffee roasts for longer, it loses caffeine and its original flavors, gaining a more smokey taste.",
         "video" : ""
     },
      "4": {
         "id": "4",
         "name": "Add Coffee and Water",
         "prev": "/learn/3",
         "path": "/learn/4",
         "next": "/learn/5", 
         "type": "slider",
         "lesson_text": "Use a 1:4 ratio of coffee to water. Always use filtered water for brewing coffee.",
         "images": {
             #"1": ["https://d29fhpw069ctt2.cloudfront.net/icon/image/49039/preview.svg", "1"],
             #"2": ["https://freefoodtips.com/wp-content/uploads/2017/08/Coffee_in_a_teaspoon-770x486.jpg", "1"],
             "1": ["https://media.istockphoto.com/photos/water-pouring-into-glass-picture-id1183424538?k=20&m=1183424538&s=612x612&w=0&h=ORPaUYOILJPmxIZAzY1yfvFYkDzGe_GLMVIAmRXyLGA=", "1"],
             "2": ["https://7omcu3a78zp40klds2w28klr-wpengine.netdna-ssl.com/wp-content/uploads/2019/09/GettyImages-746093487.jpg", "1"],
         },
         "accepting": ["1","2"],
         "accept_hint": "<b>Great Job!</b> <br> You should always have a 1:4 cups of ground coffee to cups of water ratio.",
         "cart":"https://cdn.shopify.com/s/files/1/0065/6182/products/8_cup_FP_grande.jpg?v=1588277175",
         "video" : "",
         "answer1": "4",
         "reject_hint": "Try again! Remember: <b> 1 cup coffee to 4 cups water</b>",
         "slider_question": "There is 1 cup of coffee. How much water do we need?"
     },
    # "3": {
    #      "id": "3",
    #      "name": "3. Water Type",
    #      "prev": "/learn/2",
    #      "path": "/learn/3",
    #      "next": "/learn/4",         
    #      "lesson_text": "1. Use Filtered Water! Always use filtered water for brewing coffee, regardless of brewing method. Use a charcoal filter(Brita jugs work), if possible. By using filtered water:",
    #      "image_1": "https://i.ibb.co/XxkmwRX/Screenshot-2022-04-18-082705.png",
    #      "image_2": "",
    #      "video" : ""
    #  },

# For now, we're commenting out the coffee blend info

    #  "4": {
    #      "id": "4",
    #      "name": "Step 2",
    #      "prev": "/learn/2",
    #      "path": "/learn/3",
    #      "next": "/learn/4",
    #      "lesson_text": "Coffee Type: There is a wide and overwhelming variety of coffees available. But some factors are more important when selecting a type and should help you narrow it down. Roast: the roast level gives you a good overall sense of what sort of taste profile to expect from a particular coffee and is often a good place to start when choosing your coffee.",
    #      "image_1": "https://i.ibb.co/7RN6N4n/Screenshot-2022-04-18-083955.png",
    #      "image_2": "",
    #      "video" : ""
    #  },
    #  "5": {
    #      "id": "5",
    #      "name": "Step 3",
    #      "prev": "/learn/3",
    #      "path": "/learn/4",
    #      "next": "/learn/5",
    #      "lesson_text": "Single Origin and Blends Single Origin: one that comes from a single source. It has the most original and unaltered flavour profile.Blends: two of more coffees that are mixed together. Coffee blend combines the elements and flavor profiles of various beans",
    #      "image_1": "https://i.ibb.co/HVc07b4/Screenshot-2022-04-18-084353.png",
    #      "image_2": "",
    #      "video" : ""
    #  },
    #  "4": {
    #      "id": "4",
    #      "name": "4. Measure Out Coffee",
    #      "prev": "/learn/3",
    #      "path": "/learn/4",
    #      "next": "/learn/5",
    #      "lesson_text": "Measure out desired quantity of ground coffee. Grounds to Water ratio - 1:4 :",
    #      "image_1": "https://i.ibb.co/Lk5Bcy2/Screenshot-2022-04-18-084515.png",
    #      "image_2": "",
    #      "video" : ""
    #  },
    #  "5": {
    #      "id": "5",
    #      "name": "Mix in French Press",
    #      "prev": "/learn/4",
    #      "path": "/learn/5",
    #      "next": "/learn/6",
    #      "type": "slider",
    #      "lesson_text": "Combine room-temperature water and freshly ground coffee in a large French press. 1. Add coffee grounds. 2. Add filtered water. 3. Stir several times with spoon",
    #      "image_1": "https://i.ibb.co/GPpfhJN/unnamed.gif",
    #      "image_2": "",
    #      "video" : ""
    #  },
    "5": {
          "id": "5",
          "name": "Mix in French Press",
          "prev": "/learn/4",
          "path": "/learn/5",
          "next": "/learn/6",
          "lesson_text": "Combine room-temperature water and ground coffee in your press. Stir the mixture.",
          "image_1": "https://i.ibb.co/GPpfhJN/unnamed.gif",
          "image_2": "",
          "video" : ""
      },
     "6": {
         "id": "6",
         "name": "Refrigeration Instructions",
         "prev": "/learn/5",
         "path": "/learn/6",
         "next": "/learn/7",
         "lesson_text": "Put on lid, leave plunger up, and then refrigerate for 16-24 hours. (If the French press with the plunger up is difficult to store in your refrigerator, cover the pitcher with plastic wrap, foil or a plate.)",
         "image_1": "",
         "image_2": "",
         "video" : "https://youtube.com/embed/hSSRf5NNa0A?start=85&end=112"
     },
     "7": {
         "id": "7",
         "name": "Plunge",
         "prev": "/learn/6",
         "path": "/learn/7",
         "next": "/learn/8",
         "lesson_text": "Take the top off, get a spoon, and slowly break the crust (coffee that's floated to the top). Place the lid on the French press and slowly press the plunger all the way down. Pour the cold brew concentrate into a large glass jar or pitcher.",
         "image_1": "https://cdn.shopify.com/s/files/1/0760/2923/files/Press-Slow.gif?4349006294389003401",
         "image_2": "",
         "video" : ""
     },
     "8": {
         "id": "8",
         "name": "Strain",
         "prev": "/learn/7",
         "path": "/learn/8",
         "next": "/learn/9",
         "lesson_text": "To strain, simply place a coffee filter into a small fine-mesh sieve, or drape your cloth over the sieve. Place it over a pitcher or liquid measuring cup, and pour the concentrate through it. That’s it! ",
         "image_1": "https://cookieandkate.com/images/2018/09/filtering-cold-brew-coffee-through-coffee-filter-768x528.jpg",
         "image_2": "",
         "video" : ""
     },
     "9": {
         "id": "9",
         "name": "Dilute and Serve",
         "prev": "/learn/8",
         "path": "/learn/9",
         "next": "/quiz/start",
         "lesson_text": "To serve, dilute 1/2 cup cold brew with 1/2 cup water or milk. If serving with ice, use the ice with 1/2 cup cold brew concentrate with 1/4 cup water.",
         "image_1": "https://i.ibb.co/cky9Wpj/unnamed-1.gif",
         "image_2": "",
         "video" : ""
     }
}

# The dataset for the quiz pages

quiz_data = {

    "1": {
        "id": "1",
        "name": "Question 1",
        "prev": "/quiz/",
        "path": "/quiz/1",
        "next": "/quiz/2",
        "type": "slider",
        "question": "When making cold brew in your French Press, how long should you refrigerate the coffee mixture?",
        "answer_min": "16",
        "answer_max": "24",
        "answer_range": ["0","36"],
        # "type": "draggable",
        # "data1": "",
        "image": "https://cdn.apartmenttherapy.info/image/upload/v1558645330/k/archive/02679861ca06776c0bf692c7935efe740b6b408d.jpg",
        "alt": "french press in the fridge",
        "user_input": ""
    },

    "2": {
        "id": "2",
        "name": "Question 2",
        "prev": "/quiz/1",
        "path": "/quiz/2",
        "next": "/quiz/3",
        "type": "slider",
        "question": "Drag the slider to indicate an appropriate amount of water to use for 2 cups of coffee",
        "answer_min": "8",
        "answer_max": "8",
        "answer_range": ["0","16"],
        "image": "https://www.topoffmycoffee.com/wp-content/uploads/2018/06/How-Hot-Should-The-Water-Be-In-A-French-Press.jpg",
        "alt": "water being poured into french press",
        "user_input": ""
     },
     "3": {
        "id": "3",
        "name": "Question 3",
        "prev": "/quiz/2",
        "path": "/quiz/3",
        "next": "/quiz/4",
        "type": "slider",
        "question": "How many cups of water or milk should you add to dilute 3 cups of cold brew?",
        "answer_min": "3",
        "answer_max": "3",
        "answer_range": ["0","10"],
        "image": "https://rachelsteenland.com/wp-content/uploads/2019/07/cold-brew-coffee-how-to-guide-recipe.jpg",
        "alt":"milk being poured into a glass of cold brew coffee",
        "user_input": ""
     },

    "4": {
        "id": "4",
        "name": "Question 4",
        "prev": "/quiz/3",
        "path": "/quiz/4",
        "next": "/quiz/5",
        "type": "mcq",
        "question": "After measuring out ingredients for the cold brew, what do you do first?",
        "choices": {
            "1": "Plunge the French Press to compress the ingredients.",
            "2": "Refrigerate the mixture inside of the French Press.",
            "3": "Combine room temperature water with ground coffee in your French Press and stir.",
            "4": "Dilute your mixture by adding water or milk.",
        },
        "answer": "3",
        "user_input": ""
     },

    "5": {
        "id": "5",
        "name": "Question 5",
        "prev": "/quiz/4",
        "path": "/quiz/5",
        "next": "/quiz/6",
        "type": "mcq",
        "question": "What is the correct ordering of steps for making cold brew?",
        "choices": {
            "1": "Measure ingredients, Dilute, Mix ingredients, Strain mixture, Plunge French Press, Refrigerate",
            "2": "Measure ingredients, Mix ingredients, Refrigerate, Plunge French Press, Strain mixture, Dilute",
            "3": "Measure ingredients, Refrigerate, Mix ingredients, Strain mixture, Plunge French Press, Dilute",
            "4": "Measure ingredients, Mix ingredients, Refrigerate, Strain mixture, Plunge French Press, Dilute",
        },
        "answer": "2",
        "user_input": ""
     },

    "6": {
        "id": "6",
        "name": "Question 6",
        "prev": "/quiz/5",
        "path": "/quiz/6",
        "next": "/quiz/results",
        "type": "mcq",
        "question": "Which of the following is true?",
        "choices": {
            "1": "Medium roast coffee has the least amount of caffeine.",
            "2": "Dark Roast coffee has the most acidic flavor.",
            "3": "Coffee tends to taste more bitter as it is roasted.",
            "4": "Light roast coffee tastes the most smokey.",
        },
        "answer": "3",
        "user_input": ""
     },

}
counter = 0

# ROUTES

# Home and search route (the search form redirects to /)

@app.route("/")
def home():

    return render_template("home.html")

# Routes for viewing a specific page

@app.route("/learn/<id>")
def learn_page(id=None):
    global learn_data

    # Gets a single item with the given id
    item = learn_data[id]

    return render_template("template_learn.html", id=id, item=item) 

@app.route("/quiz/<id>", methods=['GET'])
def quiz_page(id=None):
    global quiz_data
    global counter
    # Return quiz home page
    if id == "start":
        counter = 0
        return render_template("quiz_start.html") 

    if id == "results":
        return render_template("quiz_results.html", counter=counter) 

    item = quiz_data[id]
    return render_template("template_quiz.html", id=id, item=item, counter=counter)


@app.route("/check_answer", methods=['POST'])
def check_answer():
    print(request.method)
    if request.method == 'POST':
        global counter
        print("Check Answer")
        counter += 1
        print(counter)
        return jsonify()

if __name__ == "__main__":
   app.run(debug = True)