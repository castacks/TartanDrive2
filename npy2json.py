import numpy as np
import json
import os
import matplotlib.pyplot as plt

prefix = 'data/'
dirs = ['0','1']

for d in dirs:
    folder = prefix + d
    datas = os.listdir(folder)
    for data in datas:
        subdir = os.path.join(folder,data)
        files = os.listdir(subdir)
        for file in files:
            if '.npy' in file:
                # print(file)
                inname = os.path.join(subdir,file)
                points = np.load(inname)
                if 'cloud' in data:
                    # print('cropping')
                    points = points[np.linalg.norm(points,axis=1) < 50,:]
                    # plt.plot(points[:,0],points[:,1],'.')
                    # print(np.min(points,axis=0),np.max(points,axis=0))
                    # plt.show()
                # print(pts.shape)
                outname = os.path.join(subdir,file.replace('.npy','.json'))
                if points.shape == 6:
                    print('RGB POINTCLOUD')
                    points_list = {"x": points[:,0].tolist(), "y": points[:,1].tolist(), "z": points[:,2].tolist(), "r": points[:,3].tolist(), "g": points[:,4].tolist(), "b": points[:,5].tolist()}
                else:
                    points_list = {"x": points[:,0].tolist(), "y": points[:,1].tolist(), "z": points[:,2].tolist()}
                points_json = json.dumps(points_list, indent=4)
                with open(outname, 'w') as file:
                    file.write(points_json)

# Example array of points (replace this with your own data loading)
# path = 'data/1/pc/0.npy'
# points = np.load(path)
# # Convert the numpy array to a list of dictionaries
# points_list = {"x": points[:,0].tolist(), "y": points[:,1].tolist(), "z": points[:,2].tolist()}
#
#
# # Convert the list of dictionaries to JSON format
# points_json = json.dumps(points_list, indent=4)
#
# # Save or print the resulting JSON
#
# with open(path.replace('npy','json'), 'w') as file:
#     file.write(points_json)
