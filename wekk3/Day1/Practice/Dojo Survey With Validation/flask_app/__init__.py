from  flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = 'keep it'

