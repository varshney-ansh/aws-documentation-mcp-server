# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for data models in the AWS Documentation MCP Server."""

from awslabs.aws_documentation_mcp_server.models import (
    RecommendationResult,
    SearchResult,
)


class TestSearchResult:
    """Tests for SearchResult model."""

    def test_search_result_creation(self):
        """Test creation of SearchResult."""
        result = SearchResult(
            rank_order=1,
            url='https://docs.aws.amazon.com/lambda/latest/dg/welcome.html',
            title='Welcome to AWS Lambda',
            query_id='test-query-id',
            context='AWS Lambda is a compute service...',
        )
        assert result.rank_order == 1
        assert result.url == 'https://docs.aws.amazon.com/lambda/latest/dg/welcome.html'
        assert result.title == 'Welcome to AWS Lambda'
        assert result.query_id == 'test-query-id'
        assert result.context == 'AWS Lambda is a compute service...'

    def test_search_result_without_context(self):
        """Test creation of SearchResult without context."""
        result = SearchResult(
            rank_order=1,
            url='https://docs.aws.amazon.com/lambda/latest/dg/welcome.html',
            title='Welcome to AWS Lambda',
            query_id='test-query-id',
        )
        assert result.rank_order == 1
        assert result.url == 'https://docs.aws.amazon.com/lambda/latest/dg/welcome.html'
        assert result.title == 'Welcome to AWS Lambda'
        assert result.query_id == 'test-query-id'
        assert result.context is None


class TestRecommendationResult:
    """Tests for RecommendationResult model."""

    def test_recommendation_result_creation(self):
        """Test creation of RecommendationResult."""
        result = RecommendationResult(
            url='https://docs.aws.amazon.com/lambda/latest/dg/welcome.html',
            title='Welcome to AWS Lambda',
            context='AWS Lambda is a compute service...',
        )
        assert result.url == 'https://docs.aws.amazon.com/lambda/latest/dg/welcome.html'
        assert result.title == 'Welcome to AWS Lambda'
        assert result.context == 'AWS Lambda is a compute service...'

    def test_recommendation_result_without_context(self):
        """Test creation of RecommendationResult without context."""
        result = RecommendationResult(
            url='https://docs.aws.amazon.com/lambda/latest/dg/welcome.html',
            title='Welcome to AWS Lambda',
        )
        assert result.url == 'https://docs.aws.amazon.com/lambda/latest/dg/welcome.html'
        assert result.title == 'Welcome to AWS Lambda'
        assert result.context is None
