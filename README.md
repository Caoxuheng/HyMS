![TITLE](https://github.com/Caoxuheng/imgs/blob/main/TSMF.jpg)
# [Hyperspectral Image Super-resolution via Multi-stage Scheme without Employing Spatial Degradation](https://doi.org/10.1364/OL.473020)
This is an optimization-based algorithm that fuses hyperspectral and RGB images without employing spatial degradation.  For an HSI with the size of 16x16x31, the proposed HSMS can achieve 32x spatial improvement with high accuracy in 2 seconds. The quantitative results outperform the existing optimized-based algorithm and most deep-learning-based algorithms.    
The code will be released soon.  
***The paper has been accepted by Optics Letters***  
For a better study, we publish an online version based on AI-Studio. You can apply our algorithm on the CAVE dataset without configuring the system environment >>>>[*Online Version*](https://aistudio.baidu.com/aistudio/projectdetail/4418051)<<<<
# Note
There are two versions of HSMS. The GPU-based one and CPU-based one. GPU-based methods can complete super-resolution tasks in a short amount of time, but since GPU-based Newton's methods do not take into account that the denominator cannot be zero, this version may fail on some images. The CPU-based one is the stable version.
# Flowchart
![Flowchart](https://github.com/Caoxuheng/imgs/blob/main/ol2.png)  
# Result presentation  
![Simulate](https://github.com/Caoxuheng/imgs/blob/main/ol23.png)
![Real](https://github.com/Caoxuheng/imgs/blob/main/ol2real.png)
# Guidance  
Add your dataset path in `config.py`  
run `main.py` to simulated experment   
## Running interface  
![Introduce](https://github.com/Caoxuheng/imgs/blob/main/Rins.png)
# Requirements  
## Environment  
`Python 3.8`  
`Numba`, `Cupy`  
`Numpy`, `Scipy`, `Opencv`
## Datasets
[`CAVE dataset`](https://www1.cs.columbia.edu/CAVE/databases/multispectral/), 
 [`Preprocessed CAVE dataset`](https://aistudio.baidu.com/aistudio/datasetdetail/147509).
# Note
For any questions, feel free to email me at caoxuhengcn@gmail.com.  
If you find our work useful in your research, please cite our paper ^.^
```python  
@article{article,
author = {Cao, Xuheng and Lian, Yusheng and Liu, Zilong and Zhou, Han and Bin, Wang and Zhang, Wan and Huang, Beiqing},
year = {2022},
month = {09},
pages = {5184-5187},
title = {Hyperspectral Image Super-resolution via Multi-stage Scheme without Employing Spatial Degradation},
journal = {Optics Letters},
doi = {10.1364/OL.473020}
}
