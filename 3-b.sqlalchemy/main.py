from contextlib import contextmanager
from nicegui import ui
from setting import *
from model import *
from sqlalchemy import func

import datetime
import customer
import product

@ui.page('/customer')
def customer_page() -> None:
    with frame('顧客情報メンテ'):
        customer.page()

@ui.page('/product')
def product_page() -> None:
    with frame('製品情報メンテ'):
        product.page()

@ui.page('/')
def page():
    # 直近の売り上げを表示
    today = datetime.datetime.today()
    # 月始めを求める
    thisMonth = today.replace(day=1)
    lastMonth = (thisMonth - datetime.timedelta(days=1)).replace(day=1)
    last2Month = (lastMonth - datetime.timedelta(days=1)).replace(day=1)
    # 今月の売り上げ 
    result1 = session.query(func.sum(Transactions.total)).where(Transactions.dateTime >= thisMonth).all()
    # 先月の売り上げ 
    result2 = session.query(func.sum(Transactions.total)).where(Transactions.dateTime.between(lastMonth,thisMonth)).all()
    # 先々月の売り上げ 
    result3 = session.query(func.sum(Transactions.total)).where(Transactions.dateTime.between(last2Month,lastMonth)).all()

    with frame('メインページ'):
        ui.label('ようこそ').tailwind.font_size('xl')
        ui.space()
        ui.label('現在の売上高')
        echart = ui.echart({
            'xAxis':{ 'type': 'category', 'data': ['先々月', '先月', '今月'], 'inverse': True},
            'yAxis':{ 'type': 'value'},
            'series':[{'name': 'Direct', 'type': 'bar', 'barWidth':'60%', 'data':[ result3[0][0], result2[0][0], 
                        {
                            'value': result1[0][0],
                            'itemStyle': { 'color': '#c94444' }
                        }]
            }],
        }).classes('w-1/2 h-96')

# サーバの実行
ui.run()

@contextmanager
def frame(navigation_title: str):
    with ui.header():
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu'):
                with ui.menu() as menu:
                    ui.menu_item('トップページ', lambda: ui.navigate.to('/'))
                    ui.menu_item('顧客メンテ', lambda: ui.navigate.to('/customer'))
                    ui.menu_item('製品メンテ', lambda: ui.navigate.to('/product'))
                    ui.separator()
                    ui.menu_item('Close', menu.close)
            ui.label(navigation_title).tailwind.font_weight('extrabold').font_size('xl')
    yield
