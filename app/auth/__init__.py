from flask import Blueprint
auth=Blueprint('__auth__',__name__)
from . import views,forms
