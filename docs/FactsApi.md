
# factern_client.FactsApi

All URIs are relative to *https://api.factern.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member**](FactsApi.md#add_member) | **POST** /createmember | Create Member
[**bid**](FactsApi.md#bid) | **POST** /createbid | Create Bid
[**create_alias**](FactsApi.md#create_alias) | **POST** /createalias | Create Alias
[**create_application**](FactsApi.md#create_application) | **POST** /createapplication | Create Application
[**create_domain**](FactsApi.md#create_domain) | **POST** /createdomain | Create Domain
[**create_entity**](FactsApi.md#create_entity) | **POST** /createentity | Create Entity
[**create_field**](FactsApi.md#create_field) | **POST** /createfield | Create Field
[**create_filter**](FactsApi.md#create_filter) | **POST** /createfilter | Create Filter
[**create_group**](FactsApi.md#create_group) | **POST** /creategroup | Create Group
[**create_information**](FactsApi.md#create_information) | **POST** /createinformation | Create Information
[**create_interface**](FactsApi.md#create_interface) | **POST** /createinterface | Create Interface
[**create_label_list**](FactsApi.md#create_label_list) | **POST** /createlabellist | Create Label List
[**create_login**](FactsApi.md#create_login) | **POST** /createlogin | Create Login
[**create_mirror**](FactsApi.md#create_mirror) | **POST** /createmirror | Create Mirror
[**create_price**](FactsApi.md#create_price) | **POST** /createprice | Create Price
[**create_scope**](FactsApi.md#create_scope) | **POST** /createscope | Create Scope
[**create_statement**](FactsApi.md#create_statement) | **POST** /createstatement | Create Statement
[**create_template**](FactsApi.md#create_template) | **POST** /createtemplate | Create Template
[**delete**](FactsApi.md#delete) | **POST** /delete | Deleting
[**delete_node**](FactsApi.md#delete_node) | **POST** /deletenode | Delete Node
[**describe**](FactsApi.md#describe) | **POST** /describe | Describe
[**history**](FactsApi.md#history) | **POST** /history | History
[**label**](FactsApi.md#label) | **POST** /label | Label a Node
[**obliterate**](FactsApi.md#obliterate) | **POST** /obliterate | Obliterating Information Nodes
[**permission**](FactsApi.md#permission) | **POST** /permission | Create Permission
[**read**](FactsApi.md#read) | **POST** /read | Reading
[**read_information**](FactsApi.md#read_information) | **POST** /readinformation | Read Information
[**replace_information**](FactsApi.md#replace_information) | **POST** /replaceinformation | Replace
[**request_permission**](FactsApi.md#request_permission) | **POST** /requestpermission | Request Permission
[**reset_login**](FactsApi.md#reset_login) | **POST** /resetlogin | Changing Login Password
[**search_alias**](FactsApi.md#search_alias) | **POST** /searchalias | Search For Alias
[**search_entity**](FactsApi.md#search_entity) | **POST** /searchentity | Search For Entity
[**settle_account**](FactsApi.md#settle_account) | **POST** /settleaccount | Settle Account
[**update_application**](FactsApi.md#update_application) | **POST** /updateapplication | Resetting Application Secret
[**update_status**](FactsApi.md#update_status) | **POST** /updatestatus | Enabling/Disabling Nodes
[**watch**](FactsApi.md#watch) | **POST** /watch | Create Watch Trigger
[**write**](FactsApi.md#write) | **POST** /write | Writing by Template


# **add_member**
> CreateMemberResponse add_member(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_member_request = factern_client.CreateMemberRequest() # CreateMemberRequest |  (optional)

try:
    # Create Member
    api_response = api_instance.add_member(login=login, representing=representing, create_member_request=create_member_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_member_request** | [**CreateMemberRequest**](CreateMemberRequest.md)|  | [optional] 

### Return type

[**CreateMemberResponse**](CreateMemberResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bid**
> StandardNodeResponse bid(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_bid_request = factern_client.CreateBidRequest() # CreateBidRequest |  (optional)

try:
    # Create Bid
    api_response = api_instance.bid(login=login, representing=representing, create_bid_request=create_bid_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_bid_request** | [**CreateBidRequest**](CreateBidRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alias**
> CreateAliasResponse create_alias(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_alias_request = factern_client.CreateAliasRequest() # CreateAliasRequest |  (optional)

try:
    # Create Alias
    api_response = api_instance.create_alias(login=login, representing=representing, create_alias_request=create_alias_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_alias_request** | [**CreateAliasRequest**](CreateAliasRequest.md)|  | [optional] 

### Return type

[**CreateAliasResponse**](CreateAliasResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> CreateApplicationResponse create_application(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_application_request = factern_client.CreateApplicationRequest() # CreateApplicationRequest |  (optional)

try:
    # Create Application
    api_response = api_instance.create_application(login=login, representing=representing, create_application_request=create_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_application_request** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain**
> CreateDomainResponse create_domain(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_domain_request = factern_client.CreateDomainRequest() # CreateDomainRequest |  (optional)

try:
    # Create Domain
    api_response = api_instance.create_domain(login=login, representing=representing, create_domain_request=create_domain_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_domain_request** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | [optional] 

### Return type

[**CreateDomainResponse**](CreateDomainResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> CreateEntityResponse create_entity(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_entity_request = factern_client.CreateEntityRequest() # CreateEntityRequest |  (optional)

try:
    # Create Entity
    api_response = api_instance.create_entity(login=login, representing=representing, create_entity_request=create_entity_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_entity_request** | [**CreateEntityRequest**](CreateEntityRequest.md)|  | [optional] 

### Return type

[**CreateEntityResponse**](CreateEntityResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_field**
> CreateFieldResponse create_field(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_field_request = factern_client.CreateFieldRequest() # CreateFieldRequest |  (optional)

try:
    # Create Field
    api_response = api_instance.create_field(login=login, representing=representing, create_field_request=create_field_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_field_request** | [**CreateFieldRequest**](CreateFieldRequest.md)|  | [optional] 

### Return type

[**CreateFieldResponse**](CreateFieldResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_filter**
> CreateFilterResponse create_filter(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_filter_request = factern_client.CreateFilterRequest() # CreateFilterRequest |  (optional)

try:
    # Create Filter
    api_response = api_instance.create_filter(login=login, representing=representing, create_filter_request=create_filter_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_filter_request** | [**CreateFilterRequest**](CreateFilterRequest.md)|  | [optional] 

### Return type

[**CreateFilterResponse**](CreateFilterResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> CreateGroupResponse create_group(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_group_request = factern_client.CreateGroupRequest() # CreateGroupRequest |  (optional)

try:
    # Create Group
    api_response = api_instance.create_group(login=login, representing=representing, create_group_request=create_group_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_group_request** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | [optional] 

### Return type

[**CreateGroupResponse**](CreateGroupResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_information**
> CreateInformationResponse create_information(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_information_request = factern_client.CreateInformationRequest() # CreateInformationRequest |  (optional)

try:
    # Create Information
    api_response = api_instance.create_information(login=login, representing=representing, create_information_request=create_information_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_information_request** | [**CreateInformationRequest**](CreateInformationRequest.md)|  | [optional] 

### Return type

[**CreateInformationResponse**](CreateInformationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interface**
> CreateInterfaceResponse create_interface(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_interface_request = factern_client.CreateInterfaceRequest() # CreateInterfaceRequest |  (optional)

try:
    # Create Interface
    api_response = api_instance.create_interface(login=login, representing=representing, create_interface_request=create_interface_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_interface_request** | [**CreateInterfaceRequest**](CreateInterfaceRequest.md)|  | [optional] 

### Return type

[**CreateInterfaceResponse**](CreateInterfaceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_label_list**
> CreateLabelListResponse create_label_list(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_label_list_request = factern_client.CreateLabelListRequest() # CreateLabelListRequest |  (optional)

try:
    # Create Label List
    api_response = api_instance.create_label_list(login=login, representing=representing, create_label_list_request=create_label_list_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_label_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_label_list_request** | [**CreateLabelListRequest**](CreateLabelListRequest.md)|  | [optional] 

### Return type

[**CreateLabelListResponse**](CreateLabelListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_login**
> CreateLoginResponse create_login(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_login_request = factern_client.CreateLoginRequest() # CreateLoginRequest |  (optional)

try:
    # Create Login
    api_response = api_instance.create_login(login=login, representing=representing, create_login_request=create_login_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_login_request** | [**CreateLoginRequest**](CreateLoginRequest.md)|  | [optional] 

### Return type

[**CreateLoginResponse**](CreateLoginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mirror**
> CreateMirrorResponse create_mirror(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_mirror_request = factern_client.CreateMirrorRequest() # CreateMirrorRequest |  (optional)

try:
    # Create Mirror
    api_response = api_instance.create_mirror(login=login, representing=representing, create_mirror_request=create_mirror_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_mirror: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_mirror_request** | [**CreateMirrorRequest**](CreateMirrorRequest.md)|  | [optional] 

### Return type

[**CreateMirrorResponse**](CreateMirrorResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price**
> CreatePriceResponse create_price(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_price_request = factern_client.CreatePriceRequest() # CreatePriceRequest |  (optional)

try:
    # Create Price
    api_response = api_instance.create_price(login=login, representing=representing, create_price_request=create_price_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_price_request** | [**CreatePriceRequest**](CreatePriceRequest.md)|  | [optional] 

### Return type

[**CreatePriceResponse**](CreatePriceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scope**
> CreateScopeResponse create_scope(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_scope_request = factern_client.CreateScopeRequest() # CreateScopeRequest |  (optional)

try:
    # Create Scope
    api_response = api_instance.create_scope(login=login, representing=representing, create_scope_request=create_scope_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_scope_request** | [**CreateScopeRequest**](CreateScopeRequest.md)|  | [optional] 

### Return type

[**CreateScopeResponse**](CreateScopeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_statement**
> AddStatementResponse create_statement(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
add_statement_request = factern_client.AddStatementRequest() # AddStatementRequest |  (optional)

try:
    # Create Statement
    api_response = api_instance.create_statement(login=login, representing=representing, add_statement_request=add_statement_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **add_statement_request** | [**AddStatementRequest**](AddStatementRequest.md)|  | [optional] 

### Return type

[**AddStatementResponse**](AddStatementResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> CreateTemplateResponse create_template(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_template_request = factern_client.CreateTemplateRequest() # CreateTemplateRequest |  (optional)

try:
    # Create Template
    api_response = api_instance.create_template(login=login, representing=representing, create_template_request=create_template_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_template_request** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | [optional] 

### Return type

[**CreateTemplateResponse**](CreateTemplateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> DeleteResponse delete(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
delete_request = factern_client.DeleteRequest() # DeleteRequest |  (optional)

try:
    # Deleting
    api_response = api_instance.delete(login=login, representing=representing, delete_request=delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **delete_request** | [**DeleteRequest**](DeleteRequest.md)|  | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> StandardNodeResponse delete_node(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
node_id_request = factern_client.NodeIdRequest() # NodeIdRequest |  (optional)

try:
    # Delete Node
    api_response = api_instance.delete_node(login=login, representing=representing, node_id_request=node_id_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->delete_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **node_id_request** | [**NodeIdRequest**](NodeIdRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe**
> DescribeResponse describe(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
describe_request = factern_client.DescribeRequest() # DescribeRequest |  (optional)

try:
    # Describe
    api_response = api_instance.describe(login=login, representing=representing, describe_request=describe_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->describe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **describe_request** | [**DescribeRequest**](DescribeRequest.md)|  | [optional] 

### Return type

[**DescribeResponse**](DescribeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history**
> NodeListing history(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
node_id_request = factern_client.NodeIdRequest() # NodeIdRequest |  (optional)

try:
    # History
    api_response = api_instance.history(login=login, representing=representing, node_id_request=node_id_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **node_id_request** | [**NodeIdRequest**](NodeIdRequest.md)|  | [optional] 

### Return type

[**NodeListing**](NodeListing.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label**
> AddLabelResponse label(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
add_label_request = factern_client.AddLabelRequest() # AddLabelRequest |  (optional)

try:
    # Label a Node
    api_response = api_instance.label(login=login, representing=representing, add_label_request=add_label_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **add_label_request** | [**AddLabelRequest**](AddLabelRequest.md)|  | [optional] 

### Return type

[**AddLabelResponse**](AddLabelResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obliterate**
> StandardNodeResponse obliterate(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
node_id_request = factern_client.NodeIdRequest() # NodeIdRequest |  (optional)

try:
    # Obliterating Information Nodes
    api_response = api_instance.obliterate(login=login, representing=representing, node_id_request=node_id_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->obliterate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **node_id_request** | [**NodeIdRequest**](NodeIdRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission**
> CreatePermissionResponse permission(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_permission_request = factern_client.CreatePermissionRequest() # CreatePermissionRequest |  (optional)

try:
    # Create Permission
    api_response = api_instance.permission(login=login, representing=representing, create_permission_request=create_permission_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_permission_request** | [**CreatePermissionRequest**](CreatePermissionRequest.md)|  | [optional] 

### Return type

[**CreatePermissionResponse**](CreatePermissionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> ReadResponse read(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
read_request = factern_client.ReadRequest() # ReadRequest |  (optional)

try:
    # Reading
    api_response = api_instance.read(login=login, representing=representing, read_request=read_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **read_request** | [**ReadRequest**](ReadRequest.md)|  | [optional] 

### Return type

[**ReadResponse**](ReadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_information**
> ReadInformationResponse read_information(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
read_information_request = factern_client.ReadInformationRequest() # ReadInformationRequest |  (optional)

try:
    # Read Information
    api_response = api_instance.read_information(login=login, representing=representing, read_information_request=read_information_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->read_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **read_information_request** | [**ReadInformationRequest**](ReadInformationRequest.md)|  | [optional] 

### Return type

[**ReadInformationResponse**](ReadInformationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_information**
> Information replace_information(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
replace_field_request = factern_client.ReplaceFieldRequest() # ReplaceFieldRequest |  (optional)

try:
    # Replace
    api_response = api_instance.replace_information(login=login, representing=representing, replace_field_request=replace_field_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->replace_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **replace_field_request** | [**ReplaceFieldRequest**](ReplaceFieldRequest.md)|  | [optional] 

### Return type

[**Information**](Information.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_permission**
> StandardNodeResponse request_permission(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
node_id_request = factern_client.NodeIdRequest() # NodeIdRequest |  (optional)

try:
    # Request Permission
    api_response = api_instance.request_permission(login=login, representing=representing, node_id_request=node_id_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->request_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **node_id_request** | [**NodeIdRequest**](NodeIdRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_login**
> ResetLoginResponse reset_login(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
reset_login_credentials_request = factern_client.ResetLoginCredentialsRequest() # ResetLoginCredentialsRequest |  (optional)

try:
    # Changing Login Password
    api_response = api_instance.reset_login(login=login, representing=representing, reset_login_credentials_request=reset_login_credentials_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->reset_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **reset_login_credentials_request** | [**ResetLoginCredentialsRequest**](ResetLoginCredentialsRequest.md)|  | [optional] 

### Return type

[**ResetLoginResponse**](ResetLoginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alias**
> SearchAliasResponse search_alias(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
search_alias_request = factern_client.SearchAliasRequest() # SearchAliasRequest |  (optional)

try:
    # Search For Alias
    api_response = api_instance.search_alias(login=login, representing=representing, search_alias_request=search_alias_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->search_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **search_alias_request** | [**SearchAliasRequest**](SearchAliasRequest.md)|  | [optional] 

### Return type

[**SearchAliasResponse**](SearchAliasResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entity**
> EntityListResponse search_entity(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
search_entity_request = factern_client.SearchEntityRequest() # SearchEntityRequest |  (optional)

try:
    # Search For Entity
    api_response = api_instance.search_entity(login=login, representing=representing, search_entity_request=search_entity_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->search_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **search_entity_request** | [**SearchEntityRequest**](SearchEntityRequest.md)|  | [optional] 

### Return type

[**EntityListResponse**](EntityListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_account**
> SettleAccountResponse settle_account(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
settle_account_request = factern_client.SettleAccountRequest() # SettleAccountRequest |  (optional)

try:
    # Settle Account
    api_response = api_instance.settle_account(login=login, representing=representing, settle_account_request=settle_account_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->settle_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **settle_account_request** | [**SettleAccountRequest**](SettleAccountRequest.md)|  | [optional] 

### Return type

[**SettleAccountResponse**](SettleAccountResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> UpdateApplicationResponse update_application(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
update_application_request = factern_client.UpdateApplicationRequest() # UpdateApplicationRequest |  (optional)

try:
    # Resetting Application Secret
    api_response = api_instance.update_application(login=login, representing=representing, update_application_request=update_application_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **update_application_request** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | [optional] 

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status**
> StandardNodeResponse update_status(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
update_status_request = factern_client.UpdateStatusRequest() # UpdateStatusRequest |  (optional)

try:
    # Enabling/Disabling Nodes
    api_response = api_instance.update_status(login=login, representing=representing, update_status_request=update_status_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **update_status_request** | [**UpdateStatusRequest**](UpdateStatusRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch**
> CreateWatchResponse watch(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_watch_request = factern_client.CreateWatchRequest() # CreateWatchRequest |  (optional)

try:
    # Create Watch Trigger
    api_response = api_instance.watch(login=login, representing=representing, create_watch_request=create_watch_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **create_watch_request** | [**CreateWatchRequest**](CreateWatchRequest.md)|  | [optional] 

### Return type

[**CreateWatchResponse**](CreateWatchResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write**
> WriteResponse write(body, login=login, representing=representing)

### Example
```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
write_request = factern_client.WriteRequest() # WriteRequest |  (optional)

try:
    # Writing by Template
    api_response = api_instance.write(login=login, representing=representing, write_request=write_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->write: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **write_request** | [**WriteRequest**](WriteRequest.md)|  | [optional] 

### Return type

[**WriteResponse**](WriteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

