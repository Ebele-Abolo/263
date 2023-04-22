# Import Libraries below





# Define flask 


# Define upload_form() and route the webapp 
def upload_form():
	return render_template('upload.html')



@app.route('/', methods=['POST'])

# Define upload_video() to get video in defined folder and route the webapp  
	filename = secure_filename(file.filename)
	file.save(os.path.join('static/', filename))







# Define display_video() to Display video in defined folder and route the webapp  





if __name__ == "__main__":
    app.run(debug=True)














return render_template('upload.html', filename = filename)