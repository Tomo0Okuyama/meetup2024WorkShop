from sqlalchemy import Column, Integer, String, Date, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from setting import Base
import datetime

# モデルクラス

# 顧客情報
class Customer(Base):
    __tablename__ = 'Customer'
    customerId = Column('CustomerId', Integer, primary_key=True, index=True, autoincrement= False)
    firstName = Column('FirstName', String)
    lastName = Column('LastName', String)
    firstNameKana = Column('FirstNameKana', String)
    lastNameKana = Column('LastNameKana', String)
    dob = Column('DOB',Date)
    gender = Column('Gender',String)
    zipCode = Column('ZipCode',String)
    address = Column('Address', String)
    phone = Column('Phone',String)

# 製品情報
class Product(Base):
    __tablename__ = 'Product'
    productCode = Column('ProductCode', String, primary_key=True, index=True)
    productName = Column('ProductName', String)
    price = Column('Price', Integer)

# 取引明細データ
class TransactionItem(Base):
    __tablename__ = 'TransactionItem'
    transaction_id = Column('Transactions',Integer, ForeignKey("Transactions.ID"), primary_key=True, autoincrement=False)
    id = Column('childsub', Integer, primary_key=True, autoincrement=True)
    transaction = relationship('Transactions', foreign_keys=[transaction_id], back_populates="items")

    product_id = Column('Product', String, ForeignKey('Product.ProductCode'))
    product = relationship('Product',foreign_keys=[product_id])

    unitPrice = Column('UnitPrice', String)
    quantity = Column('Quantity', String)

# 取引データ
class Transactions(Base):
    __tablename__ = 'Transactions'
    id = Column('ID', Integer, primary_key=True, index=True)
    items = relationship('TransactionItem', back_populates="transaction", cascade="all,delete")

    customer_id = Column('Customer', String, ForeignKey('Customer.CustomerId'))
    customer = relationship('Customer',foreign_keys=[customer_id])

    dateTime = Column('TransactionDateTime', DateTime, default=datetime.datetime.now())
    total = Column('Total',Integer)
