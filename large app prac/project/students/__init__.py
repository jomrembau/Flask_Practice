from flask import Blueprint

students_blueprint = Blueprint("students",__name__,
                              template_folder="templates")

from project.students import views