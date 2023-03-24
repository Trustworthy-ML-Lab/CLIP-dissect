#!/usr/bin/env bash
set -e

echo "Download resnet18 trained on Places365"
echo "Downloading $MODEL"
mkdir -p data
pushd data
wget --progress=bar \
   http://places2.csail.mit.edu/models_places365/resnet18_places365.pth.tar
popd

echo "done"