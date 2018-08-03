

# CreateLoginResponse

## Properties

Name | Type | Required
-------- | -------- | --------
data_root_node | str | required
status | [StatusEnum](#StatusEnum) | required
agent | [Agent](Agent.md) | optional
batch_id | str | optional
fact_type | str | optional
node_id | str | optional
parent_id | str | optional
summary | [Summary](Summary.md) | optional
timestamp | float | optional




## Enums


<a name="StatusEnum"></a>
### StatusEnum

Name | Value
---- | -----
PENDING_CONFIRMATION | &quot;PENDING_CONFIRMATION&quot;
FAILED_TO_SEND_EMAIL | &quot;FAILED_TO_SEND_EMAIL&quot;






## Inheritance hierarchy


* [CreateLoginResponse](CreateLoginResponse.md)
    * [BaseResponse](BaseResponse.md)
