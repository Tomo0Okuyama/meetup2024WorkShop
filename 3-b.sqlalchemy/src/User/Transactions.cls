/// 取引テーブル
Class User.Transactions Extends %Persistent
{

/// 取引時刻
Property TransactionDateTime As %PosixTime;

/// 顧客
Property Customer As Customer;

/// 合計金額
Property Total As %Numeric;

/// 取引明細
Relationship Items As TransactionItem [ Cardinality = children, Inverse = Transactions ];

Storage Default
{
<Data name="TransactionsDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>TransactionDateTime</Value>
</Value>
<Value name="3">
<Value>Customer</Value>
</Value>
<Value name="4">
<Value>Total</Value>
</Value>
</Data>
<DataLocation>^User.TransactionsD</DataLocation>
<DefaultData>TransactionsDefaultData</DefaultData>
<IdLocation>^User.TransactionsD</IdLocation>
<IndexLocation>^User.TransactionsI</IndexLocation>
<StreamLocation>^User.TransactionsS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
