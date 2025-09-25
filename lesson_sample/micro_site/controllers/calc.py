from utils import render_template

def calc(environ):
    query = environ.get('QUERY_STRING', '')
    params = {}
    for pair in query.split('&'):
        if '=' in pair:
            k, v = pair.split('=', 1)
            params[k] = v

    num1 = params.get('num1')
    num2 = params.get('num2')
    result = None

    try:
        if num1 is not None and num2 is not None:
            result = float(num1) + float(num2)
    except ValueError:
        result = "計算できません"

    return render_template(
        "boundaries/calc.html",
        num1=num1 or "",
        num2=num2 or "",
        result=result if result is not None else ""
    )