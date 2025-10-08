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
"""Data models for AWS Documentation MCP Server."""

from pydantic import BaseModel
from typing import Optional


class SearchResult(BaseModel):
    """Search result from AWS documentation search."""

    rank_order: int
    url: str
    title: str
    query_id: str
    context: Optional[str] = None


class RecommendationResult(BaseModel):
    """Recommendation result from AWS documentation."""

    url: str
    title: str
    context: Optional[str] = None
