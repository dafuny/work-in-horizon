#!/usr/bin/env python3
# coding: utf-8

import os
import os.path as osp
from glob import glob
import sys

sys.path.append('../')
from utils.lighting_test import RenderPipeline
from numpy import *
import scipy.io as sio
import imageio
import time
from utils.inference import get_colors
from utils.params import *
from utils.ddfa import _parse_param

cfg = {
    'intensity_ambient': 0.3,
    'color_ambient': (1, 1, 1),
    'intensity_directional': 0.6,
    'color_directional': (1, 1, 1),
    'intensity_specular': 0.1,
    'specular_exp': 5,
    'light_pos': (0, 0, 5),
    'view_pos': (0, 0, 5)
}


def _to_ctype(arr):
    if not arr.flags.c_contiguous:
        return arr.copy(order='C')
    return arr


def main():
    wd = 'test_res@dense_py'
    if not osp.exists(wd):
        os.mkdir(wd)

    app = RenderPipeline(**cfg)
    img_fps = sorted(glob('test/*.jpg'))
    #     # = sorted(glob('test/*.jpg'))
    # triangles = sio.loadmat('tri_refine.mat')['tri']  # mx3
    triangles = sio.loadmat('../visualize/tri.mat')['tri'].T  # mx3
    triangles = _to_ctype(triangles).astype(np.int32)  # for type compatible
    mean_colors = mean_color(img_fps)
    print('---------mean color of sequence pictures has done----------')
    for img_fp in img_fps[:]:
        vertices = sio.loadmat(img_fp.replace('.jpg', '_0.mat'))['vertex'].T  # mx3
        img = imageio.imread(img_fp).astype(np.float32) / 255.
        colors = get_color_from_meancolor(img_fp, mean_colors)
        img_render = app(vertices, triangles, colors, img)
        # print('Elapse: {:.1f}ms'.format((time.clock() - end) * 1000))
        img_wfp = osp.join(wd, osp.basename(img_fp))
        imageio.imwrite(img_wfp, img_render)
        print('Writing to {}'.format(img_wfp))


def z_min(param, vertices):
    vertices_z_ori = rotated_Z(param)
    vertices_key = vertices.reshape(-1, 1)[keypoints].reshape(-1, 3)
    # 68 landmark
    z_min_left = keypoints[np.where(vertices_key[:, 0] == np.min(vertices_key[:, 0]))[0][0] * 3 + 2]
    z_min_right = keypoints[np.where(vertices_key[:, 0] == np.max(vertices_key[:, 0]))[0][0] * 3 + 2]
    vertices_zmin_left = vertices_z_ori[0, int((z_min_left + 1) / 3 - 1)]  # leftest original z
    vertices_zmin_right = vertices_z_ori[0, int((z_min_right + 1) / 3 - 1)]  # rightest original z
    return vertices_zmin_left, vertices_zmin_right

def z_min_dense(param,vertices):
    vertices_z_ori = rotated_Z(param)
    # dense method
    vertices_zmin_left =vertices_z_ori[0, np.where(vertices[:, 0] == np.min(vertices[:, 0]))[0][0]]
    vertices_zmin_right = vertices_z_ori[0, np.where(vertices[:, 0] == np.max(vertices[:, 0]))[0][0]]
    return vertices_zmin_left, vertices_zmin_right


def x_nose(param):
    vertices_x_ori = rotated_X(param)
    vertices_nose_x = vertices_x_ori[0, int(keypoints[30 * 3] / 3)]
    return vertices_nose_x


def mean_color(img_fps):
    colors_all = np.zeros((len(img_fps), (sio.loadmat(img_fps[0].replace('.jpg', '_0.mat'))['vertex'].T).shape[0],
                           (sio.loadmat(img_fps[0].replace('.jpg', '_0.mat'))['vertex'].T).shape[1]))
    for index, img_fp in enumerate(img_fps):
        vertices = sio.loadmat(img_fp.replace('.jpg', '_0.mat'))['vertex'].T  # mx3
        param = np.loadtxt(img_fp.replace('.jpg', '_param.txt'))
        img = imageio.imread(img_fp).astype(np.float32) / 255.
        z_min_left, z_min_right = z_min_dense(param, vertices)
        #print(z_min_left,z_min_right)
        z_ori = rotated_Z(param)
        x_nose_vertice = x_nose(param)
        x_ori = rotated_X(param)
        colors = get_colors_vis(img, vertices.T, z_min_left, z_min_right, z_ori, x_nose_vertice, x_ori)
        colors_all[index] = colors
    colors_mean = np.nanmean(colors_all, axis=0)
    return colors_mean


def get_colors_vis(image, vertices, z_min_left, z_min_right, z_ori, x_nose_vertice, x_ori):
    # vertices shape [53215,3].T
    [h, w, _] = image.shape
    # vertices_nose_x = (vertices.T.reshape(-1, 1))[keypoints[30 * 3]]
    vertices[0, :] = np.minimum(np.maximum(vertices[0, :], 0), w - 1)  # x
    vertices[1, :] = np.minimum(np.maximum(vertices[1, :], 0), h - 1)  # y
    ind = np.round(vertices).astype(np.int32)
    colors = image[ind[1, :], ind[0, :], :]
    for i in range(vertices.shape[1]):
        if x_ori[0, i] <= x_nose_vertice and z_ori[0, i] <= z_min_left:
            colors[i, :] = None
        elif x_ori[0, i] > x_nose_vertice and z_ori[0, i] <= z_min_right:
            colors[i, :] = None
    return colors


def get_color_from_meancolor(img_fp, mean_color):
    colors = mean_color.copy()
    vertices = sio.loadmat(img_fp.replace('.jpg', '_0.mat'))['vertex'].T  # mx3
    param = np.loadtxt(img_fp.replace('.jpg', '_param.txt'))
    image= imageio.imread(img_fp).astype(np.float32) / 255.
    z_min_left, z_min_right = z_min(param, vertices)
    z_ori = rotated_Z(param)
    x_ori = rotated_X(param)
    x_nose_vertice = x_nose(param)
    [h, w, _] = image.shape
    vertices[0, :] = np.minimum(np.maximum(vertices[0, :], 0), w - 1)  # x
    vertices[1, :] = np.minimum(np.maximum(vertices[1, :], 0), h - 1)  # y
    ind = np.round(vertices.T).astype(np.int32)
    # vertices_nose_x = (vertices.reshape(-1,1))[keypoints[30 * 3]]
    for i in range(vertices.shape[0]):
        if x_ori[0, i] <= x_nose_vertice and z_ori[0, i] <= z_min_left:
            colors[i, :] = image[ind[1, i], ind[0, i], :]
        if x_ori[0, i] > x_nose_vertice and z_ori[0, i] <= z_min_right:
            colors[i, :] = image[ind[1, i], ind[0, i], :]
    return colors


def rotated_Z(param, whitening=True):
    if len(param) == 12:
        param = np.concatenate((param, [0] * 50))
    if whitening:
        if len(param) == 62:
            param = param * param_std + param_mean
        else:
            param = np.concatenate((param[:11], [0], param[11:]))
            param = param * param_std + param_mean

    p, offset, alpha_shp, alpha_exp = _parse_param(param)
    vertex = mat(p @ (u_base + w_shp_base @ alpha_shp + w_exp_base @ alpha_exp).reshape(3, -1, order='F'))
    vertex_ori = mat((u_base + w_shp_base @ alpha_shp + w_exp_base @ alpha_exp).reshape(3, -1, order='F'))
    rotation = vertex_ori * vertex.T * np.linalg.inv(vertex * vertex.T)
    vertex_all = mat(p @ (u + w_shp @ alpha_shp + w_exp @ alpha_exp).reshape(3, -1, order='F'))
    return (rotation * vertex_all)[2, :]


def rotated_X(param, whitening=True):
    if len(param) == 12:
        param = np.concatenate((param, [0] * 50))
    if whitening:
        if len(param) == 62:
            param = param * param_std + param_mean
        else:
            param = np.concatenate((param[:11], [0], param[11:]))
            param = param * param_std + param_mean

    p, offset, alpha_shp, alpha_exp = _parse_param(param)
    vertex = mat(p @ (u_base + w_shp_base @ alpha_shp + w_exp_base @ alpha_exp).reshape(3, -1, order='F'))
    vertex_ori = mat((u_base + w_shp_base @ alpha_shp + w_exp_base @ alpha_exp).reshape(3, -1, order='F'))
    rotation = vertex_ori * vertex.T * np.linalg.inv(vertex * vertex.T)
    vertex_all = mat(p @ (u + w_shp @ alpha_shp + w_exp @ alpha_exp).reshape(3, -1, order='F'))
    return (rotation * vertex_all)[0, :]


if __name__ == '__main__':
    main()
