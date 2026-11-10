"""Genera el QR de la app que va embebido en index.html.

El código apunta a una URL fija, así que se genera una vez acá y se pega como
SVG en el HTML: la página no depende de ninguna librería ni de ningún CDN.

    pip install qrcode
    python3 herramientas/qr.py > /tmp/qr.svg

Después se reemplaza el <svg class="qr-svg"> que está dentro de .qrmarco.

Tres cosas no se tocan sin volver a verificar que el código se lea:

  * Los patrones de las esquinas van CUADRADOS. Redondearlos rompe la lectura
    (el lector ubica el código por la proporción 1:1:3:1:1 de esos patrones).
    Su color sí se puede cambiar.
  * La corrección de errores va en nivel H. Es lo que banca el hueco del logo.
  * El hueco mide 9 módulos sobre 37, el 24 % del ancho. Más grande entra en
    terreno dudoso con lectores reales.
"""

import qrcode

URL = "https://vaiven-app-ruddy.vercel.app/"
BORDE = 4       # zona de silencio, en módulos: 4 es lo que pide la norma
HUECO = 9       # lado del hueco del logo, en módulos
PUNTO = .46     # radio de cada punto de datos, en módulos
TINTA = "#11302e"
VERDE = "#2f6b50"

CANASTA = (
    '<path d="M16 17c0-5.5 3.6-9 8-9s8 3.5 8 9"/>'
    '<rect x="6" y="17" width="36" height="6" rx="3"/>'
    '<path d="M9.5 23 12.5 37.5A3.5 3.5 0 0 0 16 40.5h16a3.5 3.5 0 0 0 3.5-3L38.5 23"/>'
    '<path d="M18 27.5 19 36M24 27.5V36M30 27.5 29 36" stroke-width="2.4"/>'
    '<path d="M11.8 29.8h24.4M13.2 34.6h21.6" stroke-width="2.4"/>'
)


def generar():
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        border=BORDE,
        box_size=1,
    )
    qr.add_data(URL)
    qr.make(fit=True)
    m = qr.get_matrix()
    n = len(m)

    c0 = (n - HUECO) // 2
    c1 = c0 + HUECO
    ojos = [(BORDE, BORDE), (BORDE, n - BORDE - 7), (n - BORDE - 7, BORDE)]

    def en_ojo(f, c):
        return any(o <= f < o + 7 and p <= c < p + 7 for o, p in ojos)

    puntos = []
    for f in range(n):
        for c in range(n):
            if not m[f][c] or en_ojo(f, c):
                continue
            if c0 <= c < c1 and c0 <= f < c1:      # el hueco del logo
                continue
            puntos.append('<circle cx="%d" cy="%d" r="%s"/>' % (c, f, str(PUNTO).lstrip("0")))

    marcas = []
    for o, p in ojos:
        marcas.append('<path d="M%d %dh7v7h-7zM%d %dh5v5h-5z" fill="%s" fill-rule="evenodd"/>'
                      % (p, o, p + 1, o + 1, VERDE))
        marcas.append('<rect x="%d" y="%d" width="3" height="3" fill="%s"/>' % (p + 2, o + 2, VERDE))

    esc = HUECO * .74 / 48
    off = c0 + HUECO * .13

    return (
        '<svg class="qr-svg" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
        'role="img" aria-label="Código QR que abre la app de VaiVen">'
        '<rect width="%d" height="%d" rx="1.5" fill="#fff"/>'
        '<g transform="translate(.5 .5)" fill="%s">%s</g>%s'
        '<rect x="%d" y="%d" width="%d" height="%d" rx="2.2" fill="#fff"/>'
        '<g transform="translate(%.3f %.3f) scale(%.5f)" fill="none" stroke="%s" '
        'stroke-width="3" stroke-linecap="round" stroke-linejoin="round">%s</g>'
        '</svg>'
    ) % (n, n, n, n, TINTA, "".join(puntos), "".join(marcas),
         c0, c0, HUECO, HUECO, off, off, esc, VERDE, CANASTA)


if __name__ == "__main__":
    print(generar())
