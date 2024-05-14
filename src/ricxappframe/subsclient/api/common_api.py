# coding: utf-8

"""
    RIC subscription

    This is the initial REST API for RIC subscription  # noqa: E501

    OpenAPI spec version: 0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ....ricxappframe.subsclient.api_client import ApiClient


class CommonApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_subscriptions(self, **kwargs):  # noqa: E501
        """Returns list of subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_subscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SubscriptionList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_subscriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_subscriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_subscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """Returns list of subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_subscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SubscriptionList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubscriptionList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscribe(self, **kwargs):  # noqa: E501
        """Subscribe a list of X2AP event triggers to receive messages sent by RAN  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SubscriptionParams subscription_params: Subscription parameters
        :return: SubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subscribe_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.subscribe_with_http_info(**kwargs)  # noqa: E501
            return data

    def subscribe_with_http_info(self, **kwargs):  # noqa: E501
        """Subscribe a list of X2AP event triggers to receive messages sent by RAN  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SubscriptionParams subscription_params: Subscription parameters
        :return: SubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_params']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscribe" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscription_params' in params:
            body_params = params['subscription_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubscriptionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unsubscribe(self, subscription_id, **kwargs):  # noqa: E501
        """Unsubscribe X2AP events from Subscription Manager  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsubscribe(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: The subscriptionId received in the Subscription Response (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unsubscribe_with_http_info(subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.unsubscribe_with_http_info(subscription_id, **kwargs)  # noqa: E501
            return data

    def unsubscribe_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Unsubscribe X2AP events from Subscription Manager  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unsubscribe_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: The subscriptionId received in the Subscription Response (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unsubscribe" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and ('subscription_id' not in params or
                                                       params['subscription_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subscription_id` when calling `unsubscribe`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{subscriptionId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
