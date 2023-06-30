#!/usr/bin/env bash
set -e

# Start from parent directory of script
#cd "$(dirname "$(dirname "$(readlink -f "$0")")")"

# Download broden1_224
if [ ! -f data/broden1_224/index.csv ]
then

echo "Downloading broden1_224"
mkdir -p data
pushd data
wget --progress=bar \
   http://netdissect.csail.mit.edu/data/broden1_224.zip \
   -O broden1_224.zip
unzip -q broden1_224.zip
rm broden1_224.zip
#remove unneeded files
pushd broden1_224
#rm *.csv
rm *.txt
rm images/ade20k/*object.png
rm images/ade20k/*color.png
rm images/ade20k/*.png
rm images/dtd/*.png
rm images/opensurfaces/*color.png
rm images/opensurfaces/*.png
rm images/pascal/*.png

popd

fi