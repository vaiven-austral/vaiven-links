# vaiven-links — punto de acceso del proyecto

Página única con todo lo que se comparte de **VaiVen**: producto, repositorios, gestión, Steerings, documentos, recursos de cátedra y equipo.

Es un **entregable de dirección**, no código del producto. El producto vive en [`vaiven-app`](https://github.com/vaiven-austral/vaiven-app) y lo escriben los desarrolladores de Laboratorio II.

El checklist que originó esta página, el relevamiento de los otros equipos y las decisiones están en `vaiven-direccion/docs/linktree/`.

---

## Qué es cada cosa

| | |
|---|---|
| `index.html` | **Toda la página.** HTML y CSS en un solo archivo, sin dependencias ni build |
| Estructura | **Mobile-first.** En celular los botones van sueltos sobre el fondo; el panel crema aparece recién en `min-width: 720px`. Mismo enfoque que [`SplitItLab/splitit-linktree`](https://github.com/SplitItLab/splitit-linktree) |
| Tema claro y oscuro | Arranca siguiendo al sistema y recuerda la elección en `localStorage` (`vaiven-tema`). El atributo `data-tema` en `<html>` manda sobre la preferencia del sistema. Cambian el fondo, el panel, las tarjetas y el logotipo |
| Logotipo según tema | Dos versiones: la **verde** en claro y la **blanca** en oscuro, con `--logo-claro` y `--logo-verde` |
| La canasta | **SVG, no PNG.** El favicon original es de 82 px y se pixelaba en pantallas de alta densidad. Dibujada con trazos, toma el color del tema y es nítida a cualquier tamaño |
| Título y favicon | `VaiVen · Links`, con el favicon de la landing embebido — también como `apple-touch-icon` para cuando se guarda en la pantalla de inicio |
| Fondo | SVG inline con formas y texturas de línea, animado en 30 s. Se desactiva solo con `prefers-reduced-motion` |
| Logotipo | `logoVerde.png` y el favicon de la landing, **embebidos como data URI** — la página no depende de ningún host externo para la marca |
| Tipografía | Plus Jakarta Sans, la misma de la landing, desde Google Fonts |
| Paleta | Fondo `#0e2e30` · panel `#f5f2e9` · texto `#12302f` · verde `#2f6b50` · acento `#49a078`. Sin amarillo |
| QR a la app | Dentro del menú de compartir, **Mostrar QR de la app**. El código está **generado de antemano y embebido como SVG**: la URL no cambia, así que no hay motivo para calcularlo en el navegador ni para traer una librería por CDN |

No hay framework, ni `package.json`, ni paso de compilación. Se abre con doble clic.

## Cómo se publica

Vercel sirve un `index.html` en la raíz sin configuración:

1. **Add New → Project** y elegir este repositorio.
2. Framework Preset: **Other**. Build Command y Output Directory se dejan vacíos.
3. **Deploy**.

Cada push a `main` vuelve a publicar.

## Cómo se edita

Todo el contenido está en el HTML. Para agregar un link se copia un botón:

```html
<a class="link" href="URL">
  <span class="ic" aria-hidden="true"><svg …></svg></span>
  <span class="label">Título<span class="tag">etiqueta</span></span>
</a>
```

- `<h2>` abre una sección nueva.
- `<span class="tag">` es la etiqueta chica: `privado`, `con cuenta`, `producción`.
- `class="link featured"` lo pinta en ámbar. **Va una sola vez**, en el botón de arriba.
- `class="link off"` es un botón apagado y punteado, sin link: se usa con `<div>` en lugar de `<a>`, para lo que todavía no existe.
- Los íconos son [Lucide](https://lucide.dev), pegados como SVG inline. Para uno nuevo se copia el `<path>` desde el sitio.

**El logotipo está embebido como data URI.** Si cambia la marca, hay que volver a generar el base64 desde el PNG y reemplazar el `src` — son dos, la versión blanca y la verde.

> ⚠️ **Los tres cuadrados de las esquinas del QR van cuadrados, no redondeados.** Es el recurso típico para «embellecer» un QR y rompe la lectura: el lector ubica el código por la proporción 1:1:3:1:1 de esos patrones, y redondearlos la deforma. Medido con un decodificador: con esquinas redondeadas no leyó a ningún tamaño; con esquinas cuadradas leyó a 140, 180, 240, 320 y 480 px. Lo que sí se personaliza sin riesgo es el **color** de esos cuadrados, los **puntos redondos** de los datos y el **hueco del logo**.

> ⚠️ **No sacar el `<meta name="viewport">` del `<head>`.** Sin él el navegador móvil asume un viewport de ~980 px y la página se ve deszoomada en el celular. Pasó una vez: la página se escribió primero como artifact, donde la plataforma inyecta ese meta, y el error recién apareció al servirla desde Vercel. El detalle está en `vaiven-direccion/docs/bitacora/2026-11-09-una-pagina-sin-meta-viewport-se-ve-deszoomada-en-el-celular.md`.
>
> Para verificar que no hay desborde horizontal, comparar en el sitio desplegado `document.documentElement.scrollWidth` contra `innerWidth`. Una captura de pantalla no alcanza.

> ⚠️ **No cambiar el `height: 100lvh` del `.bg` por `inset: 0`.** Con `inset: 0` el alto sigue al viewport, y en el celular esconder la barra de direcciones lo redimensiona: el SVG se re-encuadra de golpe y el fondo parece glitchear al scrollear. `100lvh` es el viewport grande y no cambia.

## Lo que distingue a esta página

Tres gestos que salen del nombre del proyecto y no de la plantilla:

- **La canasta se mece** como un péndulo al cargar y al pasar el mouse. Vaivén es el movimiento de ida y vuelta, y la canasta es la marca del producto.
- **Cuatro burbujas flotan** sobre un fondo que no se mueve, y **sólo en escritorio**: en celular tapaban el contenido, así que ahí el fondo queda con las ondas solas. Animar la escena entera —rotarla y escalarla— se había visto raro; por eso las figuras del SVG están fijas y lo que se mueve va por encima.
- **El QR lleva la canasta en el centro.** Corrección de errores en nivel H —el más alto, 30 % de redundancia— para bancar el hueco del logo, que ocupa el 24 % del ancho. Se verificó decodificándolo, no mirándolo.
- **Un countdown corre** hasta el Steering final: días, horas, minutos y segundos. La fecha está fijada con huso (`2026-11-12T18:00:00-03:00`) para que dé igual desde dónde se abra; pasada la hora se detiene y muestra «Proyecto entregado». Para cambiarla, la constante `META` en el script.

## Pendientes

- [ ] Cronograma publicado
- [ ] PDF de las presentaciones de los Steerings 1 y 2
- [ ] Steering 3 — presentación y demo, el 12/11
- [ ] Logo de VaiVen como favicon y como imagen de previsualización al compartir
- [ ] Reemplazar la canasta dibujada a mano por el **export oficial del Figma** (`Vaivén — Kit de marca — App`, exportar como SVG). La actual es una reconstrucción a partir del favicon de 82 px: respeta el estilo pero puede no ser idéntica al original
