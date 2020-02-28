import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
import seaborn as sns

#Importing Dataset
dataset = pd.read_csv('CC.csv')

#Finding the top 5 most correlated columns to the target variable
numeric_features = dataset.select_dtypes(include=[np.number])
corr = numeric_features.corr()
#print(corr)
print(corr['TENURE'].sort_values(ascending=False)[:6])

#Eliminating the null values
data = dataset.select_dtypes(include=[np.number]).interpolate().dropna()
#print(data)

#assigning data to the independent variable
x = data.iloc[:,[2,3,-4,-5,-6]]
y = data.iloc[:,-1]

#Scaling the data
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_initial = scaler.transform(x)
X_scaled_final = pd.DataFrame(X_scaled_initial, columns = x.columns)

pca = PCA(2)
x_pca = pca.fit_transform(X_scaled_final)
df1 = pd.DataFrame(data=x_pca)
df_final = pd.concat([df1,dataset[['TENURE']]],axis=1)
print(df_final)

from sklearn import metrics
wcss = []
# ##elbow method to know the number of clusters
for i in range(2,5):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(df1)
   #print(kmeans.inertia_,'-------------------')
    wcss.append(kmeans.inertia_)
    score = silhouette_score(df1, kmeans.labels_, metric='euclidean')
    print("For n_clusters = {}, silhouette score is {})".format(i, score))
plt.plot(range(1, 4), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

nclusters = 2 # this is the k in kmeans
seed = 0
km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(x_pca) # predict the cluster for each data point
y_cluster_kmeans = km.predict(x_pca)
#plt.plot(X_scaled_final,y_cluster_kmeans)
#plt.show()
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y_cluster_kmeans, cmap='rainbow')
plt.show()
#centers = km.cluster_centers_
#plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)