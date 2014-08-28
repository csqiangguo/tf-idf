import os 
import math
import re
from operator import itemgetter

class TfIdf:
  def __init__(self, corpus_filename = None, stopword_filename = None,DEFAULT_IDF = 1.5):
    self.num_docs = 0
    self.term_num_docs = {}
    self.stopwords = []
    self.idf_default = DEFAULT_IDF
    if corpus_filename:
      corpus_file = open(corpus_filename, "r")
      line = corpus_file.readline()
      self.num_docs = int(line.strip())
      for line in corpus_file:
        tokens = line.split(":")
        term = tokens[0].strip()
        frequency = int(tokens[1].strip())
        self.term_num_docs[term] = frequency
    if stopword_filename:
      stopword_file = open(stopword_filename, "r")
      self.stopwords = [line.strip() for line in stopword_file]
  def get_tokens(self, str):
    return re.findall(r"\w+", str.lower())
  def add_input_document(self, input):
    self.num_docs += 1
    words = set(self.get_tokens(input))
    for word in words:
      if word in self.term_num_docs:
        self.term_num_docs[word] += 1
      else:
        self.term_num_docs[word] = 1
  def save_corpus_to_file(self, idf_filename, stopword_filename, STOPWORD_PERCENTAGE_THRESHOLD = 0.01):
    sorted_terms = sorted(self.term_num_docs.items(), key=itemgetter(1), reverse=True)
    stopword_file = open(stopword_filename, "w")
    for term, num_docs in sorted_terms:
      if num_docs < STOPWORD_PERCENTAGE_THRESHOLD * self.num_docs:
        break
      self.stopwords.append(term)
      stopword_file.write(term + "\n")
  def get_num_docs(self):
    return self.num_docs
  def get_idf(self, term):
    if term in self.stopwords:
      return 0
    if not term in self.term_num_docs:
      return self.idf_default
    return math.log(float(1 + self.get_num_docs()) / (1 + self.term_num_docs[term]))
  def get_doc_keywords(self, curr_doc,new_txt_path,list1):
    tf = {}
    tokens = self.get_tokens(curr_doc)
    tokens_set = set(tokens)
    for word in tokens_set:
      mytf = float(tokens.count(word))
      tf[word] = mytf
    sorted_terms=sorted(tfidf.items(), key=itemgetter(1), reverse=True)
    for term,num in sorted_terms:
        if self.term_num_docs[term]==2 and tf[term]>5:
          if not term in list1:
            list1.append(term)
  def changeidf(self,list1,path):
    num=0
    sorted_terms = sorted(self.term_num_docs.items(), key=itemgetter(1), reverse=True)
    output_stop_file = open(path, "w")
    output_stop_file.write(str(self.num_docs) + "\n")
    for term, num_docs in sorted_terms:
      if term in self.stopwords:
        continue
      if num_docs==2 and (not term in list1):
        print term
        print ' '
        num=num+1
        continue
      if self.term_num_docs[term]==1:
        break
      output_stop_file.write(term + ":" + str(num_docs) + "\n")
    
if __name__ == '__main__':
    obj=TfIdf()
    path="text3"
    result_path="tf_eachtxt"
    idf_filename="idf_stop_seq.txt"
    stopword_filename="stop_word.txt"
    L=os.listdir(path) 
    list1=[]
    #print L 
    if len(L)!=0:
      for folder_name in L:
          new_path=path+"\\"+folder_name
          txt_list=os.listdir(new_path)
          for txt_name in txt_list:
            txt_path=new_path+"\\"+txt_name
            txt_open=file(txt_path,'r')
            txt_content=txt_open.read()
            obj.add_input_document(txt_content)
    obj.save_corpus_to_file(idf_filename,stopword_filename)
    for folder_name in L:
          new_path=path+"\\"+folder_name
          print new_path
          mkdir_path=result_path+"\\"+folder_name
          print mkdir_path
          txt_list=os.listdir(new_path)
          for txt_name in txt_list:
            txt_path=new_path+"\\"+txt_name
            print txt_path
            new_txt_path=mkdir_path+"\\"+txt_name
            print new_txt_path
            txt_open=file(txt_path,'r')
            txt_content=txt_open.read()
            
    obj.changeidf(list1,idf_filename)
    print list1
    idfsave="D:\\MultimediaDataset\\textDataSet\\baoliudifi.txt"
    filesave=open(idfsave,'w')
    for term,num in obj.term_num_docs.items():
      if obj.term_num_docs[term]==2:
        if not term in list1:
          filesave.write(term+'\n')





            
            


                    






              




      
