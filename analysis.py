import csv

#统计各类资源总体下载量
kind_list=['movie','study','sports','game','music']
index=-1
total=[0,0,0,0,0]
for kind in kind_list:
    index=index+1
    for i in range(200):
        filename='./%s用户下载数据/%s_%d.csv'%(kind,kind,i+1)  #文件路径
        total[index] += len(open(filename,encoding='utf-8').readlines())-1

print('The total download of Movie is ',total[0])
print('The total download of Study is ',total[1])
print('The total download of Sports is ',total[2])
print('The total download of Game is ',total[3])
print('The total download of Music is ',total[4])

#统计各类资源的下载分布情况
kind_list=['movie','study','sports','game','music']
for kind in kind_list:
    fp = open('./ana_%s.csv'%kind,'w',newline = '',encoding='ansi')
    fp_write=csv.writer(fp)    
    for i in range(200):
        filename='./%s用户下载数据/%s_%d.csv'%(kind,kind,i+1)   #文件路径
        total= len(open(filename,encoding='utf-8').readlines())-1
        fp_write.writerow(['%s'%total])

#统计某个资源分类中出现指定用户或者类别的数量
kind_list=['movie','study','sports','game','music']
index=-1
total=[0,0,0,0,0]
for kind in kind_list:
    index=index+1
    for i in range(200):
        filename='./%s用户下载数据/%s_%d.csv'%(kind,kind,i+1)  #文件路径
        with open('./%s用户下载数据/%s_%d.csv'%(kind,kind,i+1),encoding='utf-8') as f:
            data = csv.reader(f)
            for s,lines in enumerate(data):
                if lines[0] == 'renshuxian':
                    total[index] +=1
print('The total download of Movie is ',total[0])
print('The total download of Study is ',total[1])
print('The total download of Sports is ',total[2])
print('The total download of Game is ',total[3])
print('The total download of Music is ',total[4]) 

#统计某个资源分类中出现指定用户或者类别的数量
kind_list=['movie','study','sports','game','music']
index=-1
total=[0,0,0,0,0]
for kind in kind_list:
    index=index+1
    for i in range(200):
        filename='./%s用户下载数据/%s_%d.csv'%(kind,kind,i+1)  #文件路径
        with open('./%s用户下载数据/%s_%d.csv'%(kind,kind,i+1),encoding='utf-8') as f:
            data = csv.reader(f)
            for s,lines in enumerate(data):
                if lines[0] == 'renshuxian':
                    total[index] +=1
print('The total download of Movie is ',total[0])
print('The total download of Study is ',total[1])
print('The total download of Sports is ',total[2])
print('The total download of Game is ',total[3])
print('The total download of Music is ',total[4]) 

#统计某个特定资源的用户等级分布情况

total=[0,0,0,0,0,0,0]
with open('./movie用户下载数据/movie_1.csv',encoding='utf-8') as f:
    data = csv.reader(f)
    for s,lines in enumerate(data):
        if lines[1] == '江湖侠隐':
            total[0] +=1
        if lines[1] == '世外高人':
            total[1] +=1
        if lines[1] == '无双隐士':
            total[2] +=1
        if lines[1] == '风尘奇侠':
            total[3] +=1
        if lines[1] == '武林高手':
            total[4] +=1
        if lines[1] == '后起之秀':
            total[5] +=1
        if lines[1] == '江湖小虾':
            total[6] +=1
print('The total download of 江湖侠隐 is ',total[0])
print('The total download of 世外高人 is ',total[1])
print('The total download of 无双隐士 is ',total[2])
print('The total download of 风尘奇侠 is ',total[3])
print('The total download of 武林高手 is ',total[4])
print('The total download of 后起之秀 is ',total[5]) 
print('The total download of 江湖小虾 is ',total[6]) 

        