

# SearchEntityRequest

## Properties

Name | Type | Required
-------- | -------- | --------
field_id | str | optional
max_results | float | optional
next_token | str | optional
operator | [OperatorEnum](#OperatorEnum) | optional
query | object | optional
restrict_to | str | optional
term | str | optional
include_summary | bool | optional




## Enums


<a name="OperatorEnum"></a>
### OperatorEnum

Name | Value
---- | -----
EQUALS | &quot;equals&quot;
STARTSWITH | &quot;startsWith&quot;
CONTAINS | &quot;contains&quot;
ELASTICSEARCH | &quot;elasticsearch&quot;






## Inheritance hierarchy


* [SearchEntityRequest](SearchEntityRequest.md)
    * [BaseRequest](BaseRequest.md)
