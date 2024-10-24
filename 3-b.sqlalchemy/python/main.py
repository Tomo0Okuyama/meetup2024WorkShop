from contextlib import contextmanager
from nicegui import ui
from setting import *
from model import *
from sqlalchemy import func

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
    with frame('メインページ'):
        ui.label('ようこそ').font_size('xl')

# サーバの実行
ui.run()

@contextmanager
def frame(navigation_title: str):
    #ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
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
