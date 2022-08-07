# importing the necessary libraries
from flask import Flask, render_template, request

# importing the necessary modules
from raffle import first, second, third, bonus

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def homepage():
	# the function for the homepage
	if request.method == 'POST':
		name = request.form.get('name')
		fbet = request.form.get('fbet')
		sbet = request.form.get('sbet')
		tbet = request.form.get('tbet')
		bbet = request.form.get('bbet')
		first_amount, first_comment = first(fbet)
		second_amount, second_comment = second(sbet)
		third_amount, third_comment = third(tbet)
		bonus_amount, bonus_comment = bonus(bbet)
		total_won = first_amount + second_amount + third_amount + bonus_amount
		return render_template('results.html', name=name, first_comment=first_comment, fbet=fbet, second_comment=second_comment, sbet=sbet, third_comment=third_comment, tbet=tbet, bonus_comment=bonus_comment, bbet=bbet, total_won=total_won)
	return render_template('index.html')

# error pages
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app()