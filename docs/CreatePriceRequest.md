

# CreatePriceRequest

## Properties

Name | Type | Required
-------- | -------- | --------
policy | [PermissionPolicyDocument](PermissionPolicyDocument.md) | required
price_details | [PriceDetails](PriceDetails.md) | required
target_node_id | str | required
type | [TypeEnum](#TypeEnum) | required
include_summary | bool | optional




## Enums


<a name="TypeEnum"></a>
### TypeEnum

Name | Value
---- | -----
FIXED | &quot;Fixed&quot;






## Inheritance hierarchy


* [CreatePriceRequest](CreatePriceRequest.md)
    * [BaseRequest](BaseRequest.md)
