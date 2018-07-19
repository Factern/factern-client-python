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
body = factern_client.CreateMemberRequest() # CreateMemberRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Member
    api_response = api_instance.add_member(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMemberRequest**](CreateMemberRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateMemberResponse**](CreateMemberResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bid**
> StandardNodeResponse bid(body, login=login, representing=representing)

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
body = factern_client.CreateBidRequest() # CreateBidRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Bid
    api_response = api_instance.bid(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBidRequest**](CreateBidRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alias**
> CreateAliasResponse create_alias(body, login=login, representing=representing)

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
body = factern_client.CreateAliasRequest() # CreateAliasRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Alias
    api_response = api_instance.create_alias(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAliasRequest**](CreateAliasRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateAliasResponse**](CreateAliasResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> CreateApplicationResponse create_application(body, login=login, representing=representing)

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
body = factern_client.CreateApplicationRequest() # CreateApplicationRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Application
    api_response = api_instance.create_application(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain**
> CreateDomainResponse create_domain(body, login=login, representing=representing)

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
body = factern_client.CreateDomainRequest() # CreateDomainRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Domain
    api_response = api_instance.create_domain(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateDomainResponse**](CreateDomainResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> CreateEntityResponse create_entity(body, login=login, representing=representing)

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
body = factern_client.CreateEntityRequest() # CreateEntityRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Entity
    api_response = api_instance.create_entity(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntityRequest**](CreateEntityRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateEntityResponse**](CreateEntityResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_field**
> CreateFieldResponse create_field(body, login=login, representing=representing)

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
body = factern_client.CreateFieldRequest() # CreateFieldRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Field
    api_response = api_instance.create_field(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFieldRequest**](CreateFieldRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateFieldResponse**](CreateFieldResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_filter**
> CreateFilterResponse create_filter(body, login=login, representing=representing)

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
body = factern_client.CreateFilterRequest() # CreateFilterRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Filter
    api_response = api_instance.create_filter(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFilterRequest**](CreateFilterRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateFilterResponse**](CreateFilterResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> CreateGroupResponse create_group(body, login=login, representing=representing)

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
body = factern_client.CreateGroupRequest() # CreateGroupRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Group
    api_response = api_instance.create_group(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateGroupResponse**](CreateGroupResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_information**
> CreateInformationResponse create_information(body, login=login, representing=representing)

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
body = factern_client.CreateInformationRequest() # CreateInformationRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Information
    api_response = api_instance.create_information(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInformationRequest**](CreateInformationRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateInformationResponse**](CreateInformationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interface**
> CreateInterfaceResponse create_interface(body, login=login, representing=representing)

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
body = factern_client.CreateInterfaceRequest() # CreateInterfaceRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Interface
    api_response = api_instance.create_interface(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInterfaceRequest**](CreateInterfaceRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateInterfaceResponse**](CreateInterfaceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_label_list**
> CreateLabelListResponse create_label_list(body, login=login, representing=representing)

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
body = factern_client.CreateLabelListRequest() # CreateLabelListRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Label List
    api_response = api_instance.create_label_list(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_label_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLabelListRequest**](CreateLabelListRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateLabelListResponse**](CreateLabelListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_login**
> CreateLoginResponse create_login(body, login=login, representing=representing)

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
body = factern_client.CreateLoginRequest() # CreateLoginRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Login
    api_response = api_instance.create_login(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLoginRequest**](CreateLoginRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateLoginResponse**](CreateLoginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mirror**
> CreateMirrorResponse create_mirror(body, login=login, representing=representing)

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
body = factern_client.CreateMirrorRequest() # CreateMirrorRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Mirror
    api_response = api_instance.create_mirror(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_mirror: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMirrorRequest**](CreateMirrorRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateMirrorResponse**](CreateMirrorResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price**
> CreatePriceResponse create_price(body, login=login, representing=representing)

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
body = factern_client.CreatePriceRequest() # CreatePriceRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Price
    api_response = api_instance.create_price(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePriceRequest**](CreatePriceRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreatePriceResponse**](CreatePriceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scope**
> CreateScopeResponse create_scope(body, login=login, representing=representing)

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
body = factern_client.CreateScopeRequest() # CreateScopeRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Scope
    api_response = api_instance.create_scope(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateScopeRequest**](CreateScopeRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateScopeResponse**](CreateScopeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_statement**
> AddStatementResponse create_statement(body, login=login, representing=representing)

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
body = factern_client.AddStatementRequest() # AddStatementRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Statement
    api_response = api_instance.create_statement(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddStatementRequest**](AddStatementRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**AddStatementResponse**](AddStatementResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> CreateTemplateResponse create_template(body, login=login, representing=representing)

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
body = factern_client.CreateTemplateRequest() # CreateTemplateRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Template
    api_response = api_instance.create_template(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateTemplateResponse**](CreateTemplateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> DeleteResponse delete(body, login=login, representing=representing)

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
body = factern_client.DeleteRequest() # DeleteRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Deleting
    api_response = api_instance.delete(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteRequest**](DeleteRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> StandardNodeResponse delete_node(body, login=login, representing=representing)

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
body = factern_client.NodeIdRequest() # NodeIdRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Delete Node
    api_response = api_instance.delete_node(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->delete_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeIdRequest**](NodeIdRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe**
> DescribeResponse describe(body, login=login, representing=representing)

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
body = factern_client.DescribeRequest() # DescribeRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Describe
    api_response = api_instance.describe(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->describe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DescribeRequest**](DescribeRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**DescribeResponse**](DescribeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history**
> NodeListing history(body, login=login, representing=representing)

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
body = factern_client.NodeIdRequest() # NodeIdRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # History
    api_response = api_instance.history(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeIdRequest**](NodeIdRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**NodeListing**](NodeListing.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label**
> AddLabelResponse label(body, login=login, representing=representing)

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
body = factern_client.AddLabelRequest() # AddLabelRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Label a Node
    api_response = api_instance.label(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddLabelRequest**](AddLabelRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**AddLabelResponse**](AddLabelResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obliterate**
> StandardNodeResponse obliterate(body, login=login, representing=representing)

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
body = factern_client.NodeIdRequest() # NodeIdRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Obliterating Information Nodes
    api_response = api_instance.obliterate(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->obliterate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeIdRequest**](NodeIdRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission**
> CreatePermissionResponse permission(body, login=login, representing=representing)

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
body = factern_client.CreatePermissionRequest() # CreatePermissionRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Permission
    api_response = api_instance.permission(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePermissionRequest**](CreatePermissionRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreatePermissionResponse**](CreatePermissionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> ReadResponse read(body, login=login, representing=representing)

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
body = factern_client.ReadRequest() # ReadRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Reading
    api_response = api_instance.read(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadRequest**](ReadRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**ReadResponse**](ReadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_information**
> ReadInformationResponse read_information(body, login=login, representing=representing)

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
body = factern_client.ReadInformationRequest() # ReadInformationRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Read Information
    api_response = api_instance.read_information(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->read_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadInformationRequest**](ReadInformationRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**ReadInformationResponse**](ReadInformationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_information**
> Information replace_information(body, login=login, representing=representing)

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
body = factern_client.ReplaceFieldRequest() # ReplaceFieldRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Replace
    api_response = api_instance.replace_information(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->replace_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplaceFieldRequest**](ReplaceFieldRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**Information**](Information.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_permission**
> StandardNodeResponse request_permission(body, login=login, representing=representing)

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
body = factern_client.NodeIdRequest() # NodeIdRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Request Permission
    api_response = api_instance.request_permission(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->request_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeIdRequest**](NodeIdRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_login**
> ResetLoginResponse reset_login(body, login=login, representing=representing)

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
body = factern_client.ResetLoginCredentialsRequest() # ResetLoginCredentialsRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Changing Login Password
    api_response = api_instance.reset_login(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->reset_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetLoginCredentialsRequest**](ResetLoginCredentialsRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**ResetLoginResponse**](ResetLoginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alias**
> SearchAliasResponse search_alias(body, login=login, representing=representing)

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
body = factern_client.SearchAliasRequest() # SearchAliasRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Search For Alias
    api_response = api_instance.search_alias(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->search_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchAliasRequest**](SearchAliasRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**SearchAliasResponse**](SearchAliasResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entity**
> EntityListResponse search_entity(body, login=login, representing=representing)

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
body = factern_client.SearchEntityRequest() # SearchEntityRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Search For Entity
    api_response = api_instance.search_entity(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->search_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchEntityRequest**](SearchEntityRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**EntityListResponse**](EntityListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_account**
> SettleAccountResponse settle_account(body, login=login, representing=representing)

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
body = factern_client.SettleAccountRequest() # SettleAccountRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Settle Account
    api_response = api_instance.settle_account(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->settle_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettleAccountRequest**](SettleAccountRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**SettleAccountResponse**](SettleAccountResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> UpdateApplicationResponse update_application(body, login=login, representing=representing)

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
body = factern_client.UpdateApplicationRequest() # UpdateApplicationRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Resetting Application Secret
    api_response = api_instance.update_application(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status**
> StandardNodeResponse update_status(body, login=login, representing=representing)

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
body = factern_client.UpdateStatusRequest() # UpdateStatusRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Enabling/Disabling Nodes
    api_response = api_instance.update_status(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStatusRequest**](UpdateStatusRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**StandardNodeResponse**](StandardNodeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch**
> CreateWatchResponse watch(body, login=login, representing=representing)

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
body = factern_client.CreateWatchRequest() # CreateWatchRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Create Watch Trigger
    api_response = api_instance.watch(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWatchRequest**](CreateWatchRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**CreateWatchResponse**](CreateWatchResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write**
> WriteResponse write(body, login=login, representing=representing)

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
body = factern_client.WriteRequest() # WriteRequest | 
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)

try:
    # Writing by Template
    api_response = api_instance.write(body, login=login, representing=representing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->write: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteRequest**](WriteRequest.md)|  | 
 **login** | **str**|  | [optional] 
 **representing** | **str**|  | [optional] 

### Return type

[**WriteResponse**](WriteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

