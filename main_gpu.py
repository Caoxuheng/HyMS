from config import args
from imgvision import spectra_metric
from Model.PolyAct_gpu import Modification
from Model.AngSim_init import initialization
from Model.SpeSpa_Refine_gpu import Refinement
from utils import *


def printQUI(GT,imgs,sf):
    name = ['X_in','X_act','X_re']
    print(''.ljust(50,'_'))
    print('Name\tPSNR\tSAM\t\tERGAS\tSSIM\tRMSE'.ljust(50))
    for idx,i in enumerate(imgs):
        P,SAM,E,SSIM,R = spectra_metric(GT,i,scale=sf).get_Evaluation()
        print(name[idx]+'\t{:.2f}\t{:.2f}\t{:.3f}\t{:.3f}\t{:.3f}'.format(P,SAM,E,SSIM,np.sqrt(R)*255))
    print(''.ljust(50, '-'))

def saveQUI_txt(path,metrics):
    f_list = open(path,'a')
    f_list.write(metrics)
    f_list.close()

def head_generator(path):
    f_list = open(path, 'a')
    f_list.write('PSNR\tSAM\t\tERGAS\tSSIM\tRMSE\n')
    f_list.close()

class saveQUI():
    def __init__(self,args):
        self.path = args.save_path+str(args.sf)+'_Quantitative_Results.txt'
        self.sf = args.sf
        head_generator(self.path)
    def step(self,GT,recon):
        P, SAM, E, SSIM, R = spectra_metric(GT, recon, scale=self.sf).get_Evaluation()
        self.metrics = '{:.2f}\t{:.2f}\t{:.3f}\t{:.3f}\t{:.3f}\n'.format(P,SAM,E,SSIM,np.sqrt(R)*255)

    def save(self):
        saveQUI_txt(self.path,self.metrics)

    def print(self,name):
        print(name)
        print('PSNR\tSAM\tERGAS\tSSIM\tRMSE\n')
        print(self.metrics)
        print(''.center(50,'—'))
        print('\n\n')


if __name__ =='__main__':

    # Quick Settings
    args.save_path='Result/'
    args.path = 'Dataset/'
    args.sf = 32
    args.d = 2
    srf = np.load('NikonD700.npy')
    saver = saveQUI(args)

    index = 0
    # For simulated experiment

    # Data preprocessing
    Dataset = Dataloader(args, 'HSI', True)
    GT, name = Dataset.load(index)
    LR_HSI, HR_RGB = get_pairs(GT, args.sf, srf)

    # Stage1: Initialization
    X_in = initialization(LR_HSI.copy(), HR_RGB.copy(), args.d, srf, 64, args.sf)
    # Stage2: Modificaiton
    X_mod = Modification(X_in.copy(), HR_RGB.copy(), srf, 64)
    # Stage3: Refinement
    X_re = Refinement(X_mod, HR_RGB, args.beta, args.gamma, srf.T)

    # Quantitative Result
    saver.step(GT, X_re)
    saver.save()
    saver.print(name)
    # Save Reconstructed HR-HSI
    Dataset.save(args,X_re)
