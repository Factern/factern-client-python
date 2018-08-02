

# ApiEndpoint

## Properties

Name | Type | Required
-------- | -------- | --------
body | str | optional
headers | [list[HttpHeader]](HttpHeader.md) | optional
method | [MethodEnum](#MethodEnum) | optional
response_transform | [list[TransformElement]](TransformElement.md) | optional
type | [TypeEnum](#TypeEnum) | optional
url | str | required




## Enums


<a name="MethodEnum"></a>
### MethodEnum

Name | Value
---- | -----
GET | &quot;GET&quot;
POST | &quot;POST&quot;
PUT | &quot;PUT&quot;



<a name="TypeEnum"></a>
### TypeEnum

Name | Value
---- | -----
DIRECT | &quot;Direct&quot;
INDIRECT | &quot;Indirect&quot;






## Inheritance hierarchy


* [ApiEndpoint](ApiEndpoint.md)
