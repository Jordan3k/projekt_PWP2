
from dataclasses import asdict
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import CalculationResult
from app.db import db
from app.services.calculator import Calculator, CalculatorError


bp = Blueprint("app", __name__)
calculator = Calculator()




@bp.route("/", methods=["GET", "POST"])
def index():
    """Render calculator and handle calculations."""
    expression = ""
    result = None


    if request.method == "POST":
        expression = (request.form.get("expression") or "").strip()
    try:
        result = calculator.evaluate(expression)
    except CalculatorError as exc: # pragma: no cover - flash feedback
        flash(str(exc), "error")
        result = None


    return render_template("index.html", expression=expression, result=result)




@bp.post("/save")
def save():
    """Persist the last computed result to the database."""
    expression = (request.form.get("expression") or "").strip()
    result = request.form.get("result")


    if not expression or result is None:
        flash("Brak wyrażenia lub wyniku do zapisania.", "error")
        return redirect(url_for("app.index"))

    try:
        # Validate by re-evaluating to avoid tampering
        evaluated = calculator.evaluate(expression)
        if str(evaluated) != str(result):
            flash("Wynik niezgodny z obliczeniami – odśwież i spróbuj ponownie.", "error")
            return redirect(url_for("app.index"))
    except CalculatorError as exc:
        flash(str(exc), "error")
        return redirect(url_for("app.index"))


    entry = CalculationResult(
    expression=expression,
    result=str(result),
    created_at=datetime.utcnow(),
    )
    db.session.add(entry)
    db.session.commit()


    flash("Wynik zapisany!", "success")
    return redirect(url_for("app.history"))




@bp.get("/history")
def history():
    """List saved results."""
    records = CalculationResult.query.order_by(CalculationResult.created_at.desc()).all()
    return render_template("history.html", records=records)




@bp.post("/history/clear")
def clear_history():
    CalculationResult.query.delete()
    db.session.commit()
    flash("Historia wyczyszczona.", "success")
    return redirect(url_for("app.history"))