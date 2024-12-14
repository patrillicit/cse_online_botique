#!/bin/bash -eu
#
# Copyright 2024 Your Name
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gke_likeservice_genproto]

# Script to compile Python gRPC protos for likeservice
#
# Requires gRPC tools:
#   pip install -r requirements.txt

python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/likes.proto

# [END gke_likeservice_genproto]
