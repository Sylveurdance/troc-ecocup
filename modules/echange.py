#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect, request, session, flash, Blueprint
import conf
from helpers import user_required

bp = Blueprint('echange', __name__, url_prefix='/echange/')


@bp.route('')
@user_required
def echanges():
	username = session["username"]
	return render_template("echange/index.html", **locals())


@bp.route('/details')
@user_required
def details():
	username = session["username"]
	return render_template("echange/details.html", **locals())

