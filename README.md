# Times New Woman Fonts

Font: Times New Woman
Authors: Pablo Gámez Navarro, MUY
Authors URL: http://pablogamez.com, https://somosmuy.com
Version: 1.001
Date: 2026-11-20
Downloads: https://timesnewwoman.com/

## License

Copyright 2006--2025 for TeX Gyre extensions by B. Jackowski, J.M. Nowacki et al. (on behalf of TeX Users Groups). Vietnamese characters were added by Han The Thanh.

Copyright 2026 for Variable Opentype features by Pablo Gámez Navarro and Somosmuy.

This work can be freely used and distributed under the GUST Font License (GFL -- see GUST-FONT-LICENSE.txt) which legally equivalent to the LaTeX Project Public License (LPPL -- see https://www.latex-project.org/lppl.txt ).

This work has the maintenance status "unmaintained".
This work consists of the files listed in `MANIFEST.md`.

## A brief description of the package

The current package contains the most recent version of the Times New Woman variable fonts in the Truetype and WOFF2 formats.

Times New Woman is based on the TeX Gyre Termes project (http://www.gust.org.pl/projects/e-foundry/tex-gyre/termes), which was based on the URW Nimbus Roman No9 L kindly released by URW++ Design and Development Inc. under GFL (independently of the GPL release accompanying Ghostscript). The Vietnamese glyphs were added by Han The Thanh.

Times New Woman consists of 1 variable font with 24 instances (one per year, from 2003 to 2027).
Official data can be found in [Ministerio de Igualdad's website](https://violenciagenero.igualdad.gob.es/violenciaencifras/victimasmortales/fichamujeres/).

The Times New Woman fonts can be freely used and distributed under the GUST Font License (see above) which is actually an instance of the LaTeX Project Public License (LPPL; see http://www.latex-project.org/lppl.txt ).

All font files, ttf and woff2, contain the same repertoire of 1089 characters.

## How to Build the Fonts Locally

If you want to generate the font files yourself on your computer:

1. Clone the Repository: Download or clone this repository to your computer and open your Terminal or Command Prompt in the project folder.
2. Install Python: Make sure you have [Python](https://www.python.org/) installed.
3. Install Dependencies: Run:
   ```bash
   pip install -r requirements.txt
   ```
4. Build the Font: Run the build script:
   ```bash
   sh build-font.sh
   ```
Your newly built fonts will appear in the `timesnewwoman-fonts` folder