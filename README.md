# @factern/factern-client
[![Build Status](https://travis-ci.org/Factern/factern-client-python.svg?branch=master)](https://travis-ci.org/Factern/factern-client-python)

## Python Client for Factern API v2

- API version: 2.0.0
- Package version: 1.0.6

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

The python package is hosted on pypi, you can install directly from command line

```sh
pip install factern_client
```
(you may need to run `pip` with root permission: `sudo pip install factern_client`)

Then import the package:
```python
import factern_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import factern_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import factern_client
from factern_client.rest import ApiException

configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))

try:
    api_response = api_instance.create_entity(login="Your login ID", representing="Your representing ID", body=factern_client.CreateEntityRequest())
    print("Node ID: %s" % api_response.node_id)
except ApiException as e:
    print("Exception when calling createentity: %s" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.factern.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FactsApi* | [**add_member**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#add_member) | **POST** /createmember | Create Member
*FactsApi* | [**bid**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#bid) | **POST** /createbid | Create Bid
*FactsApi* | [**create_alias**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_alias) | **POST** /createalias | Create Alias
*FactsApi* | [**create_application**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_application) | **POST** /createapplication | Create Application
*FactsApi* | [**create_domain**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_domain) | **POST** /createdomain | Create Domain
*FactsApi* | [**create_entity**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_entity) | **POST** /createentity | Create Entity
*FactsApi* | [**create_field**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_field) | **POST** /createfield | Create Field
*FactsApi* | [**create_filter**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_filter) | **POST** /createfilter | Create Filter
*FactsApi* | [**create_group**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_group) | **POST** /creategroup | Create Group
*FactsApi* | [**create_information**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_information) | **POST** /createinformation | Create Information
*FactsApi* | [**create_interface**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_interface) | **POST** /createinterface | Create Interface
*FactsApi* | [**create_label_list**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_label_list) | **POST** /createlabellist | Create Label List
*FactsApi* | [**create_login**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_login) | **POST** /createlogin | Create Login
*FactsApi* | [**create_mirror**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_mirror) | **POST** /createmirror | Create Mirror
*FactsApi* | [**create_price**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_price) | **POST** /createprice | Create Price
*FactsApi* | [**create_scope**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_scope) | **POST** /createscope | Create Scope
*FactsApi* | [**create_statement**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_statement) | **POST** /createstatement | Create Statement
*FactsApi* | [**create_template**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#create_template) | **POST** /createtemplate | Create Template
*FactsApi* | [**delete**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#delete) | **POST** /delete | Deleting
*FactsApi* | [**delete_node**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#delete_node) | **POST** /deletenode | Delete Node
*FactsApi* | [**describe**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#describe) | **POST** /describe | Describe
*FactsApi* | [**history**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#history) | **POST** /history | History
*FactsApi* | [**label**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#label) | **POST** /label | Label a Node
*FactsApi* | [**obliterate**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#obliterate) | **POST** /obliterate | Obliterating Information Nodes
*FactsApi* | [**permission**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#permission) | **POST** /permission | Create Permission
*FactsApi* | [**read**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#read) | **POST** /read | Reading
*FactsApi* | [**read_information**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#read_information) | **POST** /readinformation | Read Information
*FactsApi* | [**replace_information**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#replace_information) | **POST** /replaceinformation | Replace
*FactsApi* | [**request_permission**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#request_permission) | **POST** /requestpermission | Request Permission
*FactsApi* | [**reset_login**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#reset_login) | **POST** /resetlogin | Changing Login Password
*FactsApi* | [**search_alias**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#search_alias) | **POST** /searchalias | Search For Alias
*FactsApi* | [**search_entity**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#search_entity) | **POST** /searchentity | Search For Entity
*FactsApi* | [**settle_account**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#settle_account) | **POST** /settleaccount | Settle Account
*FactsApi* | [**update_application**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#update_application) | **POST** /updateapplication | Resetting Application Secret
*FactsApi* | [**update_status**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#update_status) | **POST** /updatestatus | Enabling/Disabling Nodes
*FactsApi* | [**updateinterface**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#updateinterface) | **POST** /updateinterface | Updating interface endpoints
*FactsApi* | [**watch**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#watch) | **POST** /watch | Create Watch Trigger
*FactsApi* | [**write**](https://github.com/Factern/factern-client-python/blob/master/docs/FactsApi.md#write) | **POST** /write | Writing by Template


## Documentation For Models

 - [Account](https://github.com/Factern/factern-client-javascript/blob/master/docs/Account.md)
 - [AddLabelRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/AddLabelRequest.md)
 - [AddLabelResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/AddLabelResponse.md)
 - [AddStatementRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/AddStatementRequest.md)
 - [AddStatementResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/AddStatementResponse.md)
 - [Agent](https://github.com/Factern/factern-client-javascript/blob/master/docs/Agent.md)
 - [Alias](https://github.com/Factern/factern-client-javascript/blob/master/docs/Alias.md)
 - [AliasNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/AliasNode.md)
 - [ApiEndpoint](https://github.com/Factern/factern-client-javascript/blob/master/docs/ApiEndpoint.md)
 - [Application](https://github.com/Factern/factern-client-javascript/blob/master/docs/Application.md)
 - [ApplicationNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/ApplicationNode.md)
 - [BaseRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/BaseRequest.md)
 - [BaseResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/BaseResponse.md)
 - [Bid](https://github.com/Factern/factern-client-javascript/blob/master/docs/Bid.md)
 - [BidNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/BidNode.md)
 - [Cost](https://github.com/Factern/factern-client-javascript/blob/master/docs/Cost.md)
 - [CreateAliasRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateAliasRequest.md)
 - [CreateAliasResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateAliasResponse.md)
 - [CreateApplicationRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateApplicationRequest.md)
 - [CreateApplicationResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateApplicationResponse.md)
 - [CreateBidRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateBidRequest.md)
 - [CreateBidResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateBidResponse.md)
 - [CreateChildRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateChildRequest.md)
 - [CreateDomainRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateDomainRequest.md)
 - [CreateDomainResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateDomainResponse.md)
 - [CreateEntityRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateEntityRequest.md)
 - [CreateEntityResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateEntityResponse.md)
 - [CreateFieldRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateFieldRequest.md)
 - [CreateFieldResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateFieldResponse.md)
 - [CreateFilterRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateFilterRequest.md)
 - [CreateFilterResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateFilterResponse.md)
 - [CreateGroupRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateGroupRequest.md)
 - [CreateGroupResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateGroupResponse.md)
 - [CreateInformationRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateInformationRequest.md)
 - [CreateInformationResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateInformationResponse.md)
 - [CreateInterfaceRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateInterfaceRequest.md)
 - [CreateInterfaceResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateInterfaceResponse.md)
 - [CreateLabelListRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateLabelListRequest.md)
 - [CreateLabelListResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateLabelListResponse.md)
 - [CreateLoginRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateLoginRequest.md)
 - [CreateLoginResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateLoginResponse.md)
 - [CreateMemberRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateMemberRequest.md)
 - [CreateMemberResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateMemberResponse.md)
 - [CreateMirrorRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateMirrorRequest.md)
 - [CreateMirrorResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateMirrorResponse.md)
 - [CreateNamedRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateNamedRequest.md)
 - [CreatePermissionRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreatePermissionRequest.md)
 - [CreatePermissionResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreatePermissionResponse.md)
 - [CreatePriceRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreatePriceRequest.md)
 - [CreatePriceResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreatePriceResponse.md)
 - [CreateScopeRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateScopeRequest.md)
 - [CreateScopeResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateScopeResponse.md)
 - [CreateTemplateRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateTemplateRequest.md)
 - [CreateTemplateResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateTemplateResponse.md)
 - [CreateWatchRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateWatchRequest.md)
 - [CreateWatchResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/CreateWatchResponse.md)
 - [DeleteRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/DeleteRequest.md)
 - [DeleteResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/DeleteResponse.md)
 - [DeletedItem](https://github.com/Factern/factern-client-javascript/blob/master/docs/DeletedItem.md)
 - [DeletedStatusItem](https://github.com/Factern/factern-client-javascript/blob/master/docs/DeletedStatusItem.md)
 - [DescribeRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/DescribeRequest.md)
 - [DescribeResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/DescribeResponse.md)
 - [Domain](https://github.com/Factern/factern-client-javascript/blob/master/docs/Domain.md)
 - [DomainNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/DomainNode.md)
 - [Entity](https://github.com/Factern/factern-client-javascript/blob/master/docs/Entity.md)
 - [EntityListResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/EntityListResponse.md)
 - [EntityNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/EntityNode.md)
 - [ExternalDataUsage](https://github.com/Factern/factern-client-javascript/blob/master/docs/ExternalDataUsage.md)
 - [FactCount](https://github.com/Factern/factern-client-javascript/blob/master/docs/FactCount.md)
 - [Field](https://github.com/Factern/factern-client-javascript/blob/master/docs/Field.md)
 - [FieldNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/FieldNode.md)
 - [FieldStoreValues](https://github.com/Factern/factern-client-javascript/blob/master/docs/FieldStoreValues.md)
 - [Filter](https://github.com/Factern/factern-client-javascript/blob/master/docs/Filter.md)
 - [FilterNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/FilterNode.md)
 - [FilterStatement](https://github.com/Factern/factern-client-javascript/blob/master/docs/FilterStatement.md)
 - [GasCost](https://github.com/Factern/factern-client-javascript/blob/master/docs/GasCost.md)
 - [Group](https://github.com/Factern/factern-client-javascript/blob/master/docs/Group.md)
 - [GroupNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/GroupNode.md)
 - [HttpHeader](https://github.com/Factern/factern-client-javascript/blob/master/docs/HttpHeader.md)
 - [Information](https://github.com/Factern/factern-client-javascript/blob/master/docs/Information.md)
 - [InformationListResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/InformationListResponse.md)
 - [InformationNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/InformationNode.md)
 - [Interface](https://github.com/Factern/factern-client-javascript/blob/master/docs/Interface.md)
 - [InterfaceNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/InterfaceNode.md)
 - [Label](https://github.com/Factern/factern-client-javascript/blob/master/docs/Label.md)
 - [LabelList](https://github.com/Factern/factern-client-javascript/blob/master/docs/LabelList.md)
 - [LabelListMember](https://github.com/Factern/factern-client-javascript/blob/master/docs/LabelListMember.md)
 - [LabelListMemberNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/LabelListMemberNode.md)
 - [LabelListNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/LabelListNode.md)
 - [LabelStatement](https://github.com/Factern/factern-client-javascript/blob/master/docs/LabelStatement.md)
 - [ListCriteria](https://github.com/Factern/factern-client-javascript/blob/master/docs/ListCriteria.md)
 - [Login](https://github.com/Factern/factern-client-javascript/blob/master/docs/Login.md)
 - [LoginNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/LoginNode.md)
 - [Member](https://github.com/Factern/factern-client-javascript/blob/master/docs/Member.md)
 - [MemberNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/MemberNode.md)
 - [Mirror](https://github.com/Factern/factern-client-javascript/blob/master/docs/Mirror.md)
 - [MirrorNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/MirrorNode.md)
 - [NamedNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/NamedNode.md)
 - [NodeIdRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/NodeIdRequest.md)
 - [NodeListing](https://github.com/Factern/factern-client-javascript/blob/master/docs/NodeListing.md)
 - [Permission](https://github.com/Factern/factern-client-javascript/blob/master/docs/Permission.md)
 - [PermissionAction](https://github.com/Factern/factern-client-javascript/blob/master/docs/PermissionAction.md)
 - [PermissionEffect](https://github.com/Factern/factern-client-javascript/blob/master/docs/PermissionEffect.md)
 - [PermissionNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/PermissionNode.md)
 - [PermissionPolicyDocument](https://github.com/Factern/factern-client-javascript/blob/master/docs/PermissionPolicyDocument.md)
 - [Price](https://github.com/Factern/factern-client-javascript/blob/master/docs/Price.md)
 - [PriceDetails](https://github.com/Factern/factern-client-javascript/blob/master/docs/PriceDetails.md)
 - [PriceNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/PriceNode.md)
 - [ReadInformationRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/ReadInformationRequest.md)
 - [ReadInformationResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/ReadInformationResponse.md)
 - [ReadItem](https://github.com/Factern/factern-client-javascript/blob/master/docs/ReadItem.md)
 - [ReadRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/ReadRequest.md)
 - [ReadResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/ReadResponse.md)
 - [ReadStatusItem](https://github.com/Factern/factern-client-javascript/blob/master/docs/ReadStatusItem.md)
 - [ReplaceFieldRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/ReplaceFieldRequest.md)
 - [ResetLoginCredentialsRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/ResetLoginCredentialsRequest.md)
 - [ResetLoginResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/ResetLoginResponse.md)
 - [Scope](https://github.com/Factern/factern-client-javascript/blob/master/docs/Scope.md)
 - [ScopeNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/ScopeNode.md)
 - [SearchAliasRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/SearchAliasRequest.md)
 - [SearchAliasResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/SearchAliasResponse.md)
 - [SearchEntityRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/SearchEntityRequest.md)
 - [Searches](https://github.com/Factern/factern-client-javascript/blob/master/docs/Searches.md)
 - [SettleAccountRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/SettleAccountRequest.md)
 - [SettleAccountResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/SettleAccountResponse.md)
 - [StandardNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/StandardNode.md)
 - [StandardNodeResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/StandardNodeResponse.md)
 - [Statement](https://github.com/Factern/factern-client-javascript/blob/master/docs/Statement.md)
 - [StatementStatement](https://github.com/Factern/factern-client-javascript/blob/master/docs/StatementStatement.md)
 - [Summary](https://github.com/Factern/factern-client-javascript/blob/master/docs/Summary.md)
 - [Template](https://github.com/Factern/factern-client-javascript/blob/master/docs/Template.md)
 - [TemplateNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/TemplateNode.md)
 - [TokenPayment](https://github.com/Factern/factern-client-javascript/blob/master/docs/TokenPayment.md)
 - [TransformElement](https://github.com/Factern/factern-client-javascript/blob/master/docs/TransformElement.md)
 - [UpdateApplicationRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/UpdateApplicationRequest.md)
 - [UpdateApplicationResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/UpdateApplicationResponse.md)
 - [UpdateInterfaceRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/UpdateInterfaceRequest.md)
 - [UpdateStatusRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/UpdateStatusRequest.md)
 - [Watch](https://github.com/Factern/factern-client-javascript/blob/master/docs/Watch.md)
 - [WatchEvent](https://github.com/Factern/factern-client-javascript/blob/master/docs/WatchEvent.md)
 - [WatchEventNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/WatchEventNode.md)
 - [WatchNode](https://github.com/Factern/factern-client-javascript/blob/master/docs/WatchNode.md)
 - [WriteItem](https://github.com/Factern/factern-client-javascript/blob/master/docs/WriteItem.md)
 - [WriteRequest](https://github.com/Factern/factern-client-javascript/blob/master/docs/WriteRequest.md)
 - [WriteResponse](https://github.com/Factern/factern-client-javascript/blob/master/docs/WriteResponse.md)


## Authentication

To generate an OAuth2 token, see [the user's guide](http://docs.factern.net/users-guide/#acquiring-an-access-token).

## Author

Factern Ltd.
mailto:support@factern.com

