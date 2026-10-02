#!/bin/sh

set -e

sourcesPath=./sources
output_dir=./fonts-tnw
#########################################

echo "
=================
 Building font …
=================
 $(date "+  DATE: %Y-%m-%d%n   TIME: %H:%M:%S")"
echo

rm -rf $output_dir
mkdir -p $output_dir

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
