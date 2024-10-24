/// 取引明細テーブル
Class User.TransactionItem Extends %Persistent
{

/// 製品
Property Product As Product;

/// 単価
Property UnitPrice As %Numeric;

/// 個数
Property Quantity As %Numeric;

/// 取引
Relationship Transactions As Transactions [ Cardinality = parent, Inverse = Items ];

Storage Default
{
<Data name="TransactionItemDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>Product</Value>
</Value>
<Value name="3">
<Value>UnitPrice</Value>
</Value>
<Value name="4">
<Value>Quantity</Value>
</Value>
</Data>
<DataLocation>{%%PARENT}("Items")</DataLocation>
<DefaultData>TransactionItemDefaultData</DefaultData>
<IdLocation>^User.TransactionsC("Items")</IdLocation>
<IndexLocation>^User.TransactionItemI</IndexLocation>
<StreamLocation>^User.TransactionItemS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
