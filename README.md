# foci_analysis
Analysis pipeline for foci colocalization/proximity.

## Create conda environment

Preliminary installation instructions while the package is not in pypi:

- Create a conda environment:
```bash
conda create -y -n cellpose-env python=3.11 -c conda-forge
```
- Activate the environment:
```bash
conda activate cellpose-env
```
- Install torch (detailed instructions here: https://pytorch.org/get-started/locally/). Make sure that you match CUDA version, for example:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
- Install napari (detailed instructions here: https://napari.org/dev/tutorials/fundamentals/installation.html):
```bash
pip install "napari[all]"
```
- Install nd2reader:
```bash
pip install nd2reader
```

