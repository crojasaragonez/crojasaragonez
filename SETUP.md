# GitHub profile

This folder is the source for the public profile repository
`crojasaragonez/crojasaragonez`. Its root `README.md` appears on the GitHub profile.
The website repository remains `crojasaragonez/crojasaragonez.github.io`.

## Brand

The banner uses the website's Geist typeface and original palette:

| Token | Color |
| :--- | :--- |
| Background | `#0b0f19` |
| Text | `#f8fafc` |
| Muted text | `#94a3b8` |
| Blue | `#4f8cff` |
| Cyan | `#35d6ff` |
| Violet | `#7c5cff` |
| Border | `#273244` |

GitHub controls the surrounding README typography and background. The banner
carries the website's visual identity in both GitHub light and dark themes.
All banner assets are local; the profile needs no external badge services or
scheduled workflows.

## Edit the banner

Edit the text and geometry in `assets/banner-source.svg`. The published
`assets/banner.svg` converts the lettering to vector paths, so GitHub does not
need to load a font. Its title, description, and the README image alt text
provide a text alternative.

From the website repository, with its npm dependencies installed:

```bash
python3 github-profile/tools/build_banner.py \
  --font node_modules/@fontsource-variable/geist/files/geist-latin-wght-normal.woff2
```

The builder requires Python `fonttools` and `brotli`. If working from the
standalone profile repository, run `python3 tools/build_banner.py --font /path/to/geist-latin-wght-normal.woff2`.

## Suggested pins

Use **Your profile → Customize your pins** to highlight:

1. `text_to_sql_rag_app` — applied AI.
2. `light-service` — library development.
3. `crojasaragonez.github.io` — writing and personal website.
4. `presentations` — talks and teaching.

## Suggested bio

Technology entrepreneur · Co-Founder & Chief AI Officer @ Subaxa · Co-Founder & Board @ Golabs · AI products, engineering leadership & LATAM.

## Content maintenance

Keep roles, company metrics, program participation, and writing links aligned
with the website. The writing section is an editorial selection, not an
automatically updated feed.
