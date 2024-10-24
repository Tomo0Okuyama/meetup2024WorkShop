#   顧客情報メンテナンス
#
from nicegui import ui,run
from setting import *
from model import *
from datetime import date

import requests
import json

def page():
    # 新規顧客作成
    def add_customer():
        customer = Customer()
        edit_customer(customer,None)

    # 編集用ダイアログボックスを表示
    def edit_customer(customer: Customer,rowIndex: Integer):
        with ui.dialog() as dialog, ui.card():
            # 郵便番号検索
            async def invoke_zipcode(zipcode):
                URL = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode='+zipcode
                response = await run.io_bound(requests.get, URL, timeout=10)
                if response.status_code == 200:
                    result = json.loads(response.content.decode('utf-8'))
                    address = result["results"][0]
                    address_input.value = address["address1"] + " " + address["address2"] +" " +  address["address3"]
                else:
                    ui.notify(f'郵便番号検索時にエラーが発生しました StatusCode={response.status_code})',timeout=0,close_button="OK")
                    
            if customer.customerId == None:
                ui.input('顧客ID').bind_value(customer,'customerId')
            else:
                ui.input('顧客ID').bind_value(customer,'customerId').disable()
            with ui.row():
                ui.input('姓').bind_value(customer,'lastName')
                ui.input('名').bind_value(customer,'firstName')

            with ui.row():
                ui.input('カナ姓').bind_value(customer, 'lastNameKana')
                ui.input('カナ名').bind_value(customer,'firstNameKana')

            with ui.row():
                with ui.input('生年月日') as dob_input:
                    dob_input.bind_value(customer,'dob')
                    with ui.menu().props('no-parent-event') as dob_menu:
                        with ui.date().bind_value(dob_input):
                            with ui.row().classes('justify-end'):
                                ui.button('閉じる', on_click=dob_menu.close).props('flat')
                    with dob_input.add_slot('append'):
                        ui.icon('edit_calendar').on('click', dob_menu.open).classes('cursor-pointer')

                def select_gender(item):
                    gender_input.text=item
                
                def set_gender(str):
                    if str == '男性' or str == '女性':
                        return str
                    else:
                        return None
                def get_gender(str):
                    if str == '男性' or str == '女性':
                        return str
                    else:
                        return '性別'
                
                with ui.dropdown_button('性別', auto_close=True) as gender_input:
                    gender_input.bind_text(customer,'gender',forward= lambda x: set_gender(x), backward= lambda x: get_gender(x))
                    ui.item('男性', on_click=lambda: select_gender('男性'))
                    ui.item('女性', on_click=lambda: select_gender('女性'))

            with ui.row(wrap=False):
                ui.input('郵便番号').bind_value(customer,'zipCode').props("size=30")
                ui.button('検索',on_click= lambda: invoke_zipcode(customer.zipCode)).classes("w-32")
                address_input = ui.input('住所').bind_value(customer,'address').props("size=120")
            
            ui.input('電話番号').bind_value(customer,'phone')

            with ui.row().classes('w-full justify-center'):
                ui.button('保存', on_click=lambda: save_customer(customer, dialog, rowIndex))
                ui.button('削除', on_click=lambda: delete_customer(customer, dialog, rowIndex)).props(f'color="red"')
                ui.button('ｷｬﾝｾﾙ', on_click=lambda: close_dialog(dialog))

        dialog.open()

    # 顧客情報の保存
    def save_customer(c: Customer, dialog: ui.dialog, rowIndex: Integer):
        # バリデーションチェック
        if c.customerId == None or c.customerId == '':
            ui.notify('顧客IDが入力されていません',timeout=0,close_button="OK")
            return
        if len(c.lastName) == 0 or len(c.firstName) == 0:
            ui.notify('氏名が入力されていません',timeout=0,close_button="OK")
            return
        if len(c.lastNameKana) == 0 or len(c.firstNameKana) == 0:
            ui.notify('カナが入力されていません',timeout=0,close_button="OK")
            return
        try:
            if type(c.dob) is str:
                c.dob = date.fromisoformat(c.dob)
        except Exception as err:
            ui.notify('生年月日の形式が誤っています',timeout=0,close_button="OK")
            return
        if len(c.gender) == 0:
            ui.notify('性別が入力されていません',timeout=0,close_button="OK")
            return

        # 顧客情報の保存
        session.merge(c)
        session.commit()

        update_row(c,rowIndex)

        dialog.close()

    # 顧客情報の削除
    def delete_customer(customer: Customer,dialog: ui.dialog, rowIndex: Integer):
        if customer.customerId != None:
            session.delete(customer)
            session.commit()
            delete_row(rowIndex)

        dialog.close()

    # ダイアログを閉じる
    def close_dialog(dialog):
        dialog.close()

    # グリッドの更新
    def update_row(c: Customer,rowIndex: Integer):
        cdata={"customerId": c.customerId, "lastName": c.lastName, "firstName": c.firstName,
                  "lastNameKana": c.lastNameKana, "firstNameKana": c.firstNameKana, "dob": c.dob,
                  "gender": c.gender}
        if rowIndex == None:
            # rowIndexが指定されていない場合、行を追加
            grid.options['rowData'].append(cdata)
        else:
            grid.options['rowData'][rowIndex] = cdata
        grid.update()

    # グリッドから行を削除
    def delete_row(rowIndex: Integer):
        ui.notify("rowIndex:" + str(rowIndex))
        del grid.options['rowData'][rowIndex]
        grid.update()

    # グリッドにて行が選択されたときの処理
    def row_selected(event):
        if event.args["selected"] == True:
            obj = session.get(Customer,event.args["data"]["customerId"])
            if obj != None:
                edit_customer(obj,event.args["rowIndex"])

    # 顧客情報の取得
    customers = session.query(Customer).all()
    customer_data = [{"customerId": c.customerId, "lastName": c.lastName, "firstName": c.firstName,
                  "lastNameKana": c.lastNameKana, "firstNameKana": c.firstNameKana, "dob": c.dob,
                  "gender": c.gender} for c in customers]

    # 画面の表示
    with ui.row():
        ui.button('新規顧客', on_click=lambda: add_customer())
    
    # グリッドの表示
    grid = ui.aggrid({
        'defaultColDef': {'flex': 1},
        'columnDefs': [
            {'headerName': '顧客ID', 'field': 'customerId', 'checkboxSelection': True},
            {'headerName': '姓', 'field': 'lastName'},
            {'headerName': '名', 'field': 'firstName'},
            {'headerName': 'カナ姓', 'field': 'lastNameKana'},
            {'headerName': 'カナ名', 'field': 'firstNameKana'},
            {'headerName': '生年月日', 'field': 'dob'},
            {'headerName': '性別', 'field': 'gender'},
        ],
        'rowData': customer_data,
    }).on('rowSelected', lambda event: row_selected(event))
