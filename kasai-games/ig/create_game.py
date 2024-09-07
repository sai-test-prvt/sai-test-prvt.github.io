link = input("Geben Sie den Link für das iframe ein (z.B. https://games.crazygames.com/en_US/solar-smash/index.html): ")
filename = input("Geben Sie den Namen der HTML-Datei ein (z.B. meine_seite.html): ")

file = filename + ".html"

html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>kasai.rip</title>
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
            position: relative;
        }}
        iframe {{
            width: 100vw;
            height: 100vh;
            border: none;
        }}
        .top-right-image {{
            position: absolute;
            top: 0;
            right: 0;
            width: 250px; /* Oder die gewünschte Breite */
            height: auto;
            border-radius: 15px; /* Oder die gewünschte Abrundung */
            padding: 10px; /* Optional: Abstand zum Rand */
        }}
    </style>
</head>
<body>
    <iframe src="{link}" title="kasai.rip"></iframe>
    <img src="kasai.png" alt="Kasai" class="top-right-image">
</body>
</html>"""

with open(file, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Die Datei {filename} wurde erstellt.")
