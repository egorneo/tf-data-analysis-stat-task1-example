import pandas as pd
import numpy as np


chat_id = 341617769 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = x - 335
    est = np.log(np.median(x))
    return est + 335 # Ваш ответ
