import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

import random
import os
import shutil
import glob
class get_data_sets():
    '''
    input_address：输入地址
    output_adddress：输出的地址
    train_ratio：训练集站比，(0,1)
    '''
    def __init__(self,input_address,output_address, train_ratio):
        self.__input_address = input_address
        self.__output_address = output_address
        self.__train_ratio = train_ratio
    def run(self):
        #获取数据种类
        class_address_list = glob.glob(self.__input_address + '\*')
        class_name_list = [ class_address.split('\\')[-1] for class_address in class_address_list ]
        #print
        print('数据分类为 {} \n训练集占比 {}'.format((class_name_list), self.__train_ratio))
        
        #新建训练、测试文件夹
        train_address = self.__output_address + '/train'
        test_address = self.__output_address + '/test'
        
        os.mkdir(train_address)
        os.mkdir(test_address)
        
        #在训练、测试文件夹 新建 类型 文件
        for class_name in class_name_list:
            os.mkdir(train_address + '/{}'.format(class_name))
            os.mkdir(test_address + '/{}'.format(class_name))
        
        #获取训练、测试数据
        class_num = [ len(os.listdir(all_class_address))  for all_class_address in class_address_list ] # 获取每类数据长度
        
        random.seed(2) #设置种子，保证每次分类一致
        train_address_list = [train_address + '/{}'.format(class_name)  for class_name in class_name_list]
        test_address_list = [test_address + '/{}'.format(class_name)  for class_name in class_name_list]

        #复制文件
        for i,num in enumerate(class_num):
            all_index = set(range(num))
            train_index = random.sample(all_index,int(self.__train_ratio*num))
            test_index = all_index - set(train_index)
            
            data_list = glob.glob(class_address_list[i] + '\*')
               
            for _ in train_index:
                shutil.copy(data_list[_], train_address_list[i])

            for _ in test_index:
                shutil.copy(data_list[_], test_address_list[i] )
        
        print('创建完成')
        

input_address = r"/content/workspace/training/images/train"
output_address = r"/content/workspace/training/images/test"
a = get_data_sets(input_address,output_address,0.8)
a.run()
