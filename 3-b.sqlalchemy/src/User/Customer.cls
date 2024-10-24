/// 顧客テーブル
Class User.Customer Extends %Persistent
{

/// 顧客ID
Property CustomerId As %String;

/// 氏名姓
Property LastName As %String;

/// 氏名名
Property FirstName As %String;

/// カナ性
Property LastNameKana As %String;

/// カナ名
Property FirstNameKana As %String;

/// 誕生日 
Property DOB As %Date;

/// 性別
Property Gender As %String;

/// 郵便番号
Property ZipCode As %String;

/// 住所
Property Address As %String(MAXLEN = 1000);

/// 電話番号
Property Phone As %String;

Index CustIdIdx On CustomerId [ IdKey, Unique ];

Storage Default
{
<Data name="CustomerDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>LastName</Value>
</Value>
<Value name="3">
<Value>FirstName</Value>
</Value>
<Value name="4">
<Value>LastNameKana</Value>
</Value>
<Value name="5">
<Value>FirstNameKana</Value>
</Value>
<Value name="6">
<Value>DOB</Value>
</Value>
<Value name="7">
<Value>Gender</Value>
</Value>
<Value name="8">
<Value>ZipCode</Value>
</Value>
<Value name="9">
<Value>Address</Value>
</Value>
<Value name="10">
<Value>Phone</Value>
</Value>
</Data>
<DataLocation>^User.CustomerD</DataLocation>
<DefaultData>CustomerDefaultData</DefaultData>
<IdLocation>^User.CustomerD</IdLocation>
<IndexLocation>^User.CustomerI</IndexLocation>
<StreamLocation>^User.CustomerS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
