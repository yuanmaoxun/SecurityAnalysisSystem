class Data:
    colsize="" #数据特征的长度
    x_fath="" #训练数据的文件路径
    c_fath="" #测试数据的文件路径
    clf=None  #数据训练后的结果
    s_X=None
#SVM分类用到的参数
    C = 1.0
    kernel = "rbf"
    degree = 2
    gamma = 1
    coef0 = 0.0
    probability = False
    shrinking = True
    tol = 0.001
    cache_size = 200
    max_iter = -1
