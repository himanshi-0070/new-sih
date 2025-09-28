#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Install git lfs for large model files
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
apt-get install git-lfs
git lfs install

# Pull LFS files
git lfs pull

echo "Build completed successfully!"