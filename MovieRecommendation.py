import random as rd
import numpy as np
import pandas as pd


def generate_data():
    users = np.random.randint(10000, 99999, 5)
    users_data = pd.DataFrame(index=movies, columns=users)
    for user in users:
        num = rd.randint(5, 10)  # 用户看了几部
        for i in range(num):
            movie = movies[rd.randint(0, 9)]  # 看了的电影序号
            users_data[user][movie] = round(rd.uniform(1, 5), 1)  # 打分
    print('用户点评表格\n', users_data, '\n')
    movie_point = round(users_data.mean(axis=1), 1)  # 求出电影的平均值
    print('电影评分\n', movie_point, '\n')
    new_user = rd.randint(10000, 99999)  # 新用户
    while new_user in users:  # 判断用户id是否存在
        new_user = rd.randint(10000, 99999)  # 已存在重新生成
    else:
        print('新用户：', new_user)  # 不存在，输出
    new_user_movie = pd.Series(np.NaN, index=movies)  # 为新用户生成一个Series存放电影评分
    num = rd.randint(3, 10)  # 看过几部
    for i in range(num):
        movie = movies[rd.randint(0, 9)]  # 看了电影的序号
        new_user_movie[movie] = round(rd.uniform(1, 5), 1)  # 打分
    print('新用户电影评分\n', new_user_movie, '\n')
    score_variance = (users_data.sub(new_user_movie, axis=0)**2).sum(axis=0)  # 看过的相同电影评分的方差
    score_variance = score_variance.sort_values()  # 排序
    print('用户观看相同电影方差\n', score_variance, '\n')
    for variance in score_variance:
        minimum_variance_list = list(users_data[score_variance.index[0]].dropna(inplace=False).index)
        # 评分方差最小的用户的观看列表
        watched_list = list(new_user_movie.dropna(inplace=False).index)  # 用户已看的电影列表
        print("该用户已看电影:", watched_list, "\n观看相同电影评分方差最小用户已看电影:", minimum_variance_list)
        recommended_list = set(minimum_variance_list).difference(set(watched_list))  # 生成推荐列表
        if not recommended_list:  # 如果推荐列表为空，则说明后者包含前者
            continue
        elif variance == 0:  # 必须考虑二者的观影没有重合的情况，此时二者的方差为0
            continue
        else:
            print('推荐电影:', recommended_list)
            break


__name__
movies = ['千与千寻', '哈尔的移动城堡', '幽灵公主', '魔女宅急便', '红猪',
          '龙猫', '你的名字', '声之形', '天气之子', '秒速五厘米']
generate_data()
