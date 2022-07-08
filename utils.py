import numpy as np
from glob import glob
import cv2
import scipy.io as sio
import imgvision as iv

class Dataloader():
    def __init__(self,path):
        self.Filelist = glob(path+'*.mat')
    def load(self,index):
        self.Filename = self.Filelist[index].split('\\')[-1]
        base = sio.loadmat(self.Filelist[index])
        key = list(base.keys())[-1]
        Ground_Truth = base[key]
        print('\nLoad {} Successfully\n'.format(self.Filelist[index].split('\\')[-1] ))
        return Ground_Truth
    def save(self,path,img):
        np.save(path+self.Filename.replace('.mat',''),img)

def generate_lrhsi(gt,sf,type='Gaussian'):
    if type.lower()=='gaussian':
        return cv2.GaussianBlur(gt,(sf-1,sf-1),sf//4)[sf//2-1::sf,sf//2-1::sf]
    elif type.lower()=='motion':
        import paddleiv
        return paddleiv.get_LR(gt,type)

def generate_hrrgb(gt,srf):
    return gt @ srf

def get_pairs(gt,sf,srf,noise=None,NSR_HSI=30,NSR_RGB=40):
    lrhsi = generate_lrhsi(gt,sf)
    hrrgb = generate_hrrgb(gt,srf)
    if noise:
        lrhsi = iv.add_noise(lrhsi,NSR_HSI)
        hrrgb = iv.add_noise(hrrgb,NSR_RGB)

    print("\033[1;36m Image Settings \033[0m".center(61, '-'))
    print('\t\t\033[1;33m LR-HSI\t\t\tHR-RGB \033[0m'.ljust(50))
    print(f'size\t{lrhsi.shape}\t{hrrgb.shape}'.ljust(50))
    print(f'noise\t{noise}'.ljust(50))
    print(''.center(50,'-'))
    return lrhsi,hrrgb

