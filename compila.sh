#!/bin/bash
#
# Author : 
# Date: 
# Version 1.0.0: 
#

makepkg -s
gpg --sign --detach-sign *.pkg.tar.zst

