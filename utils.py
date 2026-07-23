def load_css(file_name):
    with open(file_name) as f:
        css = f.read()

    return f"""
    <style>
    {css}
    </style>
    """



def clean_text(text):
    return text.strip()



def calculate_percentage(completed, total):

    if total == 0:
        return 0

    return (completed / total) * 100
