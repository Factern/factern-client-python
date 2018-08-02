

# ListCriteria

## Properties

Name | Type | Required
-------- | -------- | --------
action_id | str | optional
fact_type | [Fact_typeEnum](#Fact_typeEnum) | optional
field_id | str | optional
include_deleted | bool | optional
label_list_id | str | optional
label_list_name | str | optional
max_results | float | optional
next_token | str | optional
starting_from_timestamp | float | optional
type_name | str | optional




## Enums


<a name="Fact_typeEnum"></a>
### Fact_typeEnum

Name | Value
---- | -----
ENTITY | &quot;Entity&quot;
LOGIN | &quot;Login&quot;
APPLICATION | &quot;Application&quot;
FIELD | &quot;Field&quot;
INFORMATION | &quot;Information&quot;
PERMISSION | &quot;Permission&quot;
WATCH | &quot;Watch&quot;
WATCHEVENT | &quot;WatchEvent&quot;
GROUP | &quot;Group&quot;
INTERFACE | &quot;Interface&quot;
LABELLIST | &quot;LabelList&quot;
LABEL | &quot;Label&quot;
TEMPLATE | &quot;Template&quot;
SCOPE | &quot;Scope&quot;






## Inheritance hierarchy


* [ListCriteria](ListCriteria.md)
