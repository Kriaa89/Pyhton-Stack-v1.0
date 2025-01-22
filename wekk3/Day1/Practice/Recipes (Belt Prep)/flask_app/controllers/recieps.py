from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.reciep import Recipe

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('add_recipe.html')

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
            "user_id": session["user_id"],
            "name": request.form["name"],
            "description": request.form["description"],
            "instruction": request.form["instruction"],
            "under_30": request.form["under_30"],          
    }
    Recipe.save(data)
    return redirect('/dashboard')
    
@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id" : id
    }
    recipe = Recipe.get_one(data)
    return render_template('detail_recipe.html', recipe=recipe)

@app.route('/recipes/edit/<int:id>', methods=['POST'])
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    recipe = Recipe.get_one(data)
    return render_template('edit.html', recipe=recipe)

@app.route('/recipes/updates/<int:id>', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        data = {
            "id": request.form["recipes.id"],
            "name": request.form["name"],
            "user_id": request.form["user_id"],
            "description": request.form["description"],
            "instruction": request.form["instruction"],
            "under_30": request.form["under_30"],  
        }
        Recipe.update(data)
        return redirect('/dashboard')
    
    
@app.route('/recipes/delete/<int:id>/delete')
def deleteu_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect('/dashboard')
