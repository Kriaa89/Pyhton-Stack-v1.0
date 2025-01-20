# Users CRUD Project
This project is a Flask-based web application that demonstrates full CRUD (Create, Read, Update, Delete) operations on a user database. The main objective is to practice connecting Flask to a database and performing CRUD actions efficiently.

## Features

- **Create**: Add new users to the database. Upon successful creation, the application redirects to the "Read (One)" page to display the user's information.
- **Read (All)**: View a list of all users with an "Actions" column that provides options to view, edit, or delete each user.
- **Read (One)**: Display detailed information about a single user, including options to edit or delete the user.
- **Update**: Edit user information with a form pre-populated with the current user data. The `updated_at` field is updated upon successful submission, and the app redirects back to the "Read (One)" page.
- **Delete**: Remove a user from the database and redirect to the "Read (All)" page