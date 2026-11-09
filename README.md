# vaiven-links — punto de acceso del proyecto

Página única con todo lo que se comparte de **VaiVen**: producto, repositorios, gestión, Steerings, documentos, recursos de cátedra y equipo.

Es un **entregable de dirección**, no código del producto. El producto vive en [`vaiven-app`](https://github.com/vaiven-austral/vaiven-app) y lo escriben los desarrolladores de Laboratorio II.

El checklist que originó esta página, el relevamiento de los otros equipos y las decisiones están en `vaiven-direccion/docs/linktree/`.

---

## Qué es cada cosa

| | |
|---|---|
| `index.html` | **Toda la página.** HTML y CSS en un solo archivo, sin dependencias ni build |
| Estructura | Panel crema centrado sobre formas orgánicas que se mecen despacio. Adentro: avatar, logotipo, bio y botones apilados con título, subtítulo e ícono |
| Título y favicon | `VaiVen · Links`, con el favicon de la landing embebido — también como `apple-touch-icon` para cuando se guarda en la pantalla de inicio |
| Fondo | SVG inline con formas y texturas de línea, animado en 30 s. Se desactiva solo con `prefers-reduced-motion` |
| Logotipo | `logoVerde.png` y el favicon de la landing, **embebidos como data URI** — la página no depende de ningún host externo para la marca |
| Tipografía | Plus Jakarta Sans, la misma de la landing, desde Google Fonts |
| Paleta | Fondo `#0e2e30` · panel `#f5f2e9` · texto `#12302f` · verde `#2f6b50` · acento `#49a078`. Sin amarillo |

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

**El logotipo está embebido como data URI.** Si cambia la marca, hay que volver a generar el base64 desde el PNG y reemplazar el `src`.

## Pendientes

- [ ] Cronograma publicado
- [ ] PDF de las presentaciones de los Steerings 1 y 2
- [ ] Steering 3 — presentación y demo, el 12/11
- [ ] Logo de VaiVen como favicon y como imagen de previsualización al compartir
