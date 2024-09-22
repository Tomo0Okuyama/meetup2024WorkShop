Class User.eptest Extends %Persistent
{

Property name As %String;

ClassMethod sum(x1 As %Integer, x2 As %Integer) As %Integer
{
	quit $g(x1)+$g(x2)
}

ClassMethod init()
{
	kill ^User.eptestD
	&sql( insert into eptest (name) values ('Naka') )
	&sql( insert into eptest (name) values ('Sato') )          
	kill ^a
	set ^a=55, ^a(1)=123, ^a(1,4)=999
}

Storage Default
{
<Data name="eptestDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>name</Value>
</Value>
</Data>
<DataLocation>^User.eptestD</DataLocation>
<DefaultData>eptestDefaultData</DefaultData>
<IdLocation>^User.eptestD</IdLocation>
<IndexLocation>^User.eptestI</IndexLocation>
<StreamLocation>^User.eptestS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
