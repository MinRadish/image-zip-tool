#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# 压缩体积
# @Date    : 2021-05-18 Tuesday
# @Author  : Radish
# @Version : V1.0.0

import os
from PIL import Image
# from PyQt5 import QtWidgets

class ReduceImage:

    # type str
    inputDir = ... 
    # type str
    outDir = ...
    # type QtWidgets.QListWidget
    infoCon = ...
    # type int
    size = 0
    # type int
    quality = 65

    def ergodicDir(self, fileDir):
        # fileDir = fileDir.replace('\\', '/')
        # print('fileDir:' + fileDir)
        list = os.listdir(fileDir)
        for i in range(0, len(list)):
            if not list[i] == 'textboxio':
                path = os.path.join(fileDir, list[i])
                # print(path)
                if os.path.isdir(path):
                    # print('dir')
                    # print(os.listdir(path))
                    self.ergodicDir(path)
                elif os.path.isfile(path):
                    # print('file');
                    self.compressImage(path)

    def compressImage(self, path):
        try:
            if os.path.splitext(path)[1] in ['.png', '.jpg', 'jpeg', '.PNG', '.JPG', '.JPEG']:
                img = Image.open(path)
                self.saveImg(img, path)
                # saveImg(img, path, 220)
        except Exception as e:
            raise e

    def saveImg(self, img, path, size = 23):
        (w,h) = img.size
        multiple = 1
        if self.size > 0: 
            multiple = self.getMultiple(w, h, self.size)
            
        if not multiple == -1:
            newImg = img.resize((int(w * multiple), int(h * multiple)), Image.LANCZOS)
            saveFileDir = path.replace(self.inputDir, self.outDir)
            # print(saveFileDir)
            # saveFileDir = saveFileDir.replace('\\', '/')
            outDir = os.path.dirname(saveFileDir)
            # os._exit(0)
            if not os.path.isdir(outDir):
                try:
                    os.makedirs(outDir)
                except Exception as e:
                    raise e
            try:
                #quality初始压缩比率
                newImg.save(saveFileDir, quality=self.quality)
            except Exception as e:
                newImg = newImg.convert('RGB')
                newImg.save(saveFileDir)
            self.infoCon.addItem(saveFileDir)

    def getMultiple(self, width, height, maxSize = 50):
        size = height    
        if width > height:
            size = width
        # if size > maxSize:
        return maxSize / size
        # else :
            # return -1;    