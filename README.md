![TITLE](https://github.com/Caoxuheng/imgs/blob/main/TSMF.jpg)
# [Hyperspectral Image Super-resolution via Multi-stage Scheme without Employing Spatial Degradation](https://doi.org/10.1364/OL.473020)
This is an optimization-based algorithm that fuses hyperspectral and RGB images without employing spatial degradation.  For an HSI with the size of 16x16x31, the proposed HSMS can achieve 32x spatial improvement with high accuracy in 2 seconds. The quantitative results outperform the existing optimized-based algorithm and most deep-learning-based algorithms.    
The code will be released soon.  
***The paper has been accepted by Optics Letter***  
For a better study, we publish an online version based on AI-Studio. You can apply our algorithm on the CAVE dataset without configuring the system environment >>>>[*Online Version*](https://aistudio.baidu.com/aistudio/projectdetail/4418051)<<<<
# Flowchart
**None**  
# Result presentation  
**None**  
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
