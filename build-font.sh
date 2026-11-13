#!/bin/sh

set -e

sourcesPath=./sources
output_dir=./timesnewwoman-fonts
#########################################

echo "
=================
 Building font …
=================
 $(date "+  DATE: %Y-%m-%d%n   TIME: %H:%M:%S")"
echo

rm -rf $output_dir
mkdir -p $output_dir

# project docs
for f in README.md MANIFEST.md GUST-FONT-LICENSE.txt
do
    if [ -f "$f" ]; then
        cp "$f" "$output_dir/"
    else
        echo "WARNING: $f not found, skipping."
    fi
done

# variable
fontmake -g $sourcesPath/*.glyphspackage -a -o variable \
        --output-dir $output_dir \
        --filter DecomposeTransformedComponentsFilter

for ttf in $output_dir/*.ttf
do
    fonttools ttLib.woff2 compress $ttf
done


echo "
=========================
 Finished building font!
=========================
"
