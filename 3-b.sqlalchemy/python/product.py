#   製品情報メンテナンス
#
from nicegui import ui
from setting import *
from model import *

def page():
    # 新規製品作成
    def add_product():
        product = Product()
        edit_product(product,None)

    # 編集用ダイアログボックスを表示
    def edit_product(product: Product,rowIndex: Integer):
        with ui.dialog() as dialog, ui.card():
                    
            if product.productCode == None:
                ui.input('製品コード').bind_value(product,'productCode')
            else:
                ui.input('製品コード').bind_value(product,'productCode').disable()
            ui.input('製品名').bind_value(product,'productName')
            ui.number('標準価格').bind_value(product,'price')

            with ui.row().classes('w-full justify-center'):
                ui.button('保存', on_click=lambda: save_product(product, dialog, rowIndex))
                ui.button('削除', on_click=lambda: delete_product(product, dialog, rowIndex)).props(f'color="red"')
                ui.button('ｷｬﾝｾﾙ', on_click=lambda: close_dialog(dialog))

        dialog.open()

    # 製品情報の保存
    def save_product(p: Product, dialog: ui.dialog, rowIndex: Integer):
        # バリデーションチェック
        if p.productCode == None or p.productCode == '':
            ui.notify('製品コードが入力されていません',timeout=0,close_button="OK")
            return
        if len(p.productName) == 0:
            ui.notify('製品名が入力されていません',timeout=0,close_button="OK")
            return
        if p.price<= 0:
            ui.notify('標準価格が入力されていません',timeout=0,close_button="OK")
            return

        # 製品情報の保存
        session.merge(p)
        session.commit()

        update_row(p,rowIndex)

        dialog.close()

    # 製品情報の削除
    def delete_product(product: Product,dialog: ui.dialog, rowIndex: Integer):
        if product.productCode != None:
            session.delete(product)
            session.commit()
            delete_row(rowIndex)

        dialog.close()

    # ダイアログを閉じる
    def close_dialog(dialog):
        dialog.close()

    # グリッドの更新
    def update_row(p: Product,rowIndex: Integer):
        pdata={"productCode": p.productCode, "productName": p.productName, "price": p.price}
        if rowIndex == None:
            # rowIndexが指定されていない場合、行を追加
            grid.options['rowData'].append(pdata)
        else:
            grid.options['rowData'][rowIndex] = pdata
        grid.update()

    # グリッドから行を削除
    def delete_row(rowIndex: Integer):
        ui.notify("rowIndex:" + str(rowIndex))
        del grid.options['rowData'][rowIndex]
        grid.update()

    # グリッドにて行が選択されたときの処理
    def row_selected(event):
        if event.args["selected"] == True:
            obj = session.get(Product,event.args["data"]["productCode"])
            if obj != None:
                edit_product(obj,event.args["rowIndex"])

    # 製品情報の取得
    products = session.query(Product).all()
    product_data = [{"productCode": p.productCode, "productName": p.productName, "price": p.price} for p in products]

    # 画面の表示
    with ui.row():
        ui.button('新規', on_click=lambda: add_product())
    
    # グリッドの表示
    grid = ui.aggrid({
        'defaultColDef': {'flex': 1},
        'columnDefs': [
            {'headerName': '製品コード', 'field': 'productCode', 'checkboxSelection': True},
            {'headerName': '製品名', 'field': 'productName'},
            {'headerName': '標準価格', 'field': 'price'},
        ],
        'rowData': product_data,
    }).on('rowSelected', lambda event: row_selected(event))
