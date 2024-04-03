from flask import Flask, request, render_template, jsonify
from googletrans import Translator

app = Flask(__name__)
traductor = Translator()

# Lista de idiomas permitidos
idiomas_permitidos = [
    'af', 'an', 'ak', 'sq', 'de', 'am', 'ar', 'hy', 'as', 'az', 'bm', 'bn', 'bh', 'be', 'my', 'bs', 'bg', 'kn',
    'ca', 'ceb', 'cs', 'zh-CN', 'zh-TW', 'si', 'ko', 'co', 'ht', 'hr', 'da', 'dv', 'nl', 'sk', 'sl', 'es', 'eo', 'et',
    'eu', 'ee', 'fi', 'fr', 'fy', 'gd', 'cy', 'gl', 'lg', 'ka', 'el', 'gn', 'gu', 'ha', 'haw', 'he', 'hi', 'hmn', 'hu',
    'ig', 'ilo', 'id', 'en', 'ga', 'is', 'it', 'ja', 'jv', 'km', 'kk', 'rw', 'ky', 'kri', 'ku', 'ku-sd', 'lo', 'la', 'lv',
    'ln', 'lt', 'lb', 'mk', 'mai', 'ml', 'ms', 'mg', 'mt', 'mr', 'mz', 'mn', 'ne', 'nb', 'ny', 'or', 'om', 'ps', 'fa',
    'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'sr', 'sn', 'sd', 'so', 'st', 'nr', 'sw', 'sv', 'su', 'tl', 'th',
    'ta', 'tt', 'tg', 'te', 'ti', 'ts', 'tr', 'tk', 'uk', 'ug', 'ur', 'uz', 'vi', 'xh', 'yi', 'yo', 'zu'
]

nombres_idiomas = {
    'af': 'Afrikaans', 'an': 'Aragonés', 'ak': 'Akan', 'sq': 'Albanés', 'de': 'Alemán', 'am': 'Amárico',
    'ar': 'Árabe', 'hy': 'Armenio', 'as': 'Asamés', 'az': 'Azerbaiyano', 'bm': 'Bambara', 'bn': 'Bengalí',
    'bh': 'Bihari', 'be': 'Bielorruso', 'my': 'Birmano', 'bs': 'Bosnio', 'bg': 'Búlgaro', 'kn': 'Canarés',
    'ca': 'Catalán', 'ceb': 'Cebuano', 'cs': 'Checo', 'zh-CN': 'Chino (Simplificado)', 'zh-TW': 'Chino (Tradicional)',
    'si': 'Cingalés', 'ko': 'Coreano', 'co': 'Corso', 'ht': 'Criollo haitiano', 'hr': 'Croata', 'da': 'Danés',
    'dv': 'Maldivo', 'nl': 'Neerlandés', 'sk': 'Eslovaco', 'sl': 'Esloveno', 'es': 'Español', 'eo': 'Esperanto',
    'et': 'Estonio', 'eu': 'Vasco', 'ee': 'Ewé', 'fi': 'Finés', 'fr': 'Francés', 'fy': 'Frisón occidental',
    'gd': 'Gaélico escocés', 'cy': 'Galés', 'gl': 'Gallego', 'lg': 'Ganda', 'ka': 'Georgiano', 'el': 'Griego',
    'gn': 'Guaraní', 'gu': 'Gujarati', 'ha': 'Hausa', 'haw': 'Hawaiano', 'he': 'Hebreo', 'hi': 'Hindi', 'hmn': 'Hmong',
    'hu': 'Húngaro', 'ig': 'Igbo', 'ilo': 'Ilocano', 'id': 'Indonesio', 'en': 'Inglés', 'ga': 'Irlandés',
    'is': 'Islandés', 'it': 'Italiano', 'ja': 'Japonés', 'jv': 'Javanés', 'km': 'Jemer', 'kk': 'Kazajo',
    'rw': 'Kinyarwanda', 'ky': 'Kirguís', 'kri': 'Krio', 'ku': 'Kurdo', 'ku-sd': 'Kurdo (Sorani)', 'lo': 'Lao',
    'la': 'Latín', 'lv': 'Letón', 'ln': 'Lingala', 'lt': 'Lituano', 'lb': 'Luxemburgués', 'mk': 'Macedonio',
    'mai': 'Maithili', 'ml': 'Malayalam', 'ms': 'Malayo', 'mg': 'Malgache', 'mt': 'Maltés', 'mr': 'Marathi',
    'mz': 'Mizo', 'mn': 'Mongol', 'ne': 'Nepalí', 'nb': 'Noruego Bokmål', 'ny': 'Chichewa', 'or': 'Oriya',
    'om': 'Oromo', 'ps': 'Pastú', 'fa': 'Persa', 'pl': 'Polaco', 'pt': 'Portugués', 'pa': 'Punyabí', 'qu': 'Quechua',
    'ro': 'Rumano', 'ru': 'Ruso', 'sm': 'Samoano', 'sa': 'Sánscrito', 'sr': 'Serbio', 'sn': 'Shona', 'sd': 'Sindhi',
    'so': 'Somalí', 'st': 'Sesotho meridional', 'nr': 'Sesotho septentrional', 'sw': 'Suajili', 'sv': 'Sueco',
    'su': 'Sundanés', 'tl': 'Tagalo', 'th': 'Tailandés', 'ta': 'Tamil', 'tt': 'Tártaro', 'tg': 'Tayiko',
    'te': 'Telugu', 'ti': 'Tigriña', 'ts': 'Tsonga', 'tr': 'Turco', 'tk': 'Turcomano', 'uk': 'Ucraniano',
    'ug': 'Uigur', 'ur': 'Urdu', 'uz': 'Uzbeko', 'vi': 'Vietnamita', 'xh': 'Xhosa', 'yi': 'Yidis', 'yo': 'Yoruba',
    'zu': 'Zulú'
}

def detectar_idioma(texto):
    detectado = traductor.detect(texto)
    idioma = detectado.lang if hasattr(detectado, 'lang') else None
    return idioma

@app.route('/')
def index():
    return render_template('index.html', idiomas=idiomas_permitidos, nombres_idiomas=nombres_idiomas)

@app.route('/traducir', methods=['POST'])
def traducir():
    texto = request.form['texto']
    idioma_destino = request.form['idioma_destino']
    
    # Verificar si el campo de texto está vacío
    if not texto:
        mensaje_error = "No hay texto para traducir."
        return render_template('index.html', idiomas=idiomas_permitidos, nombres_idiomas=nombres_idiomas, error=mensaje_error)
    
    try:
        # Realizar la traducción y detectar el idioma
        traduccion = traductor.translate(texto, dest=idioma_destino).text
        
        # Eliminar "Traducción:" del texto si está presente
        traduccion = traduccion.replace("Traducción:", "").strip()
        
        # Detectar el idioma de la traducción
        idioma_traduccion = traductor.detect(traduccion).lang
        
        return render_template('index.html', idiomas=idiomas_permitidos, nombres_idiomas=nombres_idiomas, traduccion=traduccion, idioma_traduccion=idioma_traduccion)
    except Exception as e:
        mensaje_error = "Se produjo un error durante la traducción."
        return render_template('index.html', idiomas=idiomas_permitidos, nombres_idiomas=nombres_idiomas, error=mensaje_error)



if __name__ == '__main__':
    app.run(debug=True)
