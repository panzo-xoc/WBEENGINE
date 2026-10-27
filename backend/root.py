
from config import app
from flask import session, render_template, url_for, redirect, flash
from database import User, Product
from utils import get_avatar_path

"""@app.errorhandler(404)
def page_not_found(e):
    flash(f"Error: {e}")
    return redirect("/")

@app.errorhandler(500)
def page_not_found(e):
    flash(f"Error: {e}")
    return redirect("/")"""

@app.route('/')
def root():

    admins = User.query.filter_by(admin=True).all()
    sellers = User.query.filter_by(seller=True, admin=False).all()
    seller_ids = []
    for user in admins:
        seller_ids.append(user.id)
    for user in sellers:
        seller_ids.append(user.id)

    user_id = session.get('user_id')

    reviews = [
        ["+rep one hand menu with nice discount really he is a nice one and every one need to pay from him",
         "02.05.2022"],
        ["+Rep nice guy. Although he encountered some difficulties, he actively dealt with the problem.",
         "12.04.2022"],
        ["REP made an order for $470+ Made an ideal design taking into account all the requirements", 
         "01.02.2022"],
        ["+rep bought a custom work to redesign my script loader (external application)  The new design was ready in 10/10.",
         "27.12.2022"],
        ["+rep very clean and professional design, helpful but takes some time to respond but he’s a human tho.",
         "28.12.2022"],
        ["Crazy quality product, waited 11 days but it was worth it! I recommend [Took the service 3 times]",
         "11.09.2023"]
    ]

    return render_template('index.html', 
                            user_id=user_id, 
                            seller_ids=seller_ids,
                            reviews=reviews)
    
@app.route('/index')
def old_index():
    return redirect(url_for('root'), code=301)