# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QObject


def set_shadow_effect(widget: QObject, color=Qt.gray, radius=20, visible=True):
    """ 设置控件阴影\n
    Args:\n
        widget: 控件对象
        color: 阴影颜色
        radius: 阴影半径，默认为0
        visible: 是否可见，为False的时候
    """
    shadowEffect = QGraphicsDropShadowEffect()
    shadowEffect.setOffset(0, 0)
    if visible is True:
        shadowEffect.setColor(color)
        shadowEffect.setBlurRadius(radius)
    else:
        shadowEffect.setColor(Qt.white)
        shadowEffect.setBlurRadius(0)
    widget.setGraphicsEffect(shadowEffect)
