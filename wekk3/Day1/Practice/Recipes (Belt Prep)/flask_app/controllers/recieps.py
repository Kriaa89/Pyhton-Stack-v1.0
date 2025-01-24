from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.reciep import Recipe
from flask_app.models.user import User

# this route will render the dashboard page
@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('add_recipe.html')


# this route will handle the creation of the recipe
@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
        
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "under_30": request.form["under_30"],
        "cook_date": request.form["cook_date"],
        "user_id": session["user_id"]
    }
    Recipe.save(data)
    return redirect('/dashboard')

# this route will render the detail page
@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id" : id
    }  
    recipe = Recipe.get_one_with_user(data) # here we are getting the recipe with the user
    user = User.get_by_id({"id": session['user_id']}) # here we are getting the user that is logged in
    return render_template('detail_recipe.html', recipe=recipe, user=user)

# this route will render the edit page 
@app.route('/recipes/<int:id>/edit' )
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    
    recipe = Recipe.get_one(data) #here we are getting the recipe by id
    
    return render_template('edit.html', recipe=recipe)

# this route will handle the update of the recipe
@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form): #here we are validating the recipe 
        return redirect(f'/recipes/{id}/edit')
        
    data = {
        "id": id,
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "under_30": request.form["under_30"],
        "cook_date": request.form["cook_date"]
    } 
    Recipe.update(data) # here we are updating the recipe 
    return redirect('/dashboard')
    

@app.route('/recipes/delete/<int:id>/delete')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect('/dashboard')
