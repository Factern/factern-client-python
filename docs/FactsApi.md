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
> CreateMemberResponse add_member(login=login, representing=representing, body=body)

Create Member

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
body = factern_client.CreateMemberRequest() # CreateMemberRequest |  (optional)

try:
    # Create Member
    api_response = api_instance.add_member(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateMemberRequest**](CreateMemberRequest.md)|  | [optional] 

### Return type

[**CreateMemberResponse**](CreateMemberResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bid**
> StandardNodeResponse bid(login=login, representing=representing, body=body)

Create Bid

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
body = factern_client.CreateBidRequest() # CreateBidRequest |  (optional)

try:
    # Create Bid
    api_response = api_instance.bid(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateBidRequest**](CreateBidRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alias**
> CreateAliasResponse create_alias(login=login, representing=representing, body=body)

Create Alias

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
body = factern_client.CreateAliasRequest() # CreateAliasRequest |  (optional)

try:
    # Create Alias
    api_response = api_instance.create_alias(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateAliasRequest**](CreateAliasRequest.md)|  | [optional] 

### Return type

[**CreateAliasResponse**](CreateAliasResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> CreateApplicationResponse create_application(login=login, representing=representing, body=body)

Create Application

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
body = factern_client.CreateApplicationRequest() # CreateApplicationRequest |  (optional)

try:
    # Create Application
    api_response = api_instance.create_application(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain**
> CreateDomainResponse create_domain(login=login, representing=representing, body=body)

Create Domain

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
body = factern_client.CreateDomainRequest() # CreateDomainRequest |  (optional)

try:
    # Create Domain
    api_response = api_instance.create_domain(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | [optional] 

### Return type

[**CreateDomainResponse**](CreateDomainResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> CreateEntityResponse create_entity(login=login, representing=representing, body=body)

Create Entity

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
body = factern_client.CreateEntityRequest() # CreateEntityRequest |  (optional)

try:
    # Create Entity
    api_response = api_instance.create_entity(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateEntityRequest**](CreateEntityRequest.md)|  | [optional] 

### Return type

[**CreateEntityResponse**](CreateEntityResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_field**
> CreateFieldResponse create_field(login=login, representing=representing, body=body)

Create Field

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
body = factern_client.CreateFieldRequest() # CreateFieldRequest |  (optional)

try:
    # Create Field
    api_response = api_instance.create_field(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateFieldRequest**](CreateFieldRequest.md)|  | [optional] 

### Return type

[**CreateFieldResponse**](CreateFieldResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_filter**
> CreateFilterResponse create_filter(login=login, representing=representing, body=body)

Create Filter

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
body = factern_client.CreateFilterRequest() # CreateFilterRequest |  (optional)

try:
    # Create Filter
    api_response = api_instance.create_filter(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateFilterRequest**](CreateFilterRequest.md)|  | [optional] 

### Return type

[**CreateFilterResponse**](CreateFilterResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> CreateGroupResponse create_group(login=login, representing=representing, body=body)

Create Group

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
body = factern_client.CreateGroupRequest() # CreateGroupRequest |  (optional)

try:
    # Create Group
    api_response = api_instance.create_group(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | [optional] 

### Return type

[**CreateGroupResponse**](CreateGroupResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_information**
> CreateInformationResponse create_information(login=login, representing=representing, body=body)

Create Information

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
body = factern_client.CreateInformationRequest() # CreateInformationRequest |  (optional)

try:
    # Create Information
    api_response = api_instance.create_information(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateInformationRequest**](CreateInformationRequest.md)|  | [optional] 

### Return type

[**CreateInformationResponse**](CreateInformationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interface**
> CreateInterfaceResponse create_interface(login=login, representing=representing, body=body)

Create Interface

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
body = factern_client.CreateInterfaceRequest() # CreateInterfaceRequest |  (optional)

try:
    # Create Interface
    api_response = api_instance.create_interface(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateInterfaceRequest**](CreateInterfaceRequest.md)|  | [optional] 

### Return type

[**CreateInterfaceResponse**](CreateInterfaceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_label_list**
> CreateLabelListResponse create_label_list(login=login, representing=representing, body=body)

Create Label List

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
body = factern_client.CreateLabelListRequest() # CreateLabelListRequest |  (optional)

try:
    # Create Label List
    api_response = api_instance.create_label_list(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_label_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateLabelListRequest**](CreateLabelListRequest.md)|  | [optional] 

### Return type

[**CreateLabelListResponse**](CreateLabelListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_login**
> CreateLoginResponse create_login(login=login, representing=representing, body=body)

Create Login

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
body = factern_client.CreateLoginRequest() # CreateLoginRequest |  (optional)

try:
    # Create Login
    api_response = api_instance.create_login(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateLoginRequest**](CreateLoginRequest.md)|  | [optional] 

### Return type

[**CreateLoginResponse**](CreateLoginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mirror**
> CreateMirrorResponse create_mirror(login=login, representing=representing, body=body)

Create Mirror

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
body = factern_client.CreateMirrorRequest() # CreateMirrorRequest |  (optional)

try:
    # Create Mirror
    api_response = api_instance.create_mirror(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_mirror: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateMirrorRequest**](CreateMirrorRequest.md)|  | [optional] 

### Return type

[**CreateMirrorResponse**](CreateMirrorResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price**
> CreatePriceResponse create_price(login=login, representing=representing, body=body)

Create Price

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
body = factern_client.CreatePriceRequest() # CreatePriceRequest |  (optional)

try:
    # Create Price
    api_response = api_instance.create_price(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreatePriceRequest**](CreatePriceRequest.md)|  | [optional] 

### Return type

[**CreatePriceResponse**](CreatePriceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scope**
> CreateScopeResponse create_scope(login=login, representing=representing, body=body)

Create Scope

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
body = factern_client.CreateScopeRequest() # CreateScopeRequest |  (optional)

try:
    # Create Scope
    api_response = api_instance.create_scope(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateScopeRequest**](CreateScopeRequest.md)|  | [optional] 

### Return type

[**CreateScopeResponse**](CreateScopeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_statement**
> AddStatementResponse create_statement(login=login, representing=representing, body=body)

Create Statement

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
body = factern_client.AddStatementRequest() # AddStatementRequest |  (optional)

try:
    # Create Statement
    api_response = api_instance.create_statement(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**AddStatementRequest**](AddStatementRequest.md)|  | [optional] 

### Return type

[**AddStatementResponse**](AddStatementResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> CreateTemplateResponse create_template(login=login, representing=representing, body=body)

Create Template

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
body = factern_client.CreateTemplateRequest() # CreateTemplateRequest |  (optional)

try:
    # Create Template
    api_response = api_instance.create_template(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | [optional] 

### Return type

[**CreateTemplateResponse**](CreateTemplateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> DeleteResponse delete(login=login, representing=representing, body=body)

Deleting

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
body = factern_client.DeleteRequest() # DeleteRequest |  (optional)

try:
    # Deleting
    api_response = api_instance.delete(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**DeleteRequest**](DeleteRequest.md)|  | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> StandardNodeResponse delete_node(login=login, representing=representing, body=body)

Delete Node

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
body = factern_client.NodeIdRequest() # NodeIdRequest |  (optional)

try:
    # Delete Node
    api_response = api_instance.delete_node(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->delete_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**NodeIdRequest**](NodeIdRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe**
> DescribeResponse describe(login=login, representing=representing, body=body)

Describe

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
body = factern_client.DescribeRequest() # DescribeRequest |  (optional)

try:
    # Describe
    api_response = api_instance.describe(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->describe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**DescribeRequest**](DescribeRequest.md)|  | [optional] 

### Return type

[**DescribeResponse**](DescribeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history**
> NodeListing history(login=login, representing=representing, body=body)

History

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
body = factern_client.NodeIdRequest() # NodeIdRequest |  (optional)

try:
    # History
    api_response = api_instance.history(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**NodeIdRequest**](NodeIdRequest.md)|  | [optional] 

### Return type

[**NodeListing**](NodeListing.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label**
> AddLabelResponse label(login=login, representing=representing, body=body)

Label a Node

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
body = factern_client.AddLabelRequest() # AddLabelRequest |  (optional)

try:
    # Label a Node
    api_response = api_instance.label(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**AddLabelRequest**](AddLabelRequest.md)|  | [optional] 

### Return type

[**AddLabelResponse**](AddLabelResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obliterate**
> StandardNodeResponse obliterate(login=login, representing=representing, body=body)

Obliterating Information Nodes

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
body = factern_client.NodeIdRequest() # NodeIdRequest |  (optional)

try:
    # Obliterating Information Nodes
    api_response = api_instance.obliterate(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->obliterate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**NodeIdRequest**](NodeIdRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission**
> CreatePermissionResponse permission(login=login, representing=representing, body=body)

Create Permission

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
body = factern_client.CreatePermissionRequest() # CreatePermissionRequest |  (optional)

try:
    # Create Permission
    api_response = api_instance.permission(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreatePermissionRequest**](CreatePermissionRequest.md)|  | [optional] 

### Return type

[**CreatePermissionResponse**](CreatePermissionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> ReadResponse read(login=login, representing=representing, body=body)

Reading

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
body = factern_client.ReadRequest() # ReadRequest |  (optional)

try:
    # Reading
    api_response = api_instance.read(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**ReadRequest**](ReadRequest.md)|  | [optional] 

### Return type

[**ReadResponse**](ReadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_information**
> ReadInformationResponse read_information(login=login, representing=representing, body=body)

Read Information

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
body = factern_client.ReadInformationRequest() # ReadInformationRequest |  (optional)

try:
    # Read Information
    api_response = api_instance.read_information(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->read_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**ReadInformationRequest**](ReadInformationRequest.md)|  | [optional] 

### Return type

[**ReadInformationResponse**](ReadInformationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_information**
> Information replace_information(login=login, representing=representing, body=body)

Replace

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
body = factern_client.ReplaceFieldRequest() # ReplaceFieldRequest |  (optional)

try:
    # Replace
    api_response = api_instance.replace_information(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->replace_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**ReplaceFieldRequest**](ReplaceFieldRequest.md)|  | [optional] 

### Return type

[**Information**](Information.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_permission**
> StandardNodeResponse request_permission(login=login, representing=representing, body=body)

Request Permission

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
body = factern_client.NodeIdRequest() # NodeIdRequest |  (optional)

try:
    # Request Permission
    api_response = api_instance.request_permission(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->request_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**NodeIdRequest**](NodeIdRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_login**
> ResetLoginResponse reset_login(login=login, representing=representing, body=body)

Changing Login Password

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
body = factern_client.ResetLoginCredentialsRequest() # ResetLoginCredentialsRequest |  (optional)

try:
    # Changing Login Password
    api_response = api_instance.reset_login(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->reset_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**ResetLoginCredentialsRequest**](ResetLoginCredentialsRequest.md)|  | [optional] 

### Return type

[**ResetLoginResponse**](ResetLoginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alias**
> SearchAliasResponse search_alias(login=login, representing=representing, body=body)

Search For Alias

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
body = factern_client.SearchAliasRequest() # SearchAliasRequest |  (optional)

try:
    # Search For Alias
    api_response = api_instance.search_alias(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->search_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**SearchAliasRequest**](SearchAliasRequest.md)|  | [optional] 

### Return type

[**SearchAliasResponse**](SearchAliasResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entity**
> EntityListResponse search_entity(login=login, representing=representing, body=body)

Search For Entity

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
body = factern_client.SearchEntityRequest() # SearchEntityRequest |  (optional)

try:
    # Search For Entity
    api_response = api_instance.search_entity(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->search_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**SearchEntityRequest**](SearchEntityRequest.md)|  | [optional] 

### Return type

[**EntityListResponse**](EntityListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_account**
> SettleAccountResponse settle_account(login=login, representing=representing, body=body)

Settle Account

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
body = factern_client.SettleAccountRequest() # SettleAccountRequest |  (optional)

try:
    # Settle Account
    api_response = api_instance.settle_account(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->settle_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**SettleAccountRequest**](SettleAccountRequest.md)|  | [optional] 

### Return type

[**SettleAccountResponse**](SettleAccountResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> UpdateApplicationResponse update_application(login=login, representing=representing, body=body)

Resetting Application Secret

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
body = factern_client.UpdateApplicationRequest() # UpdateApplicationRequest |  (optional)

try:
    # Resetting Application Secret
    api_response = api_instance.update_application(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | [optional] 

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status**
> StandardNodeResponse update_status(login=login, representing=representing, body=body)

Enabling/Disabling Nodes

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
body = factern_client.UpdateStatusRequest() # UpdateStatusRequest |  (optional)

try:
    # Enabling/Disabling Nodes
    api_response = api_instance.update_status(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**UpdateStatusRequest**](UpdateStatusRequest.md)|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch**
> CreateWatchResponse watch(login=login, representing=representing, body=body)

Create Watch Trigger

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
body = factern_client.CreateWatchRequest() # CreateWatchRequest |  (optional)

try:
    # Create Watch Trigger
    api_response = api_instance.watch(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**CreateWatchRequest**](CreateWatchRequest.md)|  | [optional] 

### Return type

[**CreateWatchResponse**](CreateWatchResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write**
> WriteResponse write(login=login, representing=representing, body=body)

Writing by Template

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
body = factern_client.WriteRequest() # WriteRequest |  (optional)

try:
    # Writing by Template
    api_response = api_instance.write(login=login, representing=representing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->write: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 
 **body** | [**WriteRequest**](WriteRequest.md)|  | [optional] 

### Return type

[**WriteResponse**](WriteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

