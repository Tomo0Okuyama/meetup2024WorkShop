/// 製品テーブル
Class User.Product Extends %Persistent
{

/// 製品番号
Property ProductCode As %String;

/// 製品名
Property ProductName As %String;

/// 価格
Property Price As %Integer;

Index ProdCode On ProductCode [ IdKey, Unique ];

Storage Default
{
<Data name="ProductDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>ProductName</Value>
</Value>
<Value name="3">
<Value>Price</Value>
</Value>
</Data>
<DataLocation>^User.ProductD</DataLocation>
<DefaultData>ProductDefaultData</DefaultData>
<IdLocation>^User.ProductD</IdLocation>
<IndexLocation>^User.ProductI</IndexLocation>
<StreamLocation>^User.ProductS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
