
pandoc \
 --variable geometry:margin=1.5cm \
 --variable fontsize=8pt \
 --variable colorlinks=true \
 --variable papersize=a4 \
 --variable classoption=twocolumn \
 --variable classoption=landscape \
 --table-of-contents \
 curated75.md -o curated75.pdf
 #--highlight-style=monochrome \
