from flask import Flask, jsonify, session, render_template
import iris

app = Flask(__name__)

# セッション管理のためのキーを設定
app.secret_key = 'secret_key'  

# 製品データの取得
def list_products():
    sql = "select ProductCode, ProductName, Price from product"
    # SQLステートメントの準備
    stmt = iris.sql.prepare(sql)
    # 結果セットの取得
    rset = stmt.execute()
    return rset

# 製品コードから製品データを1件取得
def get_product_by_code(product_code):
    sql = "select ID from product where ProductCode=?"
    # SQLステートメントの準備
    stmt = iris.sql.prepare(sql)
    # 結果セットの取得
    rset = stmt.execute(product_code)
    for product in rset:
        return iris.cls('User.Product')._OpenId(product[0])
    return None

# ルートページ
@app.route('/', methods=['GET'])
def meetup():
    name = "Hello MeetUp!"
    return name

# 製品詳細ページ (※このハンズオンでは文字列を表示するだけです。)
@app.route('/product/<product_code>')
def product_detail(product_code):
    contents = f"製品コード：{product_code} の製品の詳細を表示します。"
    return contents

# 製品リストを取得して表示
@app.route('/products', methods=['GET'])
def get_products():
    products = list_products()
    return render_template("products.html", products=products)

# ショッピングカートに製品を追加
@app.route('/cart/add/<product_code>', methods=['POST'])
def add_to_cart(product_code):
    # 製品コードから製品データを取得
    product = get_product_by_code(product_code)
    if product is None:
        return jsonify({'message': 'Product not found!'}), 404

    if 'cart' not in session:
        # Session内の'cart'初期化
        session['cart'] = {}
    
    # カートの当該製品の件数をインクリメント
    session['cart'][product_code] = session['cart'].get(product_code, 0) + 1
    
    # セッションの変更を通知
    session.modified = True  
    return render_template('cart_added.html', product_name=product.ProductName)

# カートの内容を表示
@app.route('/cart', methods=['GET'])
def view_cart():
    # セッションよりカート情報を取得
    cart = session.get('cart', {})

    cart_items = []
    total = 0
    for code, quantity in cart.items():
        # 製品コードより製品を取得
        product = get_product_by_code(code)
        if product is not None:
            # 表示するためのカート情報をセット
            cart_items.append({
                'ProductCode': code,
                'ProductName': product.ProductName,
                'Quantity': quantity,
                'UnitPrice': product.Price,
                'TotalPrice': product.Price * quantity
            })
            total += product.Price * quantity
    return render_template('cart.html', items=cart_items, total=total)

# 購入手続き
@app.route('/checkout', methods=['POST'])
def checkout():
    if 'cart' not in session or not session['cart']:
        return "カートの中身が空です。"

    # 取引オブジェクトを生成
    ts = iris.cls('User.Transactions')._New()    

    total = 0
    # カート内をループ
    for code, quantity in session['cart'].items():
        # 製品コードより製品データを取得
        product = get_product_by_code(code)

        if product is not None:
            # 取引明細オブジェクトの生成
            item = iris.cls('User.TransactionItem')._New()
            item.Transactions = ts
            item.Product = product
            item.UnitPrice = product.Price
            item.Quantity = quantity

            # 取引明細の登録
            item._Save()
            total += product.Price * quantity
    # 合計金額
    ts.Total = total

    # 現在時刻をセット
    ts.TransactionDateTime= iris.cls('%Library.PosixTime').CurrentTimeStamp()
    
    # 取引の登録
    ts._Save()

    # セッションよりカートをクリア
    session.pop('cart', None)

    # セッションの変更を通知
    session.modified = True  
    return render_template('checkout_success.html', total=total)

if __name__ == "__main__":
    app.run(debug=True)



