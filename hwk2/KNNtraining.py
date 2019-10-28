import pickle
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-21_16-08-50.pickle" , "rb") as f1:
    date_list_1 = pickle.load(f1)
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-21_16-14-09.pickle" , "rb") as f2:
    date_list_2 = pickle.load(f2)
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-21_16-21-16.pickle" , "rb") as f3:
    date_list_3 = pickle.load(f3)
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-21_16-24-53.pickle" , "rb") as f4:
    date_list_4 = pickle.load(f4)
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-21_16-25-53.pickle" , "rb") as f5:
    date_list_5 = pickle.load(f5)
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-21_16-26-53.pickle" , "rb") as f6:
    date_list_6 = pickle.load(f6)
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-21_16-27-51.pickle" , "rb") as f7:
    date_list_7 = pickle.load(f7)
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-21_17-10-23.pickle" , "rb") as f8:
    date_list_8 = pickle.load(f8)
with open ("C:\\Users\\b510\\Desktop\\chan\\riiiiiip\\MLGame-master\\games\\arkanoid\\log\\2019-10-22_14-26-02.pickle" , "rb") as f9:
    date_list_9 = pickle.load(f9)
Frame = [ ]
Status = [ ]
Ballposition = [ ]
Platformposition = [ ]
Bricks = [ ]
for i in range (0,len(date_list_1)):
    Frame.append(date_list_1[i].frame)
    Status.append(date_list_1[i].status)
    Ballposition.append(date_list_1[i].ball)
    Platformposition.append(date_list_1[i].platform)
    Bricks.append(date_list_1[i].bricks)
for i in range (0,len(date_list_2)):
    Frame.append(date_list_2[i].frame)
    Status.append(date_list_2[i].status)
    Ballposition.append(date_list_2[i].ball)
    Platformposition.append(date_list_2[i].platform)
    Bricks.append(date_list_2[i].bricks)
for i in range (0,len(date_list_3)):
    Frame.append(date_list_3[i].frame)
    Status.append(date_list_3[i].status)
    Ballposition.append(date_list_3[i].ball)
    Platformposition.append(date_list_3[i].platform)
    Bricks.append(date_list_3[i].bricks)
for i in range (0,len(date_list_4)):
    Frame.append(date_list_4[i].frame)
    Status.append(date_list_4[i].status)
    Ballposition.append(date_list_4[i].ball)
    Platformposition.append(date_list_4[i].platform)
    Bricks.append(date_list_4[i].bricks)
for i in range (0,len(date_list_5)):
    Frame.append(date_list_5[i].frame)
    Status.append(date_list_5[i].status)
    Ballposition.append(date_list_5[i].ball)
    Platformposition.append(date_list_5[i].platform)
    Bricks.append(date_list_5[i].bricks)
for i in range (0,len(date_list_6)):
    Frame.append(date_list_6[i].frame)
    Status.append(date_list_6[i].status)
    Ballposition.append(date_list_6[i].ball)
    Platformposition.append(date_list_6[i].platform)
    Bricks.append(date_list_6[i].bricks)
for i in range (0,len(date_list_7)):
    Frame.append(date_list_7[i].frame)
    Status.append(date_list_7[i].status)
    Ballposition.append(date_list_7[i].ball)
    Platformposition.append(date_list_7[i].platform)
    Bricks.append(date_list_7[i].bricks)
for i in range (0,len(date_list_8)):
    Frame.append(date_list_8[i].frame)
    Status.append(date_list_8[i].status)
    Ballposition.append(date_list_8[i].ball)
    Platformposition.append(date_list_8[i].platform)
    Bricks.append(date_list_8[i].bricks)
for i in range (0,len(date_list_9)):
    Frame.append(date_list_9[i].frame)
    Status.append(date_list_9[i].status)
    Ballposition.append(date_list_9[i].ball)
    Platformposition.append(date_list_9[i].platform)
    Bricks.append(date_list_9[i].bricks)


#----------------------------------------------------------------------------------------------------------------------------
import numpy as np
PlatX = np.array(Platformposition)[:,0][:,np.newaxis]
PlatX_next = PlatX[1:,:]
instruct = (PlatX_next - PlatX[0:len(PlatX_next),0][:, np.newaxis])/5

BallX = np.array(Ballposition)[:,0][:,np.newaxis]
BallX_next = BallX[1:,:]
vx = (BallX_next - BallX[0:len(BallX_next),0][:,np.newaxis])

BallY = np.array(Ballposition)[:,1][:,np.newaxis]
BallY_next = BallY[1:,:]
vy = (BallY_next - BallY[0:len(BallY_next),0][:,np.newaxis])

Ballarray = np.array(Ballposition[:-1])
x = np.hstack((Ballarray , PlatX[0:-1,0][:,np.newaxis],vx,vy))

y = instruct

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

#----------------------------------------------------------------------------------------------------------------------------
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
knn = KNeighborsClassifier(n_neighbors = 1)

knn.fit(x_train,y_train)

yknn_bef_scaler = knn.predict(x_test)
acc_knn_bef_scaler = accuracy_score(yknn_bef_scaler, y_test)


#----------------------------------------------------------------------------------------------------------------------------
filename = "knn_example.sav"
pickle.dump(knn , open(filename , 'wb'))


#----------------------------------------------------------------------------------------------------------------------------
