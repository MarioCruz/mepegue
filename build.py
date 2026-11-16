#!/usr/bin/env python3
"""Writes the four pages (home and privacy, in English and Spanish), robots.txt and
sitemap.xml. Edit the text in this file, then run:  python3 build.py

BASE is the public address of the site. Change it here if the site moves to its own
domain; all links between pages are relative and keep working either way.
"""
import os

BASE = "https://mepegueapp.com/"
EFFECTIVE = {"en": "15 November 2026", "es": "15 de noviembre de 2026"}
MAIL = '<a class="em" href="#" data-u="mario" data-d="mariothemaker.com">mario [at] mariothemaker [dot] com</a>'

T = {
 "en": dict(
  lang="en", other="es", other_label="Español", root="", up="es/",
  home="Home", how="How it works", help="Help", privacy="Privacy",
  title="Me Pegué — Domino score keeper that counts the dots from a photo",
  desc="Me Pegué is a domino score keeper for iPhone. Photograph the tiles the losing team is holding and the app counts the dots on your phone, circles each one, and gives the points to the other team. English and Spanish. No account, no tracking.",
  tag="The domino score keeper that counts the dots for you.",
  sub="When a hand ends, take a photo of the tiles the losing team is still holding. Me Pegué counts every dot on your phone and gives the points to the other team.",
  chips=["iPhone", "English and Español", "No account", "Works with no internet"],
  soon="Coming soon to the App Store",
  how_h="How it works",
  steps=[("Photograph the losing hand", "Lay the leftover tiles face up and take a photo from straight above."),
         ("Check the count", "Every dot the app counted is circled on the photo, so a miss is obvious. Fix the number in a tap if it needs it."),
         ("Give the points", "Pick who was holding the tiles and the points go to the other team.")],
  shots_h="A look at the app",
  shots=[("01_review", "A photo of dominoes with every counted dot circled, and the hand shown tile by tile"),
         ("02_board", "The scoreboard: Nosotros 67, Ellos 23, with the list of rounds"),
         ("03_tiles", "Entering a hand by tapping the tiles"),
         ("04_win", "The game-over screen calling a pollona")],
  feat_h="Made for the domino table",
  feats=[("Counts from a photo", "Automatic dot counting with computer vision that runs on your phone."),
         ("You stay in charge", "Correct any count as a number, or by tapping out the tiles left in the hand."),
         ("Cuban-style scoring", "Two teams, Nosotros and Ellos or any names you like. Play to 100, 150 or 200."),
         ("Double-nine and double-six", "Works with both sets."),
         ("Rounds you can undo", "Every round is listed, and the last one can be undone."),
         ("Pollona", "The app calls it when the other side never scores.")],
  help_h="Help and support",
  help_lead="Answers to the common questions. If yours isn't here, write to us.",
  faq=[("The count is wrong. What do I do?",
        "<p>Tap minus or plus to fix the number, or switch to Tiles and tap out the tiles in the hand. Nothing is scored until you tap the yellow button.</p><p>For the best count: lay the tiles face up, take the photo from straight above, and avoid heavy shadows and blur. Very dark or blurry photos are the ones it gets wrong.</p>"),
       ("Which domino sets does it work with?", "<p>Double-nine and double-six sets with dots.</p>"),
       ("How do I change the language?", "<p>Open settings with the sliders button on the scoreboard and choose English, Español, or the same language as your phone.</p>"),
       ("How do I fix a score after the round is given?", "<p>Tap Undo last to remove the last round, or tap a team's score to type the correct number.</p>"),
       ("Where are my scores kept?", "<p>Only on your phone. There is no account and nothing is uploaded. Deleting the app deletes the scores.</p>"),
       ("Does it need the internet?", "<p>No. Everything, including counting the dots, happens on your phone.</p>"),
       ("What does \"me pegué\" mean?", "<p>It is what a Cuban player says on playing the last tile and winning the hand.</p>")],
  contact_h="Contact",
  contact="Questions, a photo it counted wrong, or an idea? Email " + MAIL + ".",
  made="Me Pegué · Made by Mario The Maker",
  p_title="Me Pegué — Privacy Policy",
  p_desc="Me Pegué privacy policy: no data collected, no accounts, no tracking, no servers. Photos are counted on your phone and never uploaded.",
  p_h1="Privacy Policy",
  p_meta="Effective {date} · Applies to the Me Pegué app for iPhone.",
  p_short="<b>Short version:</b> Me Pegué does not collect your data. There are no accounts, no servers, no analytics and no tracking. The app never connects to the internet.",
  p_sections=[
   ("What Me Pegué accesses, and why",
    "<p>Me Pegué asks for one permission, and only when you use it:</p><ul><li><b>Camera.</b> If you tap Take a photo, the app uses the camera so you can photograph the dominoes. You can decline, or turn it off later in Settings, and still use the app by choosing a photo or typing the count.</li></ul><p>If you tap Choose a photo, you pick one picture through Apple's photo picker. The app receives only that picture and has no access to the rest of your library.</p>"),
   ("What happens to your photos",
    "<p>A photo is used for one thing: counting the dots. The counting runs on your phone. The photo is not uploaded, not shared, and not saved by the app; it is discarded when you finish or close the round.</p>"),
   ("What is stored",
    "<p>The app stores your games on your phone: team names, the points of each round, the target score, and your language choice. This stays on your device and is not sent anywhere.</p>"),
   ("What Me Pegué does not do",
    "<ul><li>It does <b>not</b> collect, sell or share personal data.</li><li>It does <b>not</b> use analytics, advertising or tracking tools.</li><li>It does <b>not</b> track you across apps or websites.</li><li>It has <b>no</b> accounts and needs no sign-in.</li><li>It makes <b>no</b> network connections.</li></ul>"),
   ("Third parties",
    "<p>Me Pegué uses no third-party services or software kits and shares no data with anyone.</p>"),
   ("This website",
    "<p>This site is hosted by GitHub Pages. Like any web server, GitHub's servers see the network address a visit comes from. The site has no analytics, no cookies and no forms, and the developer does not receive those server logs.</p>"),
   ("Children",
    "<p>Me Pegué is not directed at children and collects no personal information from anyone, of any age.</p>"),
   ("Your control and deleting data",
    "<p>You can turn off camera access in Settings at any time, undo rounds or start a new game inside the app, and remove everything by deleting the app. Because nothing is stored off your phone, deleting the app removes its data.</p>"),
   ("Changes to this policy",
    "<p>If this policy changes, the new version will be posted on this page with a new effective date.</p>"),
   ("Contact", "<p>Questions about privacy in Me Pegué? Email " + MAIL + ".</p>"),
  ]),
 "es": dict(
  lang="es", other="en", other_label="English", root="../", up="../",
  home="Inicio", how="Cómo funciona", help="Ayuda", privacy="Privacidad",
  title="Me Pegué — Anotador de dominó que cuenta los puntos con una foto",
  desc="Me Pegué es un anotador de dominó para iPhone. Tómale una foto a las fichas que le quedaron al equipo perdedor y la app cuenta los puntos en tu teléfono, marca cada uno y se los da al otro equipo. En español e inglés. Sin cuenta y sin rastreo.",
  tag="El anotador de dominó que cuenta los puntos por ti.",
  sub="Cuando termina una data, tómale una foto a las fichas que le quedaron al equipo perdedor. Me Pegué cuenta cada punto en tu teléfono y se los da al otro equipo.",
  chips=["iPhone", "Español e inglés", "Sin cuenta", "Funciona sin internet"],
  soon="Muy pronto en el App Store",
  how_h="Cómo funciona",
  steps=[("Tómale foto a las fichas", "Pon las fichas que quedaron boca arriba y tómales una foto desde arriba."),
         ("Revisa la cuenta", "Cada punto que la app contó queda marcado con un círculo en la foto, así un error se ve enseguida. Corrige el número con un toque si hace falta."),
         ("Da los puntos", "Elige quién se quedó con las fichas y los puntos van para el otro equipo.")],
  shots_h="Un vistazo a la app",
  shots=[("01_review", "Una foto de fichas con cada punto marcado y la mano mostrada ficha por ficha"),
         ("02_board", "El marcador: Nosotros 67, Ellos 23, con la lista de datas"),
         ("03_tiles", "Entrar una mano tocando las fichas"),
         ("04_win", "La pantalla de fin de partida cantando una pollona")],
  feat_h="Hecho para la mesa de dominó",
  feats=[("Cuenta con una foto", "Cuenta los puntos automáticamente con visión por computadora que corre en tu teléfono."),
         ("Tú mandas", "Corrige cualquier cuenta con un número o tocando las fichas que quedaron."),
         ("Se anota a lo cubano", "Dos equipos, Nosotros y Ellos o los nombres que quieras. Se juega a 100, 150 o 200."),
         ("Doble nueve y doble seis", "Funciona con los dos juegos de fichas."),
         ("Datas que se pueden deshacer", "Cada data queda en la lista y la última se puede deshacer."),
         ("Pollona", "La app la canta cuando el otro equipo no anota.")],
  help_h="Ayuda y soporte",
  help_lead="Respuestas a las preguntas más comunes. Si la tuya no está, escríbenos.",
  faq=[("La cuenta salió mal. ¿Qué hago?",
        "<p>Toca menos o más para corregir el número, o cambia a Fichas y toca las fichas de la mano. No se anota nada hasta que tocas el botón amarillo.</p><p>Para que cuente mejor: pon las fichas boca arriba, toma la foto desde arriba y evita sombras fuertes y fotos movidas. Las fotos muy oscuras o borrosas son las que falla.</p>"),
       ("¿Con qué fichas funciona?", "<p>Con juegos doble nueve y doble seis de puntos.</p>"),
       ("¿Cómo cambio el idioma?", "<p>Abre los ajustes con el botón de controles del marcador y elige English, Español o el mismo idioma del teléfono.</p>"),
       ("¿Cómo corrijo los puntos después de dar la data?", "<p>Toca Deshacer para quitar la última data, o toca los puntos de un equipo para escribir el número correcto.</p>"),
       ("¿Dónde se guardan mis puntos?", "<p>Solo en tu teléfono. No hay cuenta y no se sube nada. Si borras la app, se borran los puntos.</p>"),
       ("¿Necesita internet?", "<p>No. Todo, incluso contar los puntos, pasa en tu teléfono.</p>"),
       ("¿Qué quiere decir \"me pegué\"?", "<p>Es lo que dice un jugador cubano al poner su última ficha y ganar la data.</p>")],
  contact_h="Contacto",
  contact="¿Preguntas, una foto que contó mal, o una idea? Escribe a " + MAIL + ".",
  made="Me Pegué · Hecho por Mario The Maker",
  p_title="Me Pegué — Política de privacidad",
  p_desc="Política de privacidad de Me Pegué: no se recopilan datos, sin cuentas, sin rastreo, sin servidores. Las fotos se cuentan en tu teléfono y nunca se suben.",
  p_h1="Política de privacidad",
  p_meta="Vigente desde el {date} · Aplica a la app Me Pegué para iPhone.",
  p_short="<b>En corto:</b> Me Pegué no recopila tus datos. No hay cuentas, ni servidores, ni analíticas, ni rastreo. La app nunca se conecta a internet.",
  p_sections=[
   ("A qué accede Me Pegué y por qué",
    "<p>Me Pegué pide un solo permiso, y solo cuando lo usas:</p><ul><li><b>Cámara.</b> Si tocas Tomar foto, la app usa la cámara para que fotografíes las fichas. Puedes decir que no, o quitarlo después en Ajustes, y seguir usando la app eligiendo una foto o escribiendo la cuenta.</li></ul><p>Si tocas Elegir una foto, escoges una imagen con el selector de fotos de Apple. La app recibe solo esa imagen y no tiene acceso al resto de tu fototeca.</p>"),
   ("Qué pasa con tus fotos",
    "<p>Una foto se usa para una sola cosa: contar los puntos. La cuenta se hace en tu teléfono. La foto no se sube, no se comparte y la app no la guarda; se descarta cuando terminas o cierras la data.</p>"),
   ("Qué se guarda",
    "<p>La app guarda tus partidas en tu teléfono: los nombres de los equipos, los puntos de cada data, la meta de puntos y el idioma que elegiste. Eso se queda en tu dispositivo y no se envía a ningún lado.</p>"),
   ("Lo que Me Pegué no hace",
    "<ul><li><b>No</b> recopila, vende ni comparte datos personales.</li><li><b>No</b> usa herramientas de analíticas, publicidad ni rastreo.</li><li><b>No</b> te rastrea en otras apps ni en sitios web.</li><li><b>No</b> tiene cuentas ni pide iniciar sesión.</li><li><b>No</b> hace conexiones de red.</li></ul>"),
   ("Terceros",
    "<p>Me Pegué no usa servicios ni componentes de terceros y no comparte datos con nadie.</p>"),
   ("Este sitio web",
    "<p>Este sitio está alojado en GitHub Pages. Como cualquier servidor web, los servidores de GitHub ven la dirección de red desde la que llega una visita. El sitio no tiene analíticas, ni cookies, ni formularios, y el desarrollador no recibe esos registros.</p>"),
   ("Menores",
    "<p>Me Pegué no está dirigida a menores y no recopila información personal de nadie, de ninguna edad.</p>"),
   ("Tu control y cómo borrar los datos",
    "<p>Puedes quitar el acceso a la cámara en Ajustes cuando quieras, deshacer datas o empezar otra partida dentro de la app, y borrarlo todo eliminando la app. Como nada se guarda fuera de tu teléfono, al borrar la app se borran sus datos.</p>"),
   ("Cambios a esta política",
    "<p>Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha de vigencia.</p>"),
   ("Contacto", "<p>¿Preguntas sobre la privacidad en Me Pegué? Escribe a " + MAIL + ".</p>"),
  ]),
}


def url(lang, page):
    return BASE + ("" if lang == "en" else "es/") + ("" if page == "index.html" else page)


def head(t, page, title, desc):
    a = t["root"] + "assets/"
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(l, page)}">\n' for l in ("en", "es"))
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url(t['lang'], page)}">
{alts}<link rel="alternate" hreflang="x-default" href="{url('en', page)}">
<link rel="icon" href="{a}icon.png">
<link rel="stylesheet" href="{a}style.css">
<meta property="og:title" content="{title}">
<meta property="og:site_name" content="Me Pegué">
<meta property="og:description" content="{t['tag']}">
<meta property="og:url" content="{url(t['lang'], page)}">
<meta property="og:image" content="{BASE}assets/og.png">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
"""


def chrome(t, page):
    a = t["root"] + "assets/"
    other = t["up"] + page
    top = f"""<header class="site">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="{a}icon.png" alt=""><span>Me Pegué</span></a>
    <nav>
      <a href="index.html#how">{t['how']}</a>
      <a href="index.html#help">{t['help']}</a>
      <a href="privacy.html">{t['privacy']}</a>
      <a class="lang" href="{other}" hreflang="{t['other']}" lang="{t['other']}">{t['other_label']}</a>
    </nav>
  </div>
</header>
"""
    foot = f"""<footer class="site">
  <div class="wrap">
    <p>{t['made']} · {MAIL}</p>
    <p><a href="index.html">{t['home']}</a> · <a href="index.html#help">{t['help']}</a> · <a href="privacy.html">{t['privacy']}</a> · <a href="{other}" hreflang="{t['other']}" lang="{t['other']}">{t['other_label']}</a></p>
  </div>
</footer>

<script src="{a}em.js" defer></script>
</body>
</html>
"""
    return top, foot


def home(t):
    a = t["root"] + "assets/"
    top, foot = chrome(t, "index.html")
    ld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"Me Pegué","operatingSystem":"iOS","applicationCategory":"UtilitiesApplication","inLanguage":["en","es"],"description":"{t['desc']}","url":"{url(t['lang'], 'index.html')}","image":"{BASE}assets/icon.png","author":{{"@type":"Person","name":"Mario Cruz"}}}}
</script>
</head>
<body>
"""
    chips = "".join(f"<li>{c}</li>" for c in t["chips"])
    steps = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in t["steps"])
    shots = "".join(f'<div class="shot"><img src="{a}shots/{t["lang"]}_{n}.jpg" width="660" height="1434" loading="lazy" alt="{alt}"></div>' for n, alt in t["shots"])
    feats = "".join(f'<div class="feat"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["feats"])
    faq = "".join(f'<details><summary>{q}</summary><div class="a">{ans}</div></details>' for q, ans in t["faq"])
    body = f"""<main>
<div class="wrap hero">
  <img class="app" src="{a}icon.png" width="120" height="120" alt="">
  <h1>Me Pegué</h1>
  <p class="tag">{t['tag']}</p>
  <p class="sub">{t['sub']}</p>
  <ul class="chips">{chips}</ul>
  <span class="soon">{t['soon']}</span>
</div>

<section id="how"><div class="wrap">
  <h2>{t['how_h']}</h2>
  <ol class="steps">{steps}</ol>
</div></section>

<section><div class="wrap">
  <h2>{t['shots_h']}</h2>
  <div class="shots">{shots}</div>
</div></section>

<section><div class="wrap">
  <h2>{t['feat_h']}</h2>
  <div class="grid">{feats}</div>
</div></section>

<section id="help"><div class="wrap">
  <h2>{t['help_h']}</h2>
  <p class="lead">{t['help_lead']}</p>
  <div class="faq">{faq}</div>
  <h2 style="margin-top:34px">{t['contact_h']}</h2>
  <p>{t['contact']}</p>
</div></section>
</main>

"""
    return head(t, "index.html", t["title"], t["desc"]) + ld + top + body + foot


def privacy(t):
    top, foot = chrome(t, "privacy.html")
    sections = "".join(f"<h2>{h}</h2>\n{b}\n" for h, b in t["p_sections"])
    body = f"""<main class="wrap prose" style="padding-top:44px;padding-bottom:30px">
  <h1>{t['p_h1']}</h1>
  <p class="meta">{t['p_meta'].format(date=EFFECTIVE[t['lang']])}</p>
  <div class="callout"><p>{t['p_short']}</p></div>
{sections}</main>

"""
    return head(t, "privacy.html", t["p_title"], t["p_desc"]) + "</head>\n<body>\n" + top + body + foot


here = os.path.dirname(os.path.abspath(__file__))
for lang, t in T.items():
    folder = here if lang == "en" else os.path.join(here, "es")
    os.makedirs(folder, exist_ok=True)
    open(os.path.join(folder, "index.html"), "w").write(home(t))
    open(os.path.join(folder, "privacy.html"), "w").write(privacy(t))

pages = [url(l, p) for p in ("index.html", "privacy.html") for l in ("en", "es")]
open(os.path.join(here, "sitemap.xml"), "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{p}</loc></url>\n" for p in pages) + "</urlset>\n")
bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-Web", "PerplexityBot",
        "Google-Extended", "Applebot", "Applebot-Extended", "Bingbot"]
open(os.path.join(here, "robots.txt"), "w").write(
    "User-agent: *\nAllow: /\n\n# AI and answer-engine crawlers are welcome\n"
    + "".join(f"User-agent: {b}\nAllow: /\n" for b in bots) + f"\nSitemap: {BASE}sitemap.xml\n")
print("wrote", len(pages), "pages for", BASE)
