import os 
import math
import re
from operator import itemgetter
def strtodic(input):
  dic={}
  file_content_list=input.split()
  for term in file_content_list:
    word_list=term.split(':')
    word=word_list[0]
    num=word_list[1]
    dic[word]=num
  return dic
def get_vector(txt_dic,dic,new_txt_path):
  for tf_term,num_doc in dic.items():
    dic[tf_term]='0'
  for txt_term,num in txt_dic.items():
    dic[txt_term]=num
  fileopen=open(new_txt_path,'w')
  for tf_term,num_doc in dic.items():
    fileopen.write(num_doc+'\n')
  fileopen.close()
if __name__ == '__main__':
    path="text4"
    result_path="text5"
    idf_filename="idf_stop_seq.txt"
    stopword_filename="stop_word.txt"
    idffile=open(idf_filename,'r')
    num_docs=idffile.readline()
    print num_docs
    idffilecontents=idffile.read()
    #print idffilecontents
    dic={}
    dic=strtodic(idffilecontents)
    #print dic
    L=os.listdir(path)
    #print L 
    for folder_name in L:
          new_path=path+"\\"+folder_name
          #print new_path
          mkdir_path=result_path+"\\"+folder_name
          print mkdir_path
          os.makedirs(mkdir_path)
          txt_list=os.listdir(new_path)
          for txt_name in txt_list:
            txt_path=new_path+"\\"+txt_name
            #print txt_path
            new_txt_path=mkdir_path+"\\"+txt_name
            print new_txt_path
            txt_open=file(txt_path,'r')
            txt_content=txt_open.read()
            txt_dic=strtodic(txt_content)
            get_vector(txt_dic,dic,new_txt_path)


            
            


                    






              




      
